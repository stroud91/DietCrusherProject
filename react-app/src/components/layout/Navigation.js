import React, { useEffect, useRef, useState } from 'react';
import { Link, NavLink, useLocation, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { openCart } from '../../store/cart';
import { logout } from '../../store/session';
import { useModal } from '../../context/Modal';
import { AuthModal } from '../AuthForms';
import { BagIcon, SearchIcon, PinIcon, UserIcon, ReceiptIcon, HeartIcon, StoreIcon, LogoutIcon } from '../ui/Icons';
import Avatar from '../ui/Avatar';
import logo from '../../images/dc.png';

function AccountMenu({ user }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    if (!open) return undefined;
    const close = (e) => { if (ref.current && !ref.current.contains(e.target)) setOpen(false); };
    const esc = (e) => { if (e.key === 'Escape') setOpen(false); };
    document.addEventListener('mousedown', close);
    document.addEventListener('keydown', esc);
    return () => { document.removeEventListener('mousedown', close); document.removeEventListener('keydown', esc); };
  }, [open]);

  const go = (to) => { setOpen(false); navigate(to); };

  return (
    <div className="account-menu" ref={ref}>
      <button className="avatar-btn" onClick={() => setOpen(!open)} aria-haspopup="menu" aria-expanded={open} aria-label="Account menu">
        <Avatar src={user.profile_image_id} name={user.firstName ? `${user.firstName} ${user.lastName || ''}` : user.username} size={40} />
      </button>
      {open && (
        <div className="menu-popover" role="menu">
          <div className="menu-header">
            <strong>{user.firstName ? `${user.firstName} ${user.lastName || ''}` : user.username}</strong>
            <span className="muted small">{user.email}</span>
          </div>
          <button role="menuitem" onClick={() => go('/orders')}><ReceiptIcon size={18} /> Orders</button>
          <button role="menuitem" onClick={() => go('/favorites')}><HeartIcon size={18} /> Favorites</button>
          <button role="menuitem" onClick={() => go('/owned')}><StoreIcon size={18} /> My restaurants</button>
          <button role="menuitem" onClick={() => go('/account')}><UserIcon size={18} /> Account</button>
          <hr />
          <button role="menuitem" onClick={async () => { setOpen(false); await dispatch(logout()); navigate('/'); }}>
            <LogoutIcon size={18} /> Sign out
          </button>
        </div>
      )}
    </div>
  );
}

export default function Navigation() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const location = useLocation();
  const user = useSelector((s) => s.session.user);
  const count = useSelector((s) => s.cart.count);
  const { openModal, closeModal } = useModal();
  const [q, setQ] = useState('');
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    if (location.pathname === '/search') setQ(new URLSearchParams(location.search).get('q') || '');
  }, [location]);

  const onSearch = (e) => {
    e.preventDefault();
    navigate(q.trim() ? `/search?q=${encodeURIComponent(q.trim())}` : '/all');
  };

  const onHero = location.pathname === '/' && !scrolled;

  return (
    <header className={`topbar ${scrolled ? 'is-scrolled' : ''} ${onHero ? 'is-on-hero' : ''}`}>
      <div className="topbar-inner">
        <Link to="/" className="brand" aria-label="Diet Crusher home">
          <img src={logo} alt="" />
          <span>Diet Crusher</span>
        </Link>

        {user && user.address && (
          <Link to="/account" className="deliver-to" title="Change delivery address">
            <PinIcon size={16} />
            <span className="ellipsis">{user.address}</span>
          </Link>
        )}

        <form className="topbar-search" onSubmit={onSearch} role="search">
          <SearchIcon size={18} />
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="Food, restaurants, cuisines" aria-label="Search" />
        </form>

        <nav className="topbar-actions">
          <NavLink to="/all" className="nav-link hide-sm">Restaurants</NavLink>
          {user && <NavLink to="/orders" className="nav-link hide-sm">Orders</NavLink>}
          {user && (
            <button className="cart-btn" onClick={() => dispatch(openCart(true))} aria-label={`Cart, ${count} items`}>
              <BagIcon size={18} />
              <span>{count}</span>
            </button>
          )}
          {user ? (
            <AccountMenu user={user} />
          ) : (
            <>
              <button className="btn btn-ghost btn-sm hide-sm" onClick={() => openModal(<AuthModal onDone={closeModal} />)}>Sign in</button>
              <button className="btn btn-primary btn-sm" onClick={() => openModal(<AuthModal mode="signup" onDone={closeModal} />)}>Sign up</button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
