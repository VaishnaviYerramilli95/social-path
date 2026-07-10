import api from './api';

const DEFAULT_CAMPAIGNS = [
  {
    id: "cmp_1",
    name: "Summer Product Launch 2026",
    description: "Multi-channel launch campaign for the new v4 cloud integration product lines.",
    status: "active",
    budget: 15000,
    spent: 4500,
    startDate: "2026-06-01",
    endDate: "2026-08-31",
    platforms: ["facebook", "twitter", "linkedin", "instagram"],
    postsCount: 24
  },
  {
    id: "cmp_2",
    name: "Q3 Holiday Sale Promo",
    description: "Targeted discounts and visual posts highlighting product deals for Independence Day.",
    status: "draft",
    budget: 8000,
    spent: 0,
    startDate: "2026-07-01",
    endDate: "2026-07-15",
    platforms: ["facebook", "instagram"],
    postsCount: 12
  },
  {
    id: "cmp_3",
    name: "Developer Conference Drive",
    description: "Sponsoring engineering posts, dev-to posts, and speaker updates.",
    status: "completed",
    budget: 5000,
    spent: 5000,
    startDate: "2026-05-10",
    endDate: "2026-06-15",
    platforms: ["linkedin", "twitter"],
    postsCount: 18
  },
  {
    id: "cmp_4",
    name: "Brand Re-engagement Ad Set",
    description: "Follower growth and brand sentiment optimization.",
    status: "paused",
    budget: 12000,
    spent: 6000,
    startDate: "2026-06-15",
    endDate: "2026-09-30",
    platforms: ["facebook", "twitter", "linkedin"],
    postsCount: 8
  }
];

const getLocalStorageCampaigns = () => {
  const data = localStorage.getItem('socialpilot_campaigns');
  if (!data) {
    localStorage.setItem('socialpilot_campaigns', JSON.stringify(DEFAULT_CAMPAIGNS));
    return DEFAULT_CAMPAIGNS;
  }
  return JSON.parse(data);
};

const saveLocalStorageCampaigns = (campaigns) => {
  localStorage.setItem('socialpilot_campaigns', JSON.stringify(campaigns));
};

const campaignService = {
  getCampaigns: async () => {
    try {
      const response = await api.get('/campaigns');
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Using fallback localStorage campaigns");
      return getLocalStorageCampaigns();
    }
  },

  createCampaign: async (campaignData) => {
    try {
      const response = await api.post('/campaigns', campaignData);
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Creating campaign in localStorage");
      const campaigns = getLocalStorageCampaigns();
      const newCampaign = {
        ...campaignData,
        id: `cmp_${Date.now()}`,
        spent: 0,
        postsCount: 0
      };
      campaigns.unshift(newCampaign);
      saveLocalStorageCampaigns(campaigns);
      return newCampaign;
    }
  },

  updateCampaign: async (id, campaignData) => {
    try {
      const response = await api.put(`/campaigns/${id}`, campaignData);
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Updating campaign in localStorage");
      const campaigns = getLocalStorageCampaigns();
      const index = campaigns.findIndex(c => c.id === id);
      if (index === -1) throw new Error("Campaign not found");
      
      const updatedCampaign = {
        ...campaigns[index],
        ...campaignData
      };
      campaigns[index] = updatedCampaign;
      saveLocalStorageCampaigns(campaigns);
      return updatedCampaign;
    }
  },

  deleteCampaign: async (id) => {
    try {
      const response = await api.delete(`/campaigns/${id}`);
      return response.data;
    } catch (error) {
      console.warn("[API MOCK] Deleting campaign from localStorage");
      let campaigns = getLocalStorageCampaigns();
      campaigns = campaigns.filter(c => c.id !== id);
      saveLocalStorageCampaigns(campaigns);
      return { success: true, message: "Campaign deleted successfully" };
    }
  }
};

export default campaignService;
