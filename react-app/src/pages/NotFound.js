import React from 'react';
import { EmptyState } from '../components/ui/States';
import { useDocumentTitle } from '../utils/hooks';

export default function NotFound() {
  useDocumentTitle('Not found');
  return (
    <div className="container page">
      <EmptyState title="This page went out for delivery" action="Take me home" to="/">
        We couldn't find what you were looking for.
      </EmptyState>
    </div>
  );
}
