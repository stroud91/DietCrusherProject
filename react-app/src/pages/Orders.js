import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle } from '../utils/hooks';
import { money, shortDate, plural } from '../utils/format';
import { reorder, openCart } from '../store/cart';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import { Spinner, EmptyState } from '../components/ui/States';
import { ReceiptIcon, ChevronRight } from '../components/ui/Icons';

export function StatusPill({ status }) {
  return <span className={`status-pill status-${status.toLowerCase().replace(/\s+/g, '-')}`}>{status}</span>;
}

export default function Orders() {
  useDocumentTitle('Your orders');
  const dispatch = useDispatch();
  const toast = useToast();
  const [orders, setOrders] = useState(null);

  useEffect(() => { api('/orders/').then((d) => setOrders(d.orders)).catch(() => setOrders([])); }, []);

  const again = async (e, order) => {
    e.preventDefault();
    try {
      await dispatch(reorder(order.id));
      dispatch(openCart(true));
    } catch (err) { toast(err.message, 'error'); }
  };

  if (!orders) return <Spinner />;
  const active = orders.filter((o) => !['Delivered', 'Cancelled'].includes(o.status));
  const past = orders.filter((o) => ['Delivered', 'Cancelled'].includes(o.status));

  const list = (items) => (
    <div className="order-list">
      {items.map((o) => (
        <Link key={o.id} to={`/orders/${o.id}`} className="order-card">
          <Img src={o.business_logo} alt="" />
          <div className="order-card-body">
            <strong>{o.business_name || `Order #${o.id}`}</strong>
            <span className="muted small">{plural(o.item_count, 'item')} · {money(o.total_price)} · {shortDate(o.created_at)}</span>
            <StatusPill status={o.status} />
          </div>
          <div className="order-card-side">
            {o.business_id && <button className="btn btn-secondary btn-sm" onClick={(e) => again(e, o)}>Reorder</button>}
            <ChevronRight size={18} />
          </div>
        </Link>
      ))}
    </div>
  );

  return (
    <div className="container page narrow">
      <header className="page-head"><h1>Orders</h1></header>
      {orders.length === 0 ? (
        <EmptyState icon={<ReceiptIcon size={34} />} title="No orders yet" action="Start an order" to="/all">
          When you place an order, you can track it here.
        </EmptyState>
      ) : (
        <>
          {active.length > 0 && <section className="section"><h2>In progress</h2>{list(active)}</section>}
          {past.length > 0 && <section className="section"><h2>Past orders</h2>{list(past)}</section>}
        </>
      )}
    </div>
  );
}
