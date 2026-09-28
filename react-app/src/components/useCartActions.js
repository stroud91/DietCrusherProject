import React, { useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addToCart, openCart } from '../store/cart';
import { useModal } from '../context/Modal';
import { useToast } from '../context/Toast';
import ConfirmDialog from './ConfirmDialog';
import { AuthModal } from './AuthForms';

/** Add-to-cart with login prompt and the "start a new cart?" confirmation. */
export default function useCartActions() {
  const dispatch = useDispatch();
  const user = useSelector((s) => s.session.user);
  const { openModal, closeModal } = useModal();
  const toast = useToast();

  return useCallback(async (dish, quantity = 1) => {
    if (!user) {
      openModal(<AuthModal onDone={closeModal} />);
      return;
    }
    try {
      await dispatch(addToCart(dish.id, quantity));
      toast(`Added ${quantity > 1 ? `${quantity} × ` : ''}${dish.name}`);
    } catch (e) {
      if (e.data && e.data.code === 'DIFFERENT_BUSINESS') {
        openModal(
          <ConfirmDialog
            title="Start a new cart?"
            message={`Your cart has items from ${e.data.business_name}. Start a new cart with ${dish.business_name || 'this restaurant'} instead?`}
            confirmLabel="New cart"
            tone="primary"
            onConfirm={async () => {
              await dispatch(addToCart(dish.id, quantity, true));
              toast(`Added ${dish.name}`);
              dispatch(openCart(true));
            }}
          />
        );
      } else {
        toast(e.message, 'error');
      }
    }
  }, [user, dispatch, openModal, closeModal, toast]);
}
