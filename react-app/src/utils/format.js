const currency = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });

export const money = (value) => currency.format(Number(value) || 0);

export const shortDate = (iso) =>
  iso ? new Date(iso).toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' }) : '';

export const dateTime = (iso) =>
  iso ? new Date(iso).toLocaleString(undefined, { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }) : '';

export const eta = (prepTime = 25) => `${prepTime}–${prepTime + 10} min`;

export const plural = (n, word) => `${n} ${word}${n === 1 ? '' : 's'}`;

export const ORDER_STEPS = ['Placed', 'Preparing', 'On the way', 'Delivered'];

export function mapsUrl(business) {
  const q = encodeURIComponent(`${business.address}, ${business.city}, ${business.state} ${business.zip_code}`);
  return `https://maps.google.com/?q=${q}`;
}
