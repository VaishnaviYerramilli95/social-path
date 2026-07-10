/* import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
*/

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import { AuthProvider } from './context/AuthContext'; // 1. Add this import

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* 2. Wrap App inside AuthProvider */}
    <AuthProvider>
      <App />
    </AuthProvider>
  </StrictMode>,
);