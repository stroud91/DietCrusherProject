import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle } from '../utils/hooks';
import { money, eta, mapsUrl } from '../utils/format';
import { loadBusinesses } from '../store/business';
import { useModal } from '../context/Modal';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import { RatingPill } from '../components/ui/Rating';
import { Spinner, EmptyState } from '../components/ui/States';
import { MenuItem } from '../components/DishCard';
import { FavoriteButton } from '../components/RestaurantCard';
import ConfirmDialog from '../components/ConfirmDialog';
import { PinIcon, PhoneIcon, ShareIcon, ClockIcon, BikeIcon, EditIcon, TrashIcon, PlusIcon, ChartIcon, StoreIcon } from '../components/ui/Icons';

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-');

export default function Restaurant() {
  const { id } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const user = useSelector((s) => s.session.user);
  const { openModal } = useModal();
  const toast = useToast();
  const [business, setBusiness] = useState(null);
  const [missing, setMissing] = useState(false);
  const [active, setActive] = useState('');
  useDocumentTitle(business ? business.name : 'Restaurant');

  const load = useCallback(() => api(`/business/${id}`)
    .then(setBusiness)
    .catch(() => setMissing(true)), [id]);

  useEffect(() => { setBusiness(null); setMissing(false); load(); window.scrollTo(0, 0); }, [load]);

  const sections = useMemo(() => {
    if (!business) return [];
    const groups = {};
    business.dishes.forEach((d) => {
      const key = d.category_name || 'Menu';
      (groups[key] = groups[key] || []).push(d);
    });
    return Object.entries(groups);
  }, [business]);

  useEffect(() => {
    if (!sections.length || !('IntersectionObserver' in window)) return undefined;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) setActive(e.target.id); });
    }, { rootMargin: '-140px 0px -65% 0px' });
    sections.forEach(([name]) => {
      const el = document.getElementById(`cat-${slug(name)}`);
      if (el) observer.observe(el);
    });
    return () => observer.disconnect();
  }, [sections]);

  if (missing) return <div className="container page"><EmptyState icon={<StoreIcon size={34} />} title="Restaurant not found" action="Browse restaurants" to="/all" /></div>;
  if (!business) return <Spinner />;

  const isOwner = user && user.id === business.owner_id;

  const share = async () => {
    const data = { title: business.name, text: `Order from ${business.name} on Diet Crusher`, url: window.location.href };
    try {
      if (navigator.share) await navigator.share(data);
      else { await navigator.clipboard.writeText(data.url); toast('Link copied'); }
    } catch (e) { /* user dismissed the share sheet */ }
  };

  const dishAction = async (fn, message) => {
    try { await fn(); await load(); toast(message); } catch (e) { toast(e.message, 'error'); }
  };

  const ownerTools = (dish) => isOwner && (
    <div className="owner-tools" onClick={(e) => { e.preventDefault(); e.stopPropagation(); }}>
      <button className="btn btn-secondary btn-xs" onClick={() => navigate(`/business/${business.id}/update-dish/${dish.id}`)}><EditIcon size={14} /> Edit</button>
      <button className="btn btn-secondary btn-xs" onClick={() => dishAction(
        () => api(`/menu/${dish.id}/availability`, { method: 'PATCH', body: { is_available: !dish.is_available } }),
        dish.is_available ? `${dish.name} marked sold out` : `${dish.name} is available again`)}>
        {dish.is_available ? 'Mark sold out' : 'Mark available'}
      </button>
      <button className="btn btn-danger-ghost btn-xs" onClick={() => openModal(
        <ConfirmDialog title="Delete this dish?" message={`${dish.name} and its reviews will be removed permanently.`} confirmLabel="Delete dish"
          onConfirm={() => dishAction(() => api(`/menu/${dish.id}`, { method: 'DELETE' }), 'Dish deleted')} />)}>
        <TrashIcon size={14} /> Delete
      </button>
    </div>
  );

  return (
    <div className="restaurant-page">
      <div className="restaurant-hero">
        <Img src={business.logo_id} alt="" className="restaurant-hero-img" />
        <div className="restaurant-hero-shade" />
      </div>

      <div className="container">
        <div className="restaurant-info glass-card">
          <div className="restaurant-info-main">
            <p className="eyebrow">{business.cuisines.join(' · ')}</p>
            <h1>{business.name}</h1>
            <div className="meta-row">
              <RatingPill rating={business.rating} count={business.review_count} />
              <span><BikeIcon size={16} /> {money(business.delivery_fee)} delivery</span>
              <span><ClockIcon size={16} /> {eta(business.prep_time)}</span>
            </div>
            <p className="muted restaurant-about">{business.about}</p>
            <div className="meta-row small">
              <a href={mapsUrl(business)} target="_blank" rel="noopener noreferrer"><PinIcon size={16} /> {business.address}, {business.city}, {business.state}</a>
              <a href={`tel:${business.phone}`}><PhoneIcon size={16} /> {business.phone}</a>
            </div>
          </div>
          <div className="restaurant-info-actions">
            <FavoriteButton businessId={business.id} className="fav-inline" />
            <button className="icon-btn bordered" onClick={share} aria-label="Share"><ShareIcon size={18} /></button>
          </div>
        </div>

        {isOwner && (
          <div className="owner-bar">
            <span className="pill">You own this restaurant</span>
            <div className="owner-bar-actions">
              <Link className="btn btn-secondary btn-sm" to={`/owned/${business.id}/orders`}><ChartIcon size={16} /> Orders & stats</Link>
              <Link className="btn btn-secondary btn-sm" to={`/update-business/${business.id}`}><EditIcon size={16} /> Edit details</Link>
              <Link className="btn btn-primary btn-sm" to={`/business/${business.id}/create-dish`}><PlusIcon size={16} /> Add dish</Link>
            </div>
          </div>
        )}

        {sections.length > 0 && (
          <nav className="menu-tabs" aria-label="Menu categories">
            {sections.map(([name]) => (
              <a key={name} href={`#cat-${slug(name)}`} className={`chip ${active === `cat-${slug(name)}` ? 'is-active' : ''}`}
                onClick={(e) => {
                  e.preventDefault();
                  document.getElementById(`cat-${slug(name)}`).scrollIntoView({ behavior: 'smooth', block: 'start' });
                }}>
                {name}
              </a>
            ))}
          </nav>
        )}

        {sections.length === 0 ? (
          <EmptyState title="No dishes yet" action={isOwner ? 'Add your first dish' : null} to={`/business/${business.id}/create-dish`}>
            {isOwner ? 'Build your menu to start taking orders.' : 'This kitchen is still writing its menu. Check back soon.'}
          </EmptyState>
        ) : sections.map(([name, dishes]) => (
          <section key={name} id={`cat-${slug(name)}`} className="menu-section">
            <h2>{name}</h2>
            <div className="menu-grid">
              {dishes.map((d) => <MenuItem key={d.id} dish={d} ownerTools={ownerTools(d)} />)}
            </div>
          </section>
        ))}

        {isOwner && (
          <div className="danger-zone">
            <button className="btn btn-danger-ghost btn-sm" onClick={() => openModal(
              <ConfirmDialog title="Delete this restaurant?" message="Its menu and reviews will be removed permanently. Past orders keep their receipts."
                confirmLabel="Delete restaurant"
                onConfirm={async () => {
                  await api(`/business/${business.id}`, { method: 'DELETE' });
                  await dispatch(loadBusinesses(true));
                  toast('Restaurant deleted');
                  navigate('/owned');
                }} />)}>
              <TrashIcon size={16} /> Delete restaurant
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
