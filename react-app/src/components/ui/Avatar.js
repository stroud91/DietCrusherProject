import React, { useState } from 'react';

/** Profile photo that falls back to initials when the image URL is broken. */
export default function Avatar({ src, name = '', size = 40, className = '' }) {
  const [failed, setFailed] = useState(false);
  const initials = name.split(/[\s_.-]+/).filter(Boolean).slice(0, 2).map((p) => p[0].toUpperCase()).join('') || '?';
  const style = { width: size, height: size, fontSize: size * 0.4 };
  if (!src || failed) return <span className={`avatar avatar-initials ${className}`} style={style} aria-hidden="true">{initials}</span>;
  return <img className={`avatar ${className}`} style={style} src={src} alt="" referrerPolicy="no-referrer" onError={() => setFailed(true)} />;
}
