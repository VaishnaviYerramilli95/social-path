import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/campaigns/";

function Campaigns() {
  const [campaigns, setCampaigns] = useState([]);
  const [message, setMessage] = useState("");

  const [formData, setFormData] = useState({
    name: "",
    description: "",
    platform: "",
    start_date: "",
    end_date: "",
    budget: "",
    objective: "",
  });

  const fetchCampaigns = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();

      setCampaigns(data);
    } catch (error) {
      setMessage("Unable to load campaigns");
    }
  };

  useEffect(() => {
    fetchCampaigns();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((previousData) => ({
      ...previousData,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMessage("");

    const campaignData = {
      ...formData,
      budget: formData.budget
        ? Number(formData.budget)
        : null,
      user_id: "550e8400-e29b-41d4-a716-446655440000",
    };

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(campaignData),
      });

      if (!response.ok) {
        const errorData = await response.json();

        console.error(errorData);
        setMessage("Campaign creation failed");

        return;
      }

      setMessage("Campaign created successfully");

      setFormData({
        name: "",
        description: "",
        platform: "",
        start_date: "",
        end_date: "",
        budget: "",
        objective: "",
      });

      await fetchCampaigns();
    } catch (error) {
      setMessage("Unable to connect to Campaign API");
    }
  };

  return (
    <div>
      <h1>Campaign Management</h1>

      <p>{message}</p>

      <h2>Create Campaign</h2>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Campaign Name</label>
          <br />

          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <label>Description</label>
          <br />

          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
          />
        </div>

        <br />

        <div>
          <label>Platform</label>
          <br />

          <select
            name="platform"
            value={formData.platform}
            onChange={handleChange}
            required
          >
            <option value="">Select Platform</option>
            <option value="Facebook">Facebook</option>
            <option value="Instagram">Instagram</option>
            <option value="LinkedIn">LinkedIn</option>
            <option value="X">X (Twitter)</option>
            <option value="YouTube">YouTube</option>
            <option value="Pinterest">Pinterest</option>
          </select>
        </div>

        <br />

        <div>
          <label>Start Date</label>
          <br />

          <input
            type="date"
            name="start_date"
            value={formData.start_date}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <label>End Date</label>
          <br />

          <input
            type="date"
            name="end_date"
            value={formData.end_date}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <label>Budget</label>
          <br />

          <input
            type="number"
            name="budget"
            min="0"
            value={formData.budget}
            onChange={handleChange}
          />
        </div>

        <br />

        <div>
          <label>Objective</label>
          <br />

          <textarea
            name="objective"
            value={formData.objective}
            onChange={handleChange}
          />
        </div>

        <br />

        <button type="submit">
          Create Campaign
        </button>
      </form>

      <hr />

      <h2>Campaigns</h2>

      {campaigns.length === 0 ? (
        <p>No campaigns created yet.</p>
      ) : (
        campaigns.map((campaign) => (
          <div key={campaign.id}>
            <h3>{campaign.name}</h3>

            <p>Platform: {campaign.platform}</p>

            <p>
              Duration: {campaign.start_date} to{" "}
              {campaign.end_date}
            </p>

            <p>Budget: ₹{campaign.budget}</p>

            <p>Objective: {campaign.objective}</p>

            <p>Status: {campaign.status}</p>

            <hr />
          </div>
        ))
      )}
    </div>
  );
}

export default Campaigns;