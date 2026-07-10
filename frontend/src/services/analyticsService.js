import api from './api';

const MOCK_ANALYTICS = {
  overallSummary: {
    totalEngagement: { value: "328.4K", change: "+12.4%", trend: "up" },
    totalFollowers: { value: "84.9K", change: "+8.2%", trend: "up" },
    totalReach: { value: "1.2M", change: "+15.3%", trend: "up" },
    totalImpressions: { value: "2.4M", change: "+18.7%", trend: "up" },
    totalClicks: { value: "48.2K", change: "+5.1%", trend: "up" },
    roi: { value: "348%", change: "+24.0%", trend: "up" }
  },
  monthlyGrowth: [
    { name: 'Jan', followers: 12000, reach: 98000, clicks: 3100 },
    { name: 'Feb', followers: 15000, reach: 110000, clicks: 3500 },
    { name: 'Mar', followers: 21000, reach: 135000, clicks: 4200 },
    { name: 'Apr', followers: 28000, reach: 180000, clicks: 5100 },
    { name: 'May', followers: 36000, reach: 240000, clicks: 6800 },
    { name: 'Jun', followers: 48000, reach: 310000, clicks: 8200 },
    { name: 'Jul', followers: 52000, reach: 335000, clicks: 9100 }
  ],
  engagementTimeline: [
    { name: 'Mon', facebook: 2400, twitter: 1398, linkedin: 3200, instagram: 4800 },
    { name: 'Tue', facebook: 2210, twitter: 1221, linkedin: 3400, instagram: 4300 },
    { name: 'Wed', facebook: 3290, twitter: 2225, linkedin: 4100, instagram: 5100 },
    { name: 'Thu', facebook: 2000, twitter: 1780, linkedin: 2900, instagram: 3900 },
    { name: 'Fri', facebook: 3181, twitter: 2500, linkedin: 4500, instagram: 6200 },
    { name: 'Sat', facebook: 4000, twitter: 3100, linkedin: 3800, instagram: 7800 },
    { name: 'Sun', facebook: 3800, twitter: 2800, linkedin: 3100, instagram: 7100 }
  ],
  platformComparison: [
    { name: 'Facebook', value: 25, color: '#1877F2' },
    { name: 'Instagram', value: 38, color: '#E4405F' },
    { name: 'LinkedIn', value: 22, color: '#0A66C2' },
    { name: 'Twitter/X', value: 15, color: '#1DA1F2' }
  ],
  engagementRates: [
    { name: 'Facebook', rate: 3.2 },
    { name: 'Instagram', rate: 5.6 },
    { name: 'LinkedIn', rate: 4.8 },
    { name: 'Twitter/X', rate: 2.1 }
  ]
};

const analyticsService = {
  getAnalytics: async () => {
    try {
      const response = await api.get('/analytics');
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Using fallback analytics data");
      return MOCK_ANALYTICS;
    }
  }
};

export default analyticsService;
