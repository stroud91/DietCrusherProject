import { api } from '../utils/api';
import { loadCart, resetCart } from './cart';
import { loadFavorites, resetFavorites } from './favorites';

const SET_USER = 'session/SET_USER';

export const setUser = (user) => ({ type: SET_USER, user });

async function afterLogin(dispatch, user) {
  dispatch(setUser(user));
  if (user) {
    dispatch(loadCart());
    dispatch(loadFavorites());
  } else {
    dispatch(resetCart());
    dispatch(resetFavorites());
  }
  return user;
}

export const authenticate = () => async (dispatch) => {
  try {
    const { user } = await api('/auth/');
    return afterLogin(dispatch, user);
  } catch (e) {
    return afterLogin(dispatch, null);
  }
};

export const login = (email, password) => async (dispatch) => {
  const { user } = await api('/auth/login', { method: 'POST', body: { email, password } });
  return afterLogin(dispatch, user);
};

export const demoLogin = () => login('alice@wonderland.ioo', 'passwordAlice');

export const signUp = (payload) => async (dispatch) => {
  const { user } = await api('/auth/signup', { method: 'POST', body: payload });
  return afterLogin(dispatch, user);
};

export const updateProfile = (payload) => async (dispatch) => {
  const { user } = await api('/auth/profile', { method: 'PATCH', body: payload });
  dispatch(setUser(user));
  return user;
};

export const logout = () => async (dispatch) => {
  await api('/auth/logout', { method: 'POST' });
  return afterLogin(dispatch, null);
};

export default function sessionReducer(state = { user: null }, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.user };
    default:
      return state;
  }
}
