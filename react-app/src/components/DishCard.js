import React from 'react';
import { Link } from 'react-router-dom';
import Img from './ui/Img';
import { PlusIcon, StarIcon, FlameIcon } from './ui/Icons';
import { money } from '../utils/format';
import useCartActions from './useCartActions';

/** Tall tile used in horizontal scrollers on the home page. */
export function DishTile({ dish, badge }) {
  const add = useCartActions();
  return (
    <Link to={`/dish/${dish.id}`} className="dish-tile">
      <div className="dish-tile-media">
        <Img src={dish.image_id} alt={dish.name} />
        {badge && <span className="media-badge">{badge}</span>}
        {dish.is_available && (
          <button className="quick-add" aria-label={`Add ${dish.name} to cart`}
            onClick={(e) => { e.preventDefault(); e.stopPropagation(); add(dish); }}>
            <PlusIcon size={18} />
          </button>
        )}
      </div>
      <div className="dish-tile-body">
        <h3>{dish.name}</h3>
        <p className="muted small ellipsis">{dish.business_name}</p>
        <p className="small">
          <strong>{money(dish.price)}</strong>
          {dish.rating != null && <span className="muted"> · <StarIcon size={12} /> {dish.rating.toFixed(1)}</span>}
        </p>
      </div>
    </Link>
  );
}

/** Uber Eats-style menu row: text on the left, photo with + on the right. */
export function MenuItem({ dish, ownerTools }) {
  const add = useCartActions();
  const soldOut = !dish.is_available;
  return (
    <Link to={`/dish/${dish.id}`} className={`menu-item ${soldOut ? 'is-sold-out' : ''}`}>
      <div className="menu-item-text">
        <h4>{dish.name}</h4>
        <p className="menu-item-meta">
          <span>{money(dish.price)}</span>
          {dish.calories != null && <span className="muted"><FlameIcon size={13} /> {dish.calories} Cal</span>}
          {dish.rating != null && <span className="muted"><StarIcon size={12} /> {dish.rating.toFixed(1)} ({dish.review_count})</span>}
          {soldOut && <span className="pill pill-muted">Sold out</span>}
        </p>
        {dish.description && <p className="muted small clamp-2">{dish.description}</p>}
        {ownerTools}
      </div>
      <div className="menu-item-media">
        <Img src={dish.image_id} alt={dish.name} />
        {!soldOut && !ownerTools && (
          <button className="quick-add" aria-label={`Add ${dish.name} to cart`}
            onClick={(e) => { e.preventDefault(); e.stopPropagation(); add(dish); }}>
            <PlusIcon size={18} />
          </button>
        )}
      </div>
    </Link>
  );
}
