import React, { useState } from 'react';
import fallback from '../../images/no-image.png';

/** Lazy image that swaps to a placeholder when a remote URL is broken. */
export default function Img({ src, alt = '', className = '', ...rest }) {
  const [failed, setFailed] = useState(false);
  return (
    <img
      src={!src || failed ? fallback : src}
      alt={alt}
      className={`${className} ${failed || !src ? 'img-fallback' : ''}`}
      loading="lazy"
      decoding="async"
      referrerPolicy="no-referrer"
      onError={() => setFailed(true)}
      {...rest}
    />
  );
}
