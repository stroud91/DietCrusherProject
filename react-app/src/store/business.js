import { api } from '../utils/api';

const SET_ALL = 'business/SET_ALL';

export const loadBusinesses = (force = false) => async (dispatch, getState) => {
  const { loaded } = getState().business;
  if (loaded && !force) return getState().business.list;
  const { businesses } = await api('/business/');
  dispatch({ type: SET_ALL, list: businesses });
  return businesses;
};

export default function businessReducer(state = { list: [], loaded: false }, action) {
  switch (action.type) {
    case SET_ALL:
      return { list: action.list, loaded: true };
    default:
      return state;
  }
}
