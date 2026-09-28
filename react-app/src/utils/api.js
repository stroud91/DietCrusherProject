function readCookie(name) {
  const match = document.cookie.split('; ').find((row) => row.startsWith(`${name}=`));
  return match ? decodeURIComponent(match.split('=').slice(1).join('=')) : '';
}

export class ApiError extends Error {
  constructor(status, data) {
    const errors = (data && data.errors) || ['Something went wrong. Please try again.'];
    super(errors[0]);
    this.status = status;
    this.errors = errors;
    this.data = data || {};
  }
}

/**
 * JSON fetch wrapper. Every non-GET request carries the CSRF token that Flask
 * sets in the `csrf_token` cookie, which the server validates globally.
 */
export async function api(path, { method = 'GET', body, signal } = {}) {
  const headers = { Accept: 'application/json' };
  if (body !== undefined) headers['Content-Type'] = 'application/json';
  if (method !== 'GET') headers['X-CSRFToken'] = readCookie('csrf_token');

  const res = await fetch(`/api${path}`, {
    method,
    headers,
    body: body === undefined ? undefined : JSON.stringify(body),
    credentials: 'same-origin',
    signal,
  });

  let data = null;
  try {
    data = await res.json();
  } catch (e) {
    data = null;
  }
  if (!res.ok) throw new ApiError(res.status, data);
  return data;
}
