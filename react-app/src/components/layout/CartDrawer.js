import React, { useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { openCart, setQuantity, clearCart } from '../../store/cart';
import { useToast } from '../../context/Toast';
import Img from '../ui/Img';
import Stepper from '../ui/Stepper';
import { CloseIcon, BagIcon } from '../ui/Icons';
import { money, plural } from '../../utils/format';

export default function CartDrawer() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const toast = useToast();
  const cart = useSelector((s) => s.cart);
  const close = () => dispatch(openCart(false));

  useEffect(() => {
    if (!cart.open) return undefined;
    const onKey = (e) => { if (e.key === 'Escape') dispatch(openCart(false)); };
    document.addEventListener('keydown', onKey);
    document.body.classList.add('no-scroll');
    return () => { document.removeEventListener('keydown', onKey); document.body.classList.remove('no-scroll'); };
  }, [cart.open, dispatch]);

  const change = async (item, qty) => {
    try {
      await dispatch(setQuantity(item.id, Math.max(0, qty)));
    } catch (e) {
      toast(e.message, 'error');
    }
  };

  return (
    <div className={`drawer-root ${cart.open ? 'is-open' : ''}`} aria-hidden={!cart.open}>
      <div className="drawer-backdrop" onClick={close} />
      <aside className="drawer" role="dialog" aria-label="Your cart">
        <div className="drawer-head">
          <div>
            <h2>Your cart</h2>
            {cart.business && (
              <Link to={`/business/${cart.business.id}`} onClick={close} className="muted small">{cart.business.name}</Link>
            )}
          </div>
          <button className="icon-btn" onClick={close} aria-label="Close cart"><CloseIcon /></button>
        </div>

        {cart.items.length === 0 ? (
          <div className="drawer-empty">
            <div className="empty-icon"><BagIcon size={34} /></div>
            <h3>Your cart is empty</h3>
            <p className="muted">Add something delicious to get started.</p>
            <button className="btn btn-primary" onClick={() => { close(); navigate('/all'); }}>Browse restaurants</button>
          </div>
        ) : (
          <>
            <ul className="drawer-items">
              {cart.items.map((item) => (
                <li key={item.id} className="cart-line">
                  <Img src={item.image_id} alt={item.name} />
                  <div className="cart-line-text">
                    <strong>{item.name}</strong>
                    <span className="muted small">{money(item.price)} each</span>
                  </div>
                  <div className="cart-line-side">
                    <span>{money(item.line_total)}</span>
                    <Stepper size="sm" value={item.quantity} min={1} removable onChange={(v) => change(item, v)} />
                  </div>
                </li>
              ))}
            </ul>
            <div className="drawer-foot">
              <div className="row-between">
                <span className="muted">Subtotal · {plural(cart.count, 'item')}</span>
                <strong>{money(cart.subtotal)}</strong>
              </div>
              <button className="btn btn-primary btn-block btn-lg" onClick={() => { close(); navigate('/checkout'); }}>
                Go to checkout
              </button>
              <button className="btn btn-ghost btn-block btn-sm" onClick={() => dispatch(clearCart())}>Clear cart</button>
            </div>
          </>
        )}
      </aside>
    </div>
  );
}
