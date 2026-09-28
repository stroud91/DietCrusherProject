import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import configureStore from './store';
import { ModalProvider } from './context/Modal';
import { ToastProvider } from './context/Toast';
import { applyTheme, getThemePreference } from './utils/theme';
import App from './App';
import './styles/index.css';

applyTheme(getThemePreference());
const store = configureStore();

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <ToastProvider>
          <ModalProvider>
            <App />
          </ModalProvider>
        </ToastProvider>
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
);
