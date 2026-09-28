import React, { useCallback, useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { api } from '../utils/api';
import { useDocumentTitle, usePolling } from '../utils/hooks';
import { money, dateTime, ORDER_STEPS } from '../utils/format';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import { RatingPill } from '../components/ui/Rating';
import { Spinner, EmptyState } from '../components/ui/States';
import { StatusPill } from './Orders';
import { StoreIcon, PlusIcon, ChartIcon, EditIcon, ChevronLeft } from '../components/ui/Icons';

export function OwnerDashboard() {
  useDocumentTitle('My restaurants');
  const [businesses, setBusinesses] = useState(null);
  useEffect(() => { api('/business/mine').then((d) => setBusinesses(d.businesses)).catch(() => setBusinesses([])); }, []);

  if (!businesses) return <Spinner />;
  return (
    <div className="container page">
      <header className="page-head row-between">
        <div>
          <h1>My restaurants</h1>
          <p className="muted">Manage menus, track orders and see how you're doing.</p>
        </div>
        <Link to="/create-business" className="btn btn-primary"><PlusIcon size={18} /> New restaurant</Link>
      </header>
      {businesses.length === 0 ? (
        <EmptyState icon={<StoreIcon size={34} />} title="Open your first restaurant" action="Create a restaurant" to="/create-business">
          List your kitchen on Diet Crusher and start taking orders today.
        </EmptyState>
      ) : (
        <div className="owner-grid">
          {businesses.map((b) => (
            <article key={b.id} className="owner-card">
              <Img src={b.logo_id} alt="" />
              <div className="owner-card-body">
                <div className="row-between">
                  <h3>{b.name}</h3>
                  <RatingPill rating={b.rating} count={b.review_count} />
                </div>
                <p className="muted small">{b.address}, {b.city}</p>
                <div className="owner-card-actions">
                  <Link className="btn btn-primary btn-sm" to={`/owned/${b.id}/orders`}><ChartIcon size={16} /> Orders</Link>
                  <Link className="btn btn-secondary btn-sm" to={`/business/${b.id}`}>Menu</Link>
                  <Link className="btn btn-secondary btn-sm" to={`/update-business/${b.id}`}><EditIcon size={16} /> Edit</Link>
                </div>
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  );
}

function nextStatus(status) {
  const i = ORDER_STEPS.indexOf(status);
  return i >= 0 && i < ORDER_STEPS.length - 1 ? ORDER_STEPS[i + 1] : null;
}

export function OwnerOrders() {
  const { id } = useParams();
  const toast = useToast();
  const [business, setBusiness] = useState(null);
  const [stats, setStats] = useState(null);
  const [orders, setOrders] = useState(null);
  const [filter, setFilter] = useState('active');
  const [denied, setDenied] = useState(false);
  useDocumentTitle(business ? `${business.name} orders` : 'Orders');

  const load = useCallback(() => Promise.all([
    api(`/owner/business/${id}/orders`).then((d) => setOrders(d.orders)),
    api(`/owner/business/${id}/stats`).then(setStats),
  ]).catch(() => setDenied(true)), [id]);

  useEffect(() => { api(`/business/${id}`).then(setBusiness).catch(() => setDenied(true)); load(); }, [id, load]);
  usePolling(load, 15000);

  if (denied) return <div className="container page"><EmptyState title="Restaurant not found" action="My restaurants" to="/owned" /></div>;
  if (!orders || !stats || !business) return <Spinner />;

  const update = async (order, status) => {
    try {
      const updated = await api(`/owner/orders/${order.id}/status`, { method: 'PATCH', body: { status } });
      setOrders((list) => list.map((o) => (o.id === updated.id ? updated : o)));
      api(`/owner/business/${id}/stats`).then(setStats);
      toast(`Order #${order.id} → ${status}`);
    } catch (e) { toast(e.message, 'error'); }
  };

  const closed = (o) => ['Delivered', 'Cancelled'].includes(o.status);
  const shown = orders.filter((o) => (filter === 'active' ? !closed(o) : filter === 'closed' ? closed(o) : true));

  return (
    <div className="container page">
      <Link to="/owned" className="back-link"><ChevronLeft size={18} /> My restaurants</Link>
      <header className="page-head">
        <h1>{business.name}</h1>
        <p className="muted">Live order board: refreshes every 15 seconds.</p>
      </header>

      <div className="stat-grid">
        <div className="stat"><span className="muted small">Revenue</span><strong>{money(stats.revenue)}</strong></div>
        <div className="stat"><span className="muted small">Orders</span><strong>{stats.orders}</strong></div>
        <div className="stat"><span className="muted small">Average order</span><strong>{money(stats.average_order)}</strong></div>
        <div className="stat"><span className="muted small">Rating</span><strong>{stats.rating != null ? `${stats.rating.toFixed(1)} ★` : '—'}</strong><span className="muted small">{stats.review_count} reviews</span></div>
      </div>

      {stats.top_dishes.length > 0 && (
        <section className="panel">
          <h2>Best sellers</h2>
          <div className="bar-list">
            {stats.top_dishes.map((d) => (
              <div key={d.id} className="bar-list-row">
                <span className="ellipsis">{d.name}</span>
                <div className="bar"><div style={{ width: `${(d.quantity / stats.top_dishes[0].quantity) * 100}%` }} /></div>
                <span className="muted small">{d.quantity}</span>
              </div>
            ))}
          </div>
        </section>
      )}

      <div className="segmented">
        {[['active', 'Active'], ['closed', 'Completed'], ['all', 'All']].map(([k, label]) => (
          <button key={k} className={filter === k ? 'is-active' : ''} onClick={() => setFilter(k)}>{label}</button>
        ))}
      </div>

      {shown.length === 0 ? <p className="muted pad">No orders here.</p> : (
        <div className="board">
          {shown.map((o) => {
            const next = nextStatus(o.status);
            return (
              <article key={o.id} className="board-card">
                <header className="row-between">
                  <strong>#{o.id} · {o.customer}</strong>
                  <StatusPill status={o.status} />
                </header>
                <p className="muted small">{dateTime(o.created_at)} · {o.delivery_address}</p>
                <ul className="small">
                  {(o.items || []).map((i) => <li key={i.dish_id}>{i.quantity} × {i.name}</li>)}
                </ul>
                {o.notes && <p className="small note">“{o.notes}”</p>}
                <footer className="row-between">
                  <strong>{money(o.total_price)}</strong>
                  {!closed(o) && (
                    <div className="board-actions">
                      <button className="btn btn-ghost btn-xs" onClick={() => update(o, 'Cancelled')}>Cancel</button>
                      {next && <button className="btn btn-primary btn-xs" onClick={() => update(o, next)}>Mark {next.toLowerCase()}</button>}
                    </div>
                  )}
                </footer>
              </article>
            );
          })}
        </div>
      )}
    </div>
  );
}
