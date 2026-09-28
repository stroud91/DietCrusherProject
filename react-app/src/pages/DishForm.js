import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle } from '../utils/hooks';
import { money } from '../utils/format';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import { Spinner, ErrorList, EmptyState } from '../components/ui/States';

export default function DishForm() {
  const { businessId, id } = useParams();
  const editing = Boolean(id);
  useDocumentTitle(editing ? 'Edit dish' : 'New dish');
  const navigate = useNavigate();
  const toast = useToast();
  const user = useSelector((s) => s.session.user);
  const [business, setBusiness] = useState(null);
  const [categories, setCategories] = useState([]);
  const [form, setForm] = useState(null);
  const [errors, setErrors] = useState([]);
  const [busy, setBusy] = useState(false);
  const [denied, setDenied] = useState(false);

  useEffect(() => {
    api('/categories').then((d) => setCategories(d.categories));
    api(`/business/${businessId}`).then((b) => {
      if (b.owner_id !== user.id) { setDenied(true); return; }
      setBusiness(b);
      if (editing) {
        const dish = b.dishes.find((d) => String(d.id) === id);
        if (!dish) { setDenied(true); return; }
        setForm({ name: dish.name, description: dish.description || '', price: String(dish.price), image_id: dish.image_id,
          category_id: String(dish.category_id || ''), calories: dish.calories != null ? String(dish.calories) : '' });
      } else {
        setForm({ name: '', description: '', price: '', image_id: '', category_id: '', calories: '' });
      }
    }).catch(() => setDenied(true));
  }, [businessId, id, editing, user.id]);

  if (denied) return <div className="container page"><EmptyState title="You can only manage your own menus" action="My restaurants" to="/owned" /></div>;
  if (!form || !business) return <Spinner />;

  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value });

  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    setErrors([]);
    const body = {
      ...form,
      price: parseFloat(form.price),
      category_id: parseInt(form.category_id, 10),
      calories: form.calories === '' ? null : parseInt(form.calories, 10),
    };
    try {
      await api(editing ? `/menu/${id}` : `/menu/business/${businessId}`, { method: editing ? 'PUT' : 'POST', body });
      toast(editing ? 'Dish updated' : 'Dish added to your menu');
      navigate(`/business/${businessId}`);
    } catch (err) {
      setErrors(err.errors);
      setBusy(false);
    }
  };

  return (
    <div className="container page form-page">
      <header className="page-head">
        <p className="eyebrow">{business.name}</p>
        <h1>{editing ? 'Edit dish' : 'Add a dish'}</h1>
      </header>
      <div className="form-layout">
        <form className="panel" onSubmit={submit}>
          <ErrorList errors={errors} />
          <label className="field"><span>Name</span><input value={form.name} onChange={set('name')} required minLength={2} maxLength={100} /></label>
          <label className="field"><span>Description</span><textarea rows={3} value={form.description} onChange={set('description')} maxLength={500} placeholder="Ingredients, portion size, what makes it great" /></label>
          <div className="field-row three">
            <label className="field"><span>Price ($)</span><input type="number" min="0.5" max="1000" step="0.01" value={form.price} onChange={set('price')} required /></label>
            <label className="field"><span>Calories <em>(optional)</em></span><input type="number" min="0" max="5000" value={form.calories} onChange={set('calories')} /></label>
            <label className="field"><span>Category</span>
              <select value={form.category_id} onChange={set('category_id')} required>
                <option value="" disabled>Choose…</option>
                {categories.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
              </select>
            </label>
          </div>
          <label className="field"><span>Photo URL</span><input type="url" value={form.image_id} onChange={set('image_id')} required placeholder="https://…" /></label>
          <div className="action-row">
            <button type="button" className="btn btn-secondary" onClick={() => navigate(-1)}>Cancel</button>
            <button className="btn btn-primary" disabled={busy}>{busy ? 'Saving…' : editing ? 'Save changes' : 'Add dish'}</button>
          </div>
        </form>
        <aside className="preview">
          <p className="eyebrow">Preview</p>
          <div className="menu-item static">
            <div className="menu-item-text">
              <h4>{form.name || 'Dish name'}</h4>
              <p className="menu-item-meta"><span>{money(form.price || 0)}</span>{form.calories && <span className="muted">{form.calories} Cal</span>}</p>
              <p className="muted small clamp-2">{form.description}</p>
            </div>
            <div className="menu-item-media"><Img src={form.image_id} alt="" /></div>
          </div>
        </aside>
      </div>
    </div>
  );
}
