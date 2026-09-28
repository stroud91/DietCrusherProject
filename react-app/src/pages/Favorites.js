import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { loadFavorites } from '../store/favorites';
import { useDocumentTitle } from '../utils/hooks';
import RestaurantCard from '../components/RestaurantCard';
import { SkeletonGrid, EmptyState } from '../components/ui/States';
import { HeartIcon } from '../components/ui/Icons';

export default function Favorites() {
  useDocumentTitle('Favorites');
  const dispatch = useDispatch();
  const ids = useSelector((s) => s.favorites.ids);
  const [businesses, setBusinesses] = useState(null);

  useEffect(() => { dispatch(loadFavorites()).then(setBusinesses).catch(() => setBusinesses([])); }, [dispatch]);

  // Un-hearting a card removes it immediately without a refetch.
  const visible = businesses && businesses.filter((b) => ids.includes(b.id));

  return (
    <div className="container page">
      <header className="page-head"><h1>Favorites</h1></header>
      {!visible ? <SkeletonGrid count={3} /> : visible.length ? (
        <div className="card-grid">{visible.map((b) => <RestaurantCard key={b.id} business={b} />)}</div>
      ) : (
        <EmptyState icon={<HeartIcon size={34} />} title="No favorites yet" action="Discover restaurants" to="/all">
          Tap the heart on any restaurant to save it here.
        </EmptyState>
      )}
    </div>
  );
}
