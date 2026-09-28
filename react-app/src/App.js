import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { Routes, Route, useLocation } from 'react-router-dom';
import { authenticate } from './store/session';
import Navigation from './components/layout/Navigation';
import TabBar from './components/layout/TabBar';
import Footer from './components/layout/Footer';
import CartDrawer from './components/layout/CartDrawer';
import ProtectedRoute from './components/layout/ProtectedRoute';
import { Spinner } from './components/ui/States';
import Home from './pages/Home';
import Browse from './pages/Browse';
import Search from './pages/Search';
import Restaurant from './pages/Restaurant';
import Dish from './pages/Dish';
import Checkout from './pages/Checkout';
import Orders from './pages/Orders';
import OrderDetail from './pages/OrderDetail';
import Account from './pages/Account';
import Favorites from './pages/Favorites';
import AuthPage from './pages/AuthPage';
import { OwnerDashboard, OwnerOrders } from './pages/Owner';
import BusinessForm from './pages/BusinessForm';
import DishForm from './pages/DishForm';
import NotFound from './pages/NotFound';

const guard = (el) => <ProtectedRoute>{el}</ProtectedRoute>;

function ScrollToTop() {
  const { pathname } = useLocation();
  useEffect(() => { window.scrollTo(0, 0); }, [pathname]);
  return null;
}

export default function App() {
  const dispatch = useDispatch();
  const [ready, setReady] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).finally(() => setReady(true));
  }, [dispatch]);

  return (
    <>
      <a href="#main" className="skip-link">Skip to content</a>
      <Navigation />
      <ScrollToTop />
      <main id="main">
        {!ready ? <Spinner /> : (
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/all" element={<Browse />} />
            <Route path="/search" element={<Search />} />
            <Route path="/business/:id" element={<Restaurant />} />
            <Route path="/dish/:id" element={<Dish />} />
            <Route path="/login" element={<AuthPage mode="login" />} />
            <Route path="/signup" element={<AuthPage mode="signup" />} />
            <Route path="/checkout" element={guard(<Checkout />)} />
            <Route path="/orders" element={guard(<Orders />)} />
            <Route path="/orders/:id" element={guard(<OrderDetail />)} />
            <Route path="/account" element={guard(<Account />)} />
            <Route path="/favorites" element={guard(<Favorites />)} />
            <Route path="/owned" element={guard(<OwnerDashboard />)} />
            <Route path="/owned/:id/orders" element={guard(<OwnerOrders />)} />
            <Route path="/create-business" element={guard(<BusinessForm />)} />
            <Route path="/update-business/:id" element={guard(<BusinessForm />)} />
            <Route path="/business/:businessId/create-dish" element={guard(<DishForm />)} />
            <Route path="/business/:businessId/update-dish/:id" element={guard(<DishForm />)} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        )}
      </main>
      <Footer />
      <TabBar />
      <CartDrawer />
    </>
  );
}
