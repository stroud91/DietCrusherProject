import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { login, demoLogin, signUp } from '../store/session';
import { ErrorList } from './ui/States';
import logo from '../images/dc.png';

export function LoginForm({ onDone, onSwitch }) {
  const dispatch = useDispatch();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState([]);
  const [busy, setBusy] = useState(false);

  const run = async (action) => {
    setBusy(true);
    setErrors([]);
    try {
      await dispatch(action);
      if (onDone) onDone();
    } catch (e) {
      setErrors(e.errors || [e.message]);
      setBusy(false);
    }
  };

  return (
    <form className="auth-form" onSubmit={(e) => { e.preventDefault(); run(login(email, password)); }}>
      <img src={logo} alt="" className="auth-logo" />
      <h1>Welcome back</h1>
      <p className="muted">Sign in to order, track deliveries and save favorites.</p>
      <ErrorList errors={errors} />
      <label className="field">
        <span>Email</span>
        <input type="email" autoComplete="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </label>
      <label className="field">
        <span>Password</span>
        <input type="password" autoComplete="current-password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </label>
      <button className="btn btn-primary btn-block btn-lg" disabled={busy}>{busy ? 'Signing in…' : 'Sign in'}</button>
      <button type="button" className="btn btn-secondary btn-block" disabled={busy} onClick={() => run(demoLogin())}>
        Explore with the demo account
      </button>
      {onSwitch && (
        <p className="auth-switch">New here? <button type="button" className="link-btn" onClick={onSwitch}>Create an account</button></p>
      )}
    </form>
  );
}

export function SignupForm({ onDone, onSwitch }) {
  const dispatch = useDispatch();
  const [form, setForm] = useState({ username: '', email: '', password: '', confirm: '', first_name: '', last_name: '', address: '', phone: '' });
  const [errors, setErrors] = useState([]);
  const [busy, setBusy] = useState(false);
  const set = (key) => (e) => setForm({ ...form, [key]: e.target.value });

  const submit = async (e) => {
    e.preventDefault();
    if (form.password !== form.confirm) return setErrors(['Passwords do not match.']);
    setBusy(true);
    setErrors([]);
    try {
      const { confirm, ...payload } = form;
      await dispatch(signUp(payload));
      if (onDone) onDone();
    } catch (err) {
      setErrors(err.errors || [err.message]);
      setBusy(false);
    }
    return null;
  };

  return (
    <form className="auth-form" onSubmit={submit}>
      <img src={logo} alt="" className="auth-logo" />
      <h1>Create your account</h1>
      <p className="muted">Great food from local kitchens, delivered.</p>
      <ErrorList errors={errors} />
      <div className="field-row">
        <label className="field"><span>First name</span><input autoComplete="given-name" value={form.first_name} onChange={set('first_name')} /></label>
        <label className="field"><span>Last name</span><input autoComplete="family-name" value={form.last_name} onChange={set('last_name')} /></label>
      </div>
      <label className="field"><span>Username</span><input autoComplete="username" value={form.username} onChange={set('username')} required minLength={3} maxLength={30} /></label>
      <label className="field"><span>Email</span><input type="email" autoComplete="email" value={form.email} onChange={set('email')} required /></label>
      <div className="field-row">
        <label className="field"><span>Password</span><input type="password" autoComplete="new-password" value={form.password} onChange={set('password')} required minLength={8} /></label>
        <label className="field"><span>Confirm</span><input type="password" autoComplete="new-password" value={form.confirm} onChange={set('confirm')} required /></label>
      </div>
      <p className="hint">At least 8 characters, including a letter and a number.</p>
      <label className="field"><span>Delivery address <em>(optional)</em></span><input autoComplete="street-address" value={form.address} onChange={set('address')} /></label>
      <button className="btn btn-primary btn-block btn-lg" disabled={busy}>{busy ? 'Creating account…' : 'Create account'}</button>
      {onSwitch && (
        <p className="auth-switch">Already have an account? <button type="button" className="link-btn" onClick={onSwitch}>Sign in</button></p>
      )}
    </form>
  );
}

/** Modal wrapper that can flip between sign-in and sign-up. */
export function AuthModal({ mode: initial = 'login', onDone }) {
  const [mode, setMode] = useState(initial);
  return mode === 'login'
    ? <LoginForm onDone={onDone} onSwitch={() => setMode('signup')} />
    : <SignupForm onDone={onDone} onSwitch={() => setMode('login')} />;
}
