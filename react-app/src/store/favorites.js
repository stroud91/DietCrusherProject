import { api } from '../utils/api';

const SET = 'favorites/SET';
const TOGGLE = 'favorites/TOGGLE';

export const resetFavorites = () => ({ type: SET, ids: [] });

export const loadFavorites = () => async (dispatch) => {
  const { businesses } = await api('/favorites/');
  dispatch({ type: SET, ids: businesses.map((b) => b.id) });
  return businesses;
};

export const toggleFavorite = (businessId, isFavorite) => async (dispatch) => {
  dispatch({ type: TOGGLE, id: businessId, on: !isFavorite });
  try {
    await api(`/favorites/${businessId}`, { method: isFavorite ? 'DELETE' : 'PUT' });
  } catch (e) {
    dispatch({ type: TOGGLE, id: businessId, on: isFavorite });
    throw e;
  }
};

export default function favoritesReducer(state = { ids: [] }, action) {
  switch (action.type) {
    case SET:
      return { ids: action.ids };
    case TOGGLE: {
      const ids = state.ids.filter((id) => id !== action.id);
      return { ids: action.on ? [...ids, action.id] : ids };
    }
    default:
      return state;
  }
}
