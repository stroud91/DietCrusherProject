import React, { useCallback, useEffect, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle } from '../utils/hooks';
import { money, shortDate, plural } from '../utils/format';
import { useModal } from '../context/Modal';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import Avatar from '../components/ui/Avatar';
import Stepper from '../components/ui/Stepper';
import { Stars } from '../components/ui/Rating';
import { Spinner, EmptyState } from '../components/ui/States';
import ReviewModal from '../components/ReviewModal';
import ConfirmDialog from '../components/ConfirmDialog';
import useCartActions from '../components/useCartActions';
import { AuthModal } from '../components/AuthForms';
import { ChevronLeft, FlameIcon, StarIcon } from '../components/ui/Icons';

export default function Dish() {
  const { id } = useParams();
  const navigate = useNavigate();
  const user = useSelector((s) => s.session.user);
  const { openModal, closeModal } = useModal();
  const toast = useToast();
  const add = useCartActions();
  const [dish, setDish] = useState(null);
  const [reviews, setReviews] = useState(null);
  const [owner, setOwner] = useState(null);
  const [qty, setQty] = useState(1);
  const [missing, setMissing] = useState(false);
  useDocumentTitle(dish ? dish.name : 'Dish');

  const loadReviews = useCallback(() => api(`/review/dish/${id}`).then(setReviews), [id]);

  useEffect(() => {
    setDish(null); setQty(1); setMissing(false);
    api(`/menu/${id}`).then((d) => {
      setDish(d);
      return api(`/business/${d.business_id}`).then((b) => setOwner(b.owner_id));
    }).catch(() => setMissing(true));
    loadReviews().catch(() => {});
  }, [id, loadReviews]);

  if (missing) return <div className="container page"><EmptyState title="Dish not found" action="Browse restaurants" to="/all" /></div>;
  if (!dish || !reviews) return <Spinner />;

  const isOwner = user && owner === user.id;
  const mine = user && reviews.reviews.find((r) => r.user_id === user.id);
  const { summary } = reviews;

  const refresh = () => { loadReviews(); api(`/menu/${id}`).then(setDish); };
  const writeReview = () => (user
    ? openModal(<ReviewModal dish={dish} review={mine} onSaved={() => { refresh(); toast('Thanks for your review'); }} />)
    : openModal(<AuthModal onDone={closeModal} />));

  return (
    <div className="container page dish-page">
      <button className="back-link" onClick={() => navigate(-1)}><ChevronLeft size={18} /> Back</button>
      <div className="dish-layout">
        <div className="dish-hero-img"><Img src={dish.image_id} alt={dish.name} /></div>
        <div className="dish-panel">
          <Link to={`/business/${dish.business_id}`} className="eyebrow">{dish.business_name}</Link>
          <h1>{dish.name}</h1>
          <div className="meta-row">
            <span className="price-lg">{money(dish.price)}</span>
            {dish.calories != null && <span className="pill"><FlameIcon size={14} /> {dish.calories} Cal</span>}
            {dish.category_name && <span className="pill pill-muted">{dish.category_name}</span>}
          </div>
          {summary.average != null && (
            <p className="rating-line"><Stars value={summary.average} /> <strong>{summary.average.toFixed(1)}</strong> <span className="muted">· {plural(summary.count, 'review')}</span></p>
          )}
          {dish.description && <p className="muted dish-desc">{dish.description}</p>}

          {!isOwner && (dish.is_available ? (
            <div className="buy-row">
              <Stepper value={qty} onChange={setQty} min={1} />
              <button className="btn btn-primary btn-lg grow" onClick={() => add(dish, qty)}>
                Add {qty} to cart · {money(dish.price * qty)}
              </button>
            </div>
          ) : <p className="pill pill-muted">Sold out today</p>)}
          {isOwner && (
            <div className="buy-row">
              <Link className="btn btn-secondary" to={`/business/${dish.business_id}/update-dish/${dish.id}`}>Edit dish</Link>
              <button className="btn btn-danger-ghost" onClick={() => openModal(
                <ConfirmDialog title="Delete this dish?" message="This removes the dish and its reviews permanently." confirmLabel="Delete dish"
                  onConfirm={async () => { await api(`/menu/${dish.id}`, { method: 'DELETE' }); toast('Dish deleted'); navigate(`/business/${dish.business_id}`); }} />)}>
                Delete
              </button>
            </div>
          )}
        </div>
      </div>

      <section className="section reviews">
        <div className="section-head">
          <h2>Ratings & reviews</h2>
          {!isOwner && <button className="btn btn-secondary btn-sm" onClick={writeReview}>{mine ? 'Edit your review' : 'Write a review'}</button>}
        </div>

        {summary.count > 0 && (
          <div className="rating-summary">
            <div className="rating-big">
              <strong>{summary.average.toFixed(1)}</strong>
              <span className="muted small">out of 5</span>
            </div>
            <div className="rating-bars">
              {[5, 4, 3, 2, 1].map((star) => (
                <div key={star} className="rating-bar">
                  <span className="small muted">{star} <StarIcon size={11} /></span>
                  <div className="bar"><div style={{ width: `${(summary.distribution[star] / summary.count) * 100}%` }} /></div>
                </div>
              ))}
            </div>
          </div>
        )}

        {reviews.reviews.length === 0 ? (
          <p className="muted">No reviews yet. Be the first to share what you think.</p>
        ) : (
          <div className="review-list">
            {reviews.reviews.map((r) => (
              <article key={r.id} className="review-card">
                <header>
                  <Avatar src={r.profile_image_id} name={r.user_name} size={40} />
                  <div>
                    <strong>{r.user_name}</strong>
                    <span className="muted small">{shortDate(r.review_date || r.created_at)}</span>
                  </div>
                  <Stars value={r.rating} size={14} />
                </header>
                <p>{r.comment}</p>
                {user && r.user_id === user.id && (
                  <div className="review-actions">
                    <button className="link-btn" onClick={writeReview}>Edit</button>
                    <button className="link-btn danger" onClick={() => openModal(
                      <ConfirmDialog title="Delete your review?" message="This can't be undone." confirmLabel="Delete"
                        onConfirm={async () => { await api(`/review/${r.id}`, { method: 'DELETE' }); refresh(); toast('Review deleted'); }} />)}>
                      Delete
                    </button>
                  </div>
                )}
              </article>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
