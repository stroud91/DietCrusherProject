import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle } from '../utils/hooks';
import { loadBusinesses } from '../store/business';
import { authenticate } from '../store/session';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import { Spinner, ErrorList, EmptyState } from '../components/ui/States';

const EMPTY = { name: '', about: '', type: '', address: '', city: '', state: '', zip_code: '', phone_number: '', email: '', logo_id: '', delivery_fee: '2.99', prep_time: '25' };

export default function BusinessForm() {
  const { id } = useParams();
  const editing = Boolean(id);
  useDocumentTitle(editing ? 'Edit restaurant' : 'New restaurant');
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const toast = useToast();
  const user = useSelector((s) => s.session.user);
  const [form, setForm] = useState(editing ? null : EMPTY);
  const [errors, setErrors] = useState([]);
  const [busy, setBusy] = useState(false);
  const [denied, setDenied] = useState(false);

  useEffect(() => {
    if (!editing) return;
    api(`/business/${id}`).then((b) => {
      if (b.owner_id !== user.id) { setDenied(true); return; }
      setForm({
        name: b.name, about: b.about, type: b.type, address: b.address, city: b.city, state: b.state,
        zip_code: b.zip_code, phone_number: b.phone, email: b.email || '', logo_id: b.logo_id,
        delivery_fee: String(b.delivery_fee), prep_time: String(b.prep_time),
      });
    }).catch(() => setDenied(true));
  }, [editing, id, user.id]);

  if (denied) return <div className="container page"><EmptyState title="You can only edit your own restaurants" action="My restaurants" to="/owned" /></div>;
  if (!form) return <Spinner />;

  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value });

  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    setErrors([]);
    const body = { ...form, delivery_fee: parseFloat(form.delivery_fee) || 0, prep_time: parseInt(form.prep_time, 10) || 25 };
    try {
      const saved = await api(editing ? `/business/${id}` : '/business/', { method: editing ? 'PUT' : 'POST', body });
      await dispatch(loadBusinesses(true));
      if (!editing) dispatch(authenticate());
      toast(editing ? 'Restaurant updated' : 'Restaurant created. Now add some dishes!');
      navigate(`/business/${saved.id}`);
    } catch (err) {
      setErrors(err.errors);
      setBusy(false);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  return (
    <div className="container page form-page">
      <header className="page-head">
        <h1>{editing ? 'Edit restaurant' : 'Open your restaurant'}</h1>
        <p className="muted">{editing ? 'Keep your details fresh for customers.' : 'Tell customers who you are. You can add dishes next.'}</p>
      </header>
      <div className="form-layout">
        <form className="panel" onSubmit={submit}>
          <ErrorList errors={errors} />
          <label className="field"><span>Restaurant name</span><input value={form.name} onChange={set('name')} required minLength={2} maxLength={50} /></label>
          <label className="field"><span>Cuisine</span><input value={form.type} onChange={set('type')} required maxLength={255} placeholder="e.g. Japanese, Sushi Bars" /></label>
          <label className="field"><span>About</span><textarea rows={4} value={form.about} onChange={set('about')} required maxLength={500} placeholder="What makes your kitchen special?" /></label>
          <label className="field"><span>Cover image URL</span><input type="url" value={form.logo_id} onChange={set('logo_id')} required placeholder="https://images.unsplash.com/…" /></label>
          <label className="field"><span>Street address</span><input value={form.address} onChange={set('address')} required maxLength={255} autoComplete="street-address" /></label>
          <div className="field-row three">
            <label className="field"><span>City</span><input value={form.city} onChange={set('city')} required maxLength={50} /></label>
            <label className="field"><span>State</span><input value={form.state} onChange={set('state')} required maxLength={2} placeholder="CO" /></label>
            <label className="field"><span>ZIP</span><input value={form.zip_code} onChange={set('zip_code')} required inputMode="numeric" maxLength={10} /></label>
          </div>
          <div className="field-row">
            <label className="field"><span>Phone</span><input type="tel" value={form.phone_number} onChange={set('phone_number')} required placeholder="(303) 555-0100" /></label>
            <label className="field"><span>Email <em>(optional)</em></span><input type="email" value={form.email} onChange={set('email')} /></label>
          </div>
          <div className="field-row">
            <label className="field"><span>Delivery fee ($)</span><input type="number" min="0" max="50" step="0.01" value={form.delivery_fee} onChange={set('delivery_fee')} /></label>
            <label className="field"><span>Prep time (min)</span><input type="number" min="5" max="120" value={form.prep_time} onChange={set('prep_time')} /></label>
          </div>
          <div className="action-row">
            <button type="button" className="btn btn-secondary" onClick={() => navigate(-1)}>Cancel</button>
            <button className="btn btn-primary" disabled={busy}>{busy ? 'Saving…' : editing ? 'Save changes' : 'Create restaurant'}</button>
          </div>
        </form>
        <aside className="preview">
          <p className="eyebrow">Preview</p>
          <div className="restaurant-card static">
            <div className="restaurant-media"><Img src={form.logo_id} alt="" /></div>
            <div className="restaurant-body">
              <h3>{form.name || 'Your restaurant'}</h3>
              <p className="muted small">${Number(form.delivery_fee || 0).toFixed(2)} delivery · {form.prep_time || 25}–{(parseInt(form.prep_time, 10) || 25) + 10} min</p>
              <p className="muted small">{form.type || 'Cuisine'}</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}
