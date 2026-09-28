import React, { useCallback, useContext, useEffect, useRef, useState } from 'react';
import ReactDOM from 'react-dom';
import { CloseIcon } from '../components/ui/Icons';

const ModalContext = React.createContext(null);

export function ModalProvider({ children }) {
  const [content, setContent] = useState(null);
  const onCloseRef = useRef(null);

  const closeModal = useCallback(() => {
    setContent(null);
    const cb = onCloseRef.current;
    onCloseRef.current = null;
    if (typeof cb === 'function') cb();
  }, []);

  const openModal = useCallback((node, onClose) => {
    onCloseRef.current = onClose || null;
    setContent(node);
  }, []);

  return (
    <ModalContext.Provider value={{ openModal, closeModal, isOpen: !!content }}>
      {children}
      {content && <ModalFrame onClose={closeModal}>{content}</ModalFrame>}
    </ModalContext.Provider>
  );
}

function ModalFrame({ children, onClose }) {
  const panel = useRef(null);

  useEffect(() => {
    const previous = document.activeElement;
    const onKey = (e) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('keydown', onKey);
    document.body.classList.add('no-scroll');
    const firstField = panel.current && panel.current.querySelector('input, textarea, select, button:not(.modal-close)');
    if (firstField) firstField.focus();
    return () => {
      document.removeEventListener('keydown', onKey);
      document.body.classList.remove('no-scroll');
      if (previous && previous.focus) previous.focus();
    };
  }, [onClose]);

  return ReactDOM.createPortal(
    <div className="modal-root">
      <div className="modal-backdrop" onClick={onClose} />
      <div className="modal-panel" role="dialog" aria-modal="true" ref={panel}>
        <button className="icon-btn modal-close" aria-label="Close" onClick={onClose}>
          <CloseIcon />
        </button>
        {children}
      </div>
    </div>,
    document.body
  );
}

export const useModal = () => useContext(ModalContext);
