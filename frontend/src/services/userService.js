import api from './api';

const DEFAULT_USER = {
  id: "usr_100",
  name: "Jane Doe",
  email: "jane@example.com",
  phone: "+1 555-019-2834",
  companyName: "SocialPilot Corp",
  avatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
};

const getLocalStorageUser = () => {
  const data = localStorage.getItem('socialpilot_user');
  if (!data) {
    localStorage.setItem('socialpilot_user', JSON.stringify(DEFAULT_USER));
    return DEFAULT_USER;
  }
  return JSON.parse(data);
};

const saveLocalStorageUser = (user) => {
  localStorage.setItem('socialpilot_user', JSON.stringify(user));
};

const userService = {
  getProfile: async () => {
    try {
      const response = await api.get('/profile');
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Using fallback localStorage user profile");
      return getLocalStorageUser();
    }
  },

  updateProfile: async (userData) => {
    try {
      const response = await api.put('/profile', userData);
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Updating user profile in localStorage");
      const currentUser = getLocalStorageUser();
      const updatedUser = {
        ...currentUser,
        ...userData
      };
      saveLocalStorageUser(updatedUser);
      return updatedUser;
    }
  }
};

export default userService;
