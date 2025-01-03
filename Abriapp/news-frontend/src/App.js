import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import Home from './components/Home';
import AdminPanel from './components/AdminPanel';
import ProtectedRoute from './components/ProtectedRoute';
import NewsDetail from './components/NewsDetail';
// ... other imports

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/admin"
          element={
            <ProtectedRoute roles={['ADMIN', 'SUPER_USER']}>
              <AdminPanel />
            </ProtectedRoute>
          }
        />
        <Route path="/news/:id" element={<NewsDetail />} />
        {/* ... other routes */}
      </Routes>
    </Router>
  );
}

export default App;
