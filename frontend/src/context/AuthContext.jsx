import React, { createContext, useState, useEffect } from 'react';
import authService from '../services/authService';
import userService from '../services/userService';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(() => localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initializeAuth = async () => {
      if (token) {
        try {
          // Fetch user profile to verify token validity
          const userData = await userService.getProfile();
          setUser(userData);
        } catch (error) {
          console.error("Token verification failed, logging out:", error);
          handleLogout();
        }
      }
      setLoading(false);
    };
    initializeAuth();
  }, [token]);

  const handleLogin = async (email, password) => {
    setLoading(true);
    try {
      const response = await authService.login(email, password);
      localStorage.setItem('token', response.token);
      setToken(response.token);
      setUser(response.user);
      return response;
    } catch (error) {
      setLoading(false);
      throw error;
    }
  };

  const handleRegister = async (name, email, password, phone, companyName) => {
    setLoading(true);
    try {
      const response = await authService.register({
        name,
        email,
        password,
        phone,
        companyName
      });
      localStorage.setItem('token', response.token);
      setToken(response.token);
      setUser(response.user);
      return response;
    } catch (error) {
      setLoading(false);
      throw error;
    }
  };

  const handleLogout = () => {
    authService.logout();
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  const handleUpdateProfile = async (profileData) => {
    try {
      const updatedUser = await userService.updateProfile(profileData);
      setUser(updatedUser);
      return updatedUser;
    } catch (error) {
      throw error;
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        loading,
        isAuthenticated: !!token,
        login: handleLogin,
        register: handleRegister,
        logout: handleLogout,
        updateProfile: handleUpdateProfile
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
