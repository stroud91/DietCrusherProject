import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { HomeIcon, SearchIcon, ReceiptIcon, UserIcon } from '../ui/Icons';

/** iOS-style bottom tab bar shown on phones. */
export default function TabBar() {
  const user = useSelector((s) => s.session.user);
  return (
    <nav className="tabbar" aria-label="Primary">
      <NavLink to="/" end><HomeIcon /><span>Home</span></NavLink>
      <NavLink to="/all"><SearchIcon /><span>Browse</span></NavLink>
      <NavLink to={user ? '/orders' : '/login'}><ReceiptIcon /><span>Orders</span></NavLink>
      <NavLink to={user ? '/account' : '/login'}><UserIcon /><span>Account</span></NavLink>
    </nav>
  );
}
