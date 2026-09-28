import React from 'react';
import { StarIcon } from './Icons';

export function RatingPill({ rating, count, className = '' }) {
  if (rating == null) return <span className={`rating-pill is-new ${className}`}>New</span>;
  return (
    <span className={`rating-pill ${className}`}>
      <StarIcon size={13} /> {Number(rating).toFixed(1)}
      {count != null && <span className="muted"> ({count})</span>}
    </span>
  );
}

export function Stars({ value = 0, size = 16 }) {
  return (
    <span className="stars" aria-label={`${value} out of 5 stars`}>
      {[1, 2, 3, 4, 5].map((n) => (
        <StarIcon key={n} size={size} filled={n <= Math.round(value)} className={n <= Math.round(value) ? 'on' : 'off'} />
      ))}
    </span>
  );
}

export function StarInput({ value, onChange }) {
  const [hover, setHover] = React.useState(0);
  const shown = hover || value;
  return (
    <div className="star-input" role="radiogroup" aria-label="Rating" onMouseLeave={() => setHover(0)}>
      {[1, 2, 3, 4, 5].map((n) => (
        <button
          type="button"
          key={n}
          role="radio"
          aria-checked={value === n}
          aria-label={`${n} star${n > 1 ? 's' : ''}`}
          className={n <= shown ? 'on' : 'off'}
          onMouseEnter={() => setHover(n)}
          onClick={() => onChange(n)}
        >
          <StarIcon size={30} filled={n <= shown} />
        </button>
      ))}
    </div>
  );
}
