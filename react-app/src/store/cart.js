import { api } from '../utils/api';

const SET_CART = 'cart/SET_CART';
const SET_OPEN = 'cart/SET_OPEN';
const RESET = 'cart/RESET';

const empty = { id: null, business: null, items: [], count: 0, subtotal: 0 };

export const setCart = (cart) => ({ type: SET_CART, cart });
export const openCart = (open = true) => ({ type: SET_OPEN, open });
export const resetCart = () => ({ type: RESET });

export const loadCart = () => async (dispatch) => {
  dispatch(setCart(await api('/cart/')));
};

/** Throws ApiError; err.data.code === 'DIFFERENT_BUSINESS' means the caller should confirm replace. */
export const addToCart = (dishId, quantity = 1, replace = false) => async (dispatch) => {
  const cart = await api('/cart/items', { method: 'POST', body: { dish_id: dishId, quantity, replace } });
  dispatch(setCart(cart));
  return cart;
};

export const setQuantity = (itemId, quantity) => async (dispatch) => {
  dispatch(setCart(await api(`/cart/items/${itemId}`, { method: 'PATCH', body: { quantity } })));
};

export const clearCart = () => async (dispatch) => {
  dispatch(setCart(await api('/cart/', { method: 'DELETE' })));
};

export const reorder = (orderId) => async (dispatch) => {
  const cart = await api(`/orders/${orderId}/reorder`, { method: 'POST' });
  dispatch(setCart(cart));
  return cart;
};

export default function cartReducer(state = { ...empty, open: false }, action) {
  switch (action.type) {
    case SET_CART:
      return { ...state, ...action.cart };
    case SET_OPEN:
      return { ...state, open: action.open };
    case RESET:
      return { ...empty, open: false };
    default:
      return state;
  }
}
