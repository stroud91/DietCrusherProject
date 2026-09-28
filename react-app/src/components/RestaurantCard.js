import React from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import Img from './ui/Img';
import { RatingPill } from './ui/Rating';
import { HeartIcon } from './ui/Icons';
import { toggleFavorite } from '../store/favorites';
import { money, eta } from '../utils/format';
import { useToast } from '../context/Toast';

export function FavoriteButton({ businessId, className = '' }) {
  const dispatch = useDispatch();
  const user = useSelector((s) => s.session.user);
  const isFav = useSelector((s) => s.favorites.ids.includes(businessId));
  const toast = useToast();
  if (!user) return null;
  const onClick = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    try {
      await dispatch(toggleFavorite(businessId, isFav));
      toast(isFav ? 'Removed from favorites' : 'Saved to favorites');
    } catch (err) {
      toast(err.message, 'error');
    }
  };
  return (
    <button className={`fav-btn ${isFav ? 'is-on' : ''} ${className}`} onClick={onClick}
      aria-pressed={isFav} aria-label={isFav ? 'Remove from favorites' : 'Save to favorites'}>
      <HeartIcon filled={isFav} size={18} />
    </button>
  );
}

export default function RestaurantCard({ business }) {
  return (
    <Link to={`/business/${business.id}`} className="restaurant-card">
      <div className="restaurant-media">
        <Img src={business.logo_id} alt={business.name} />
        <FavoriteButton businessId={business.id} />
        {business.delivery_fee === 0 && <span className="media-badge">Free delivery</span>}
      </div>
      <div className="restaurant-body">
        <div className="restaurant-title">
          <h3>{business.name}</h3>
          <RatingPill rating={business.rating} />
        </div>
        <p className="muted small">
          {money(business.delivery_fee)} delivery · {eta(business.prep_time)}
        </p>
        <p className="muted small ellipsis">{business.cuisines.join(' · ')}</p>
      </div>
    </Link>
  );
}
