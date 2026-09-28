import React, { useEffect, useMemo } from 'react';
import { useSearchParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { loadBusinesses } from '../store/business';
import { useDocumentTitle } from '../utils/hooks';
import RestaurantCard from '../components/RestaurantCard';
import { SkeletonGrid, EmptyState } from '../components/ui/States';
import { StoreIcon } from '../components/ui/Icons';

const SORTS = {
  recommended: { label: 'Recommended', fn: (a, b) => (b.rating || 0) * Math.log(2 + b.review_count) - (a.rating || 0) * Math.log(2 + a.review_count) },
  rating: { label: 'Highest rated', fn: (a, b) => (b.rating || 0) - (a.rating || 0) },
  fee: { label: 'Lowest delivery fee', fn: (a, b) => a.delivery_fee - b.delivery_fee },
  fastest: { label: 'Fastest', fn: (a, b) => a.prep_time - b.prep_time },
  name: { label: 'A–Z', fn: (a, b) => a.name.localeCompare(b.name) },
};

export default function Browse() {
  useDocumentTitle('Restaurants');
  const dispatch = useDispatch();
  const { list, loaded } = useSelector((s) => s.business);
  const [params, setParams] = useSearchParams();
  const cuisine = params.get('cuisine') || '';
  const sort = SORTS[params.get('sort')] ? params.get('sort') : 'recommended';
  const topOnly = params.get('top') === '1';

  useEffect(() => { dispatch(loadBusinesses()); }, [dispatch]);

  const update = (key, value) => {
    const next = new URLSearchParams(params);
    if (value) next.set(key, value); else next.delete(key);
    setParams(next, { replace: true });
  };

  const cuisines = useMemo(() => {
    const set = new Set();
    list.forEach((b) => b.cuisines.forEach((c) => set.add(c)));
    return [...set].sort();
  }, [list]);

  const results = useMemo(() => list
    .filter((b) => !cuisine || b.cuisines.includes(cuisine))
    .filter((b) => !topOnly || (b.rating || 0) >= 4.5)
    .sort(SORTS[sort].fn), [list, cuisine, topOnly, sort]);

  return (
    <div className="container page">
      <header className="page-head">
        <h1>{cuisine || 'All restaurants'}</h1>
        <p className="muted">{loaded ? `${results.length} places delivering to you` : 'Finding places near you…'}</p>
      </header>

      <div className="filters">
        <div className="chip-row">
          <button className={`chip ${!cuisine ? 'is-active' : ''}`} onClick={() => update('cuisine', '')}>All</button>
          {cuisines.map((c) => (
            <button key={c} className={`chip ${cuisine === c ? 'is-active' : ''}`} onClick={() => update('cuisine', c)}>{c}</button>
          ))}
        </div>
        <div className="filter-controls">
          <button className={`chip ${topOnly ? 'is-active' : ''}`} onClick={() => update('top', topOnly ? '' : '1')}>Rated 4.5+</button>
          <label className="select-wrap">
            <span className="sr-only">Sort by</span>
            <select value={sort} onChange={(e) => update('sort', e.target.value === 'recommended' ? '' : e.target.value)}>
              {Object.entries(SORTS).map(([key, s]) => <option key={key} value={key}>{s.label}</option>)}
            </select>
          </label>
        </div>
      </div>

      {!loaded ? <SkeletonGrid count={9} /> : results.length ? (
        <div className="card-grid">{results.map((b) => <RestaurantCard key={b.id} business={b} />)}</div>
      ) : (
        <EmptyState icon={<StoreIcon size={34} />} title="No matches">Try a different cuisine or clear your filters.</EmptyState>
      )}
    </div>
  );
}
