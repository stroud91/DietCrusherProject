import React from 'react';
import { MinusIcon, PlusIcon, TrashIcon } from './Icons';

export default function Stepper({ value, onChange, min = 1, max = 25, removable = false, size = 'md' }) {
  const atMin = value <= min;
  return (
    <div className={`stepper stepper-${size}`}>
      <button type="button" aria-label={removable && atMin ? 'Remove item' : 'Decrease quantity'}
        onClick={() => onChange(value - 1)} disabled={atMin && !removable}>
        {removable && atMin ? <TrashIcon size={16} /> : <MinusIcon size={16} />}
      </button>
      <span aria-live="polite">{value}</span>
      <button type="button" aria-label="Increase quantity" onClick={() => onChange(value + 1)} disabled={value >= max}>
        <PlusIcon size={16} />
      </button>
    </div>
  );
}
