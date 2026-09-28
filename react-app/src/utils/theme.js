const KEY = 'dc-theme';

export function getThemePreference() {
  try {
    return localStorage.getItem(KEY) || 'system';
  } catch (e) {
    return 'system';
  }
}

export function applyTheme(pref) {
  const root = document.documentElement;
  if (pref === 'light' || pref === 'dark') root.setAttribute('data-theme', pref);
  else root.removeAttribute('data-theme');
  try {
    localStorage.setItem(KEY, pref);
  } catch (e) {
    /* storage unavailable (private mode) */
  }
}
