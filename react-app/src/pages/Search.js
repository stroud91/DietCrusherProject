import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { api } from '../utils/api';
import { useDebounce, useDocumentTitle } from '../utils/hooks';
import RestaurantCard from '../components/RestaurantCard';
import { MenuItem } from '../components/DishCard';
import { EmptyState, SkeletonGrid } from '../components/ui/States';
import { SearchIcon } from '../components/ui/Icons';

export default function Search() {
  const [params, setParams] = useSearchParams();
  const initial = params.get('q') || '';
  const [q, setQ] = useState(initial);
  const term = useDebounce(q.trim(), 250);
  const [results, setResults] = useState(null);
  useDocumentTitle(term ? `“${term}”` : 'Search');

  // Sync when the query changes from outside (e.g. the top bar search),
  // without clobbering trailing spaces while the user is typing here.
  useEffect(() => {
    const fromUrl = params.get('q') || '';
    setQ((current) => (current.trim() === fromUrl ? current : fromUrl));
  }, [params]);

  useEffect(() => {
    if (term !== (params.get('q') || '')) setParams(term ? { q: term } : {}, { replace: true });
    if (!term) { setResults(null); return undefined; }
    const ctrl = new AbortController();
    setResults(undefined);
    api(`/search?q=${encodeURIComponent(term)}`, { signal: ctrl.signal })
      .then(setResults)
      .catch((e) => { if (e.name !== 'AbortError') setResults({ businesses: [], dishes: [] }); });
    return () => ctrl.abort();
  }, [term]); // eslint-disable-line react-hooks/exhaustive-deps

  return (
    <div className="container page">
      <div className="search-hero">
        <SearchIcon size={22} />
        <input autoFocus value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search dishes, restaurants or cuisines" aria-label="Search" />
      </div>

      {results === undefined && <SkeletonGrid count={3} />}
      {results === null && <EmptyState icon={<SearchIcon size={34} />} title="Search Diet Crusher">Try “sushi”, “tacos” or “pizza”.</EmptyState>}
      {results && results.businesses.length === 0 && results.dishes.length === 0 && (
        <EmptyState icon={<SearchIcon size={34} />} title={`No results for “${term}”`}>Check the spelling or try something broader.</EmptyState>
      )}
      {results && results.businesses.length > 0 && (
        <section className="section">
          <div className="section-head"><h2>Restaurants</h2></div>
          <div className="card-grid">{results.businesses.map((b) => <RestaurantCard key={b.id} business={b} />)}</div>
        </section>
      )}
      {results && results.dishes.length > 0 && (
        <section className="section">
          <div className="section-head"><h2>Dishes</h2></div>
          <div className="menu-grid">{results.dishes.map((d) => <MenuItem key={d.id} dish={d} />)}</div>
        </section>
      )}
    </div>
  );
}
