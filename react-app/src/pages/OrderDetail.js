import React, { useCallback, useEffect, useState } from 'react';
import { Link, useLocation, useParams, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle, usePolling } from '../utils/hooks';
import { money, dateTime, ORDER_STEPS } from '../utils/format';
import { reorder, openCart } from '../store/cart';
import { useModal } from '../context/Modal';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import { Spinner, EmptyState } from '../components/ui/States';
import ConfirmDialog from '../components/ConfirmDialog';
import { StatusPill } from './Orders';
import { CheckIcon, PinIcon, ChevronLeft } from '../components/ui/Icons';

const STEP_COPY = {
  Placed: 'The restaurant has your order.',
  Preparing: 'Your food is being prepared.',
  'On the way': 'Your courier is heading to you.',
  Delivered: 'Enjoy your meal!',
};

export default function OrderDetail() {
  const { id } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { openModal } = useModal();
  const toast = useToast();
  const [order, setOrder] = useState(null);
  const [missing, setMissing] = useState(false);
  useDocumentTitle(order ? `Order #${order.id}` : 'Order');

  const load = useCallback(() => api(`/orders/${id}`).then(setOrder).catch(() => setMissing(true)), [id]);
  useEffect(() => { load(); }, [load]);
  const live = order && !['Delivered', 'Cancelled'].includes(order.status);
  usePolling(load, 10000, !!live);

  if (missing) return <div className="container page"><EmptyState title="Order not found" action="Your orders" to="/orders" /></div>;
  if (!order) return <Spinner />;

  const cancelled = order.status === 'Cancelled';
  const stepIndex = ORDER_STEPS.indexOf(order.status);

  return (
    <div className="container page narrow">
      <button className="back-link" onClick={() => navigate('/orders')}><ChevronLeft size={18} /> Orders</button>
      {location.state && location.state.justPlaced && (
        <div className="success-banner"><CheckIcon size={20} /> Order confirmed. We'll keep this page updated.</div>
      )}

      <header className="page-head">
        <p className="eyebrow">Order #{order.id} · {dateTime(order.created_at)}</p>
        <h1>{cancelled ? 'Order cancelled' : STEP_COPY[order.status] || order.status}</h1>
        <StatusPill status={order.status} />
      </header>

      {!cancelled && (
        <ol className="timeline" aria-label="Order progress">
          {ORDER_STEPS.map((step, i) => (
            <li key={step} className={i < stepIndex ? 'is-done' : i === stepIndex ? 'is-current' : ''}>
              <span className="dot">{i < stepIndex || order.status === 'Delivered' ? <CheckIcon size={12} /> : null}</span>
              <span>{step}</span>
            </li>
          ))}
        </ol>
      )}
      {live && <p className="hint">Live: this page refreshes automatically.</p>}

      <section className="panel">
        <div className="row-between">
          <h2>{order.business_id ? <Link to={`/business/${order.business_id}`}>{order.business_name}</Link> : 'Your order'}</h2>
        </div>
        <p className="muted small"><PinIcon size={14} /> {order.delivery_address}</p>
        {order.notes && <p className="muted small">Note: {order.notes}</p>}
        <ul className="checkout-items">
          {(order.items || []).map((item) => (
            <li key={item.dish_id} className="cart-line">
              <Img src={item.image_id} alt="" />
              <div className="cart-line-text">
                <strong>{item.quantity} × {item.name}</strong>
              </div>
              <div className="cart-line-side"><span>{money(item.subtotal_price)}</span></div>
            </li>
          ))}
        </ul>
        <dl className="receipt">
          {order.subtotal != null && <div><dt>Subtotal</dt><dd>{money(order.subtotal)}</dd></div>}
          {order.discount > 0 && <div className="success"><dt>Discount {order.promo_code && `(${order.promo_code})`}</dt><dd>−{money(order.discount)}</dd></div>}
          {order.delivery_fee != null && <div><dt>Delivery fee</dt><dd>{money(order.delivery_fee)}</dd></div>}
          {order.tax != null && <div><dt>Taxes</dt><dd>{money(order.tax)}</dd></div>}
          {order.tip != null && <div><dt>Tip</dt><dd>{money(order.tip)}</dd></div>}
          <div className="receipt-total"><dt>Total</dt><dd>{money(order.total_price)}</dd></div>
        </dl>
      </section>

      <div className="action-row">
        {order.business_id && (
          <button className="btn btn-primary" onClick={async () => {
            try { await dispatch(reorder(order.id)); dispatch(openCart(true)); } catch (e) { toast(e.message, 'error'); }
          }}>Reorder</button>
        )}
        {order.status === 'Placed' && (
          <button className="btn btn-danger-ghost" onClick={() => openModal(
            <ConfirmDialog title="Cancel this order?" message="The restaurant hasn't started preparing it yet." confirmLabel="Cancel order"
              onConfirm={async () => { setOrder(await api(`/orders/${order.id}/cancel`, { method: 'POST' })); toast('Order cancelled'); }} />)}>
            Cancel order
          </button>
        )}
      </div>
    </div>
  );
}
