import React, { useState } from 'react';
import { useModal } from '../context/Modal';

export default function ConfirmDialog({ title, message, confirmLabel = 'Confirm', tone = 'danger', onConfirm }) {
  const { closeModal } = useModal();
  const [busy, setBusy] = useState(false);
  const [problem, setProblem] = useState('');

  const confirm = async () => {
    setBusy(true);
    try {
      await onConfirm();
      closeModal();
    } catch (e) {
      setProblem(e.message);
      setBusy(false);
    }
  };

  return (
    <div className="dialog">
      <h2>{title}</h2>
      <p className="muted">{message}</p>
      {problem && <p className="form-errors">{problem}</p>}
      <div className="dialog-actions">
        <button className="btn btn-secondary" onClick={closeModal} disabled={busy}>Cancel</button>
        <button className={`btn ${tone === 'danger' ? 'btn-danger' : 'btn-primary'}`} onClick={confirm} disabled={busy}>
          {busy ? 'Working…' : confirmLabel}
        </button>
      </div>
    </div>
  );
}
