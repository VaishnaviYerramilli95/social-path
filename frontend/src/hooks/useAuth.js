import { useContext } from 'react';
//import { AuthContext } from '../context/ThemeContext'; // Wait, it should import from AuthContext, let's fix the path in CodeContent
// Ah, let's use ../context/AuthContext!
import { AuthContext } from "../context/AuthContext";
import { AuthContext as AuthContextType } from '../context/AuthContext';

export const useAuth = () => {
  const context = useContext(AuthContextType);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
