import React, { useState } from 'react';
import { api } from '../utils/api';
import { useModal } from '../context/Modal';
import { StarInput } from './ui/Rating';
import { ErrorList } from './ui/States';

export default function ReviewModal({ dish, review, onSaved }) {
  const { closeModal } = useModal();
  const [rating, setRating] = useState(review ? review.rating : 0);
  const [comment, setComment] = useState(review ? review.comment : '');
  const [errors, setErrors] = useState([]);
  const [busy, setBusy] = useState(false);
  const valid = rating >= 1 && comment.trim().length >= 10;

  const submit = async (e) => {
    e.preventDefault();
    setBusy(true);
    try {
      if (review) await api(`/review/${review.id}`, { method: 'PUT', body: { rating, comment } });
      else await api('/review/', { method: 'POST', body: { dish_id: dish.id, rating, comment } });
      closeModal();
      if (onSaved) onSaved();
    } catch (err) {
      setErrors(err.errors);
      setBusy(false);
    }
  };

  return (
    <form className="dialog" onSubmit={submit}>
      <h2>{review ? 'Edit your review' : 'How was it?'}</h2>
      <p className="muted">{dish.name}</p>
      <ErrorList errors={errors} />
      <StarInput value={rating} onChange={setRating} />
      <label className="field">
        <span>Your review</span>
        <textarea rows={4} maxLength={500} value={comment} onChange={(e) => setComment(e.target.value)}
          placeholder="What did you love? What could be better?" />
      </label>
      <p className="hint">{comment.trim().length < 10 ? `${10 - comment.trim().length} more characters` : `${500 - comment.length} characters left`}</p>
      <div className="dialog-actions">
        <button type="button" className="btn btn-secondary" onClick={closeModal}>Cancel</button>
        <button className="btn btn-primary" disabled={!valid || busy}>{busy ? 'Saving…' : review ? 'Save changes' : 'Post review'}</button>
      </div>
    </form>
  );
}
