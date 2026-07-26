import api from './api';

const socialAccountService = {
  getAccounts: async () => {
    try {
      const response = await api.get('/social-accounts');
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Fallback social accounts");
      return [
        { id: '1', platform: 'facebook', account_name: '@SocialPilotDev', status: 'Connected' },
        { id: '2', platform: 'instagram', account_name: 'socialpilot_dev', status: 'Connected' },
        { id: '3', platform: 'linkedin', account_name: 'SocialPilot Inc', status: 'Connected' },
        { id: '4', platform: 'twitter', account_name: '@SocialPilotHQ', status: 'Connected' }
      ];
    }
  }
};

export default socialAccountService;
