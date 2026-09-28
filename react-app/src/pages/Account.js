import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { api } from '../utils/api';
import { useDocumentTitle } from '../utils/hooks';
import { getThemePreference, applyTheme } from '../utils/theme';
import { updateProfile, logout } from '../store/session';
import { useToast } from '../context/Toast';
import { ErrorList } from '../components/ui/States';
import Avatar from '../components/ui/Avatar';
import { HeartIcon, ReceiptIcon, StoreIcon, SunIcon, MoonIcon, LogoutIcon, ChevronRight } from '../components/ui/Icons';

export default function Account() {
  useDocumentTitle('Account');
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const toast = useToast();
  const user = useSelector((s) => s.session.user);
  const [profile, setProfile] = useState({
    first_name: user.firstName || '', last_name: user.lastName || '', address: user.address || '',
    phone: user.phone || '', profile_image_id: user.profile_image_id || '',
  });
  const [pw, setPw] = useState({ current_password: '', new_password: '' });
  const [errors, setErrors] = useState([]);
  const [pwErrors, setPwErrors] = useState([]);
  const [theme, setTheme] = useState(getThemePreference());
  const set = (k) => (e) => setProfile({ ...profile, [k]: e.target.value });

  const saveProfile = async (e) => {
    e.preventDefault();
    setErrors([]);
    try { await dispatch(updateProfile(profile)); toast('Profile saved'); } catch (err) { setErrors(err.errors); }
  };

  const savePassword = async (e) => {
    e.preventDefault();
    setPwErrors([]);
    try {
      await api('/auth/password', { method: 'POST', body: pw });
      setPw({ current_password: '', new_password: '' });
      toast('Password updated');
    } catch (err) { setPwErrors(err.errors); }
  };

  const chooseTheme = (t) => { setTheme(t); applyTheme(t); };

  return (
    <div className="container page narrow">
      <header className="account-head">
        <Avatar src={user.profile_image_id} name={user.firstName || user.username} size={84} className="account-avatar" />
        <div>
          <h1>{user.firstName ? `${user.firstName} ${user.lastName || ''}` : user.username}</h1>
          <p className="muted">@{user.username} · {user.email}</p>
        </div>
      </header>

      <nav className="list-links panel">
        <Link to="/orders"><ReceiptIcon /> Orders <ChevronRight size={18} /></Link>
        <Link to="/favorites"><HeartIcon /> Favorites <ChevronRight size={18} /></Link>
        <Link to="/owned"><StoreIcon /> My restaurants <ChevronRight size={18} /></Link>
      </nav>

      <section className="panel">
        <h2>Appearance</h2>
        <div className="segmented">
          <button type="button" className={theme === 'system' ? 'is-active' : ''} onClick={() => chooseTheme('system')}>Automatic</button>
          <button type="button" className={theme === 'light' ? 'is-active' : ''} onClick={() => chooseTheme('light')}><SunIcon size={16} /> Light</button>
          <button type="button" className={theme === 'dark' ? 'is-active' : ''} onClick={() => chooseTheme('dark')}><MoonIcon size={16} /> Dark</button>
        </div>
      </section>

      <form className="panel" onSubmit={saveProfile}>
        <h2>Profile</h2>
        <ErrorList errors={errors} />
        <div className="field-row">
          <label className="field"><span>First name</span><input value={profile.first_name} onChange={set('first_name')} maxLength={50} /></label>
          <label className="field"><span>Last name</span><input value={profile.last_name} onChange={set('last_name')} maxLength={50} /></label>
        </div>
        <label className="field"><span>Default delivery address</span><input value={profile.address} onChange={set('address')} maxLength={255} /></label>
        <label className="field"><span>Phone</span><input type="tel" value={profile.phone} onChange={set('phone')} maxLength={30} /></label>
        <label className="field"><span>Avatar image URL</span><input type="url" value={profile.profile_image_id} onChange={set('profile_image_id')} placeholder="https://…" /></label>
        <button className="btn btn-primary">Save profile</button>
      </form>

      <form className="panel" onSubmit={savePassword}>
        <h2>Password</h2>
        <ErrorList errors={pwErrors} />
        <div className="field-row">
          <label className="field"><span>Current password</span><input type="password" autoComplete="current-password" value={pw.current_password} onChange={(e) => setPw({ ...pw, current_password: e.target.value })} required /></label>
          <label className="field"><span>New password</span><input type="password" autoComplete="new-password" value={pw.new_password} onChange={(e) => setPw({ ...pw, new_password: e.target.value })} required minLength={8} /></label>
        </div>
        <button className="btn btn-secondary">Update password</button>
      </form>

      <button className="btn btn-danger-ghost btn-block" onClick={async () => { await dispatch(logout()); navigate('/'); }}>
        <LogoutIcon size={18} /> Sign out
      </button>
    </div>
  );
}
