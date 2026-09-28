import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle, useDebounce } from '../utils/hooks';
import { money, eta, plural } from '../utils/format';
import { loadCart, setQuantity } from '../store/cart';
import { useToast } from '../context/Toast';
import Img from '../components/ui/Img';
import Stepper from '../components/ui/Stepper';
import { EmptyState, ErrorList } from '../components/ui/States';
import { BagIcon, PinIcon, TagIcon, CheckIcon, ClockIcon } from '../components/ui/Icons';

const TIP_OPTIONS = [0, 0.15, 0.18, 0.2];

export default function Checkout() {
  useDocumentTitle('Checkout');
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const toast = useToast();
  const user = useSelector((s) => s.session.user);
  const cart = useSelector((s) => s.cart);
  const [address, setAddress] = useState(user.address || '');
  const [notes, setNotes] = useState('');
  const [tipRate, setTipRate] = useState(0.18);
  const [customTip, setCustomTip] = useState('');
  const [promoInput, setPromoInput] = useState('');
  const [promo, setPromo] = useState('');
  const [quote, setQuote] = useState(null);
  const [promoError, setPromoError] = useState('');
  const [errors, setErrors] = useState([]);
  const [busy, setBusy] = useState(false);

  useEffect(() => { dispatch(loadCart()); }, [dispatch]);

  const tip = tipRate === 'custom'
    ? Math.max(0, Math.min(200, parseFloat(customTip) || 0))
    : Math.round(cart.subtotal * tipRate * 100) / 100;
  const debouncedTip = useDebounce(tip, 300);

  useEffect(() => {
    if (!cart.items.length) { setQuote(null); return; }
    api('/orders/quote', { method: 'POST', body: { tip: debouncedTip, promo_code: promo } })
      .then((q) => { setQuote(q); setPromoError(''); })
      .catch((e) => { setPromoError(e.message); setPromo(''); });
  }, [debouncedTip, promo, cart.subtotal, cart.items.length]);

  if (!cart.items.length) {
    return (
      <div className="container page">
        <EmptyState icon={<BagIcon size={34} />} title="Your cart is empty" action="Find something tasty" to="/all">
          Add dishes from any restaurant to check out.
        </EmptyState>
      </div>
    );
  }

  const placeOrder = async (e) => {
    e.preventDefault();
    setBusy(true);
    setErrors([]);
    try {
      const order = await api('/orders/', { method: 'POST', body: { delivery_address: address, notes, tip, promo_code: promo } });
      await dispatch(loadCart());
      toast('Order placed!');
      navigate(`/orders/${order.id}`, { state: { justPlaced: true } });
    } catch (err) {
      setErrors(err.errors);
      setBusy(false);
    }
  };

  return (
    <div className="container page">
      <header className="page-head">
        <h1>Checkout</h1>
        <p className="muted">From <Link to={`/business/${cart.business.id}`}>{cart.business.name}</Link> · <ClockIcon size={14} /> {eta(cart.business.prep_time)}</p>
      </header>

      <form className="checkout-layout" onSubmit={placeOrder}>
        <div className="checkout-main">
          <section className="panel">
            <h2><PinIcon size={18} /> Delivery details</h2>
            <label className="field">
              <span>Address</span>
              <input value={address} onChange={(e) => setAddress(e.target.value)} autoComplete="street-address" required maxLength={255} placeholder="Street, city, ZIP" />
            </label>
            <label className="field">
              <span>Note for the courier <em>(optional)</em></span>
              <input value={notes} onChange={(e) => setNotes(e.target.value)} maxLength={300} placeholder="Gate code, leave at door…" />
            </label>
          </section>

          <section className="panel">
            <h2><BagIcon size={18} /> {plural(cart.count, 'item')}</h2>
            <ul className="checkout-items">
              {cart.items.map((item) => (
                <li key={item.id} className="cart-line">
                  <Img src={item.image_id} alt="" />
                  <div className="cart-line-text">
                    <strong>{item.name}</strong>
                    <span className="muted small">{money(item.price)}</span>
                  </div>
                  <div className="cart-line-side">
                    <span>{money(item.line_total)}</span>
                    <Stepper size="sm" value={item.quantity} removable onChange={(v) => dispatch(setQuantity(item.id, Math.max(0, v)))} />
                  </div>
                </li>
              ))}
            </ul>
          </section>

          <section className="panel">
            <h2>Tip your courier</h2>
            <p className="muted small">100% of your tip goes to the person delivering your food.</p>
            <div className="segmented">
              {TIP_OPTIONS.map((rate) => (
                <button type="button" key={rate} className={tipRate === rate ? 'is-active' : ''} onClick={() => setTipRate(rate)}>
                  {rate === 0 ? 'None' : `${Math.round(rate * 100)}%`}
                </button>
              ))}
              <button type="button" className={tipRate === 'custom' ? 'is-active' : ''} onClick={() => setTipRate('custom')}>Other</button>
            </div>
            {tipRate === 'custom' && (
              <label className="field inline-field">
                <span>Custom tip ($)</span>
                <input type="number" min="0" max="200" step="0.5" value={customTip} onChange={(e) => setCustomTip(e.target.value)} />
              </label>
            )}
          </section>
        </div>

        <aside className="checkout-summary panel">
          <h2>Summary</h2>
          <div className="promo-row">
            <TagIcon size={18} />
            <input value={promoInput} onChange={(e) => setPromoInput(e.target.value.toUpperCase())} placeholder="Promo code" aria-label="Promo code" />
            <button type="button" className="btn btn-secondary btn-sm" onClick={() => setPromo(promoInput.trim())} disabled={!promoInput.trim()}>Apply</button>
          </div>
          {promoError && <p className="form-errors small">{promoError}</p>}
          {quote && quote.promo_code && <p className="success small"><CheckIcon size={14} /> {quote.promo_code} applied</p>}

          {quote ? (
            <dl className="receipt">
              <div><dt>Subtotal</dt><dd>{money(quote.subtotal)}</dd></div>
              {quote.discount > 0 && <div className="success"><dt>Discount</dt><dd>−{money(quote.discount)}</dd></div>}
              <div><dt>Delivery fee</dt><dd>{quote.delivery_fee === 0 ? 'Free' : money(quote.delivery_fee)}</dd></div>
              <div><dt>Taxes</dt><dd>{money(quote.tax)}</dd></div>
              <div><dt>Tip</dt><dd>{money(quote.tip)}</dd></div>
              <div className="receipt-total"><dt>Total</dt><dd>{money(quote.total)}</dd></div>
            </dl>
          ) : <p className="muted">Calculating…</p>}

          <ErrorList errors={errors} />
          <button className="btn btn-primary btn-block btn-lg" disabled={busy || !quote}>
            {busy ? 'Placing order…' : `Place order${quote ? ` · ${money(quote.total)}` : ''}`}
          </button>
          <p className="hint center">Demo checkout, so no card is charged.</p>
        </aside>
      </form>
    </div>
  );
}
