import React from 'react';
import { Navigate, useLocation, useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { LoginForm, SignupForm } from '../components/AuthForms';
import { useDocumentTitle } from '../utils/hooks';

export default function AuthPage({ mode }) {
  useDocumentTitle(mode === 'login' ? 'Sign in' : 'Sign up');
  const user = useSelector((s) => s.session.user);
  const navigate = useNavigate();
  const location = useLocation();
  const from = (location.state && location.state.from) || '/';
  if (user) return <Navigate to={from} replace />;
  const done = () => navigate(from, { replace: true });
  return (
    <div className="auth-page">
      <div className="auth-card">
        {mode === 'login'
          ? <LoginForm onDone={done} onSwitch={() => navigate('/signup', { state: location.state })} />
          : <SignupForm onDone={done} onSwitch={() => navigate('/login', { state: location.state })} />}
      </div>
    </div>
  );
}
