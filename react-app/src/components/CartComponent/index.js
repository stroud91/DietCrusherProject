import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllDishes } from '../../store/dish';

const Cart = ({ dishes }) => {

    const [cartItems, setCartItems] = useState([]);


    useEffect(() => {

        const savedCart = localStorage.getItem('cart');
        if (savedCart) {
            setCartItems(JSON.parse(savedCart));
        }
    }, []);

    useEffect(() => {
        localStorage.setItem('cart', JSON.stringify(cartItems));
    }, [cartItems]);

    const addToCart = (dish) => {
      console.log("this is dish", dish)
        const existingCartItem = cartItems.find(item => item.dish_id === dish.id);
        if (existingCartItem) {
            const updatedCartItems = cartItems.map(item =>
                item.dish_id === dish.id ? { ...item, quantity: item.quantity + 1 } : item
            );
            setCartItems(updatedCartItems);
        } else {
            const newCartItem = {
                id: Date.now(),
                dish_id: dish.id,
                dish_name: dish.name,
                quantity: 1,
                price: dish.price
            };
            setCartItems([...cartItems, newCartItem]);
        }

    };

    const updateQuantity = (dishId, amount) => {
        const updatedCartItems = cartItems.map(item =>
            item.dish_id === dishId ? { ...item, quantity: item.quantity + amount } : item
        ).filter(item => item.quantity > 0);
        setCartItems(updatedCartItems);
    };

    const getTotalPrice = () => {
        return cartItems.reduce((total, item) => total + (item.price * item.quantity), 0);
    }

    const handleSubmit = () => {
        setCartItems([]);
        localStorage.removeItem('cart');
    };

    return (
        <div>
            <div class="cart-container">
            <h2 class="cart-title">Cart</h2>
              <ul class="cart-items">
             {cartItems.map(item => (
            <li class="cart-item" key={item.id}>
                <span class="item-name">{item.dish_name}</span>
                <button class="item-decrease" onClick={() => updateQuantity(item.dish_id, -1)}>-</button>
                <span class="item-quantity">{item.quantity}</span>
                <button class="item-increase" onClick={() => updateQuantity(item.dish_id, 1)}>+</button>
                <span class="item-subtotal">- Subtotal: ${item.price * item.quantity}</span>
                <button class="item-remove" onClick={() => updateQuantity(item.dish_id, -item.quantity)}>Remove</button>
            </li>
               ))}
             </ul>
             <div class="cart-total">Total: ${getTotalPrice().toFixed(2)}</div>
             {cartItems && (
              <button class="submit-button" onClick={handleSubmit}>Submit Order</button>
             )}

           </div>
            <div>
                <h2>Select your items you want to add</h2>
                <ul>
                <div className="dish-container">
                    {dishes.map(dish => (
                        <li key={dish.id} className="dish-card">

                             <div class="product-item">
                              <img className="image-inside" src={dish.image_id} alt="Product Name" />
                            </div>
                             <div class="product-description">
                             <h2>{dish.name} - ${dish.price}</h2>
                              From: {dish.business_name} </div>
                            <button class="add-to-cart" onClick={() => addToCart(dish)}>Add to Cart</button>

                        </li>
                    ))}
                  </div>
                </ul>

            </div>
        </div>
    );
};

export default Cart;
