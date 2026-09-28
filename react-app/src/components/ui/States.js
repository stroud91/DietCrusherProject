import React from 'react';
import { Link } from 'react-router-dom';

export function Spinner({ label = 'Loading' }) {
  return (
    <div className="spinner-wrap" role="status">
      <span className="spinner" />
      <span className="sr-only">{label}</span>
    </div>
  );
}

export function SkeletonGrid({ count = 6 }) {
  return (
    <div className="card-grid">
      {Array.from({ length: count }).map((_, i) => (
        <div className="skeleton-card" key={i}>
          <div className="skeleton skeleton-img" />
          <div className="skeleton skeleton-line" />
          <div className="skeleton skeleton-line short" />
        </div>
      ))}
    </div>
  );
}

export function EmptyState({ icon, title, children, action, to }) {
  return (
    <div className="empty-state">
      {icon && <div className="empty-icon">{icon}</div>}
      <h2>{title}</h2>
      {children && <p>{children}</p>}
      {action && to && <Link className="btn btn-primary" to={to}>{action}</Link>}
    </div>
  );
}

export function ErrorList({ errors }) {
  if (!errors || errors.length === 0) return null;
  return (
    <ul className="form-errors" role="alert">
      {errors.map((e, i) => <li key={i}>{e}</li>)}
    </ul>
  );
}
