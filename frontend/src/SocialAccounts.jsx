import React, { useState } from "react";

export default function SocialAccounts() {
  const [showModal, setShowModal] = useState(false);
  const [platform, setPlatform] = useState("");
  const [accountName, setAccountName] = useState("");

  const [accounts, setAccounts] = useState([
    {
      platform: "Instagram",
      accountName: "@demo_user",
      status: "Connected",
    },
    {
      platform: "Facebook",
      accountName: "@demo_page",
      status: "Connected",
    },
  ]);

  const handleSave = () => {
    if (platform.trim() === "" || accountName.trim() === "") {
      alert("Please fill all fields!");
      return;
    }

    const newAccount = {
      platform,
      accountName,
      status: "Connected",
    };

    setAccounts([...accounts, newAccount]);

    setPlatform("");
    setAccountName("");
    setShowModal(false);

    alert("Account Connected Successfully!");
  };

  const handleDisconnect = (index) => {
    const updatedAccounts = accounts.filter((_, i) => i !== index);
    setAccounts(updatedAccounts);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">
        Social Account Management
      </h1>

      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold mb-4">
          Connected Social Accounts
        </h2>

        <table className="w-full border-collapse border">
          <thead>
            <tr className="bg-gray-200">
              <th className="border p-2">Platform</th>
              <th className="border p-2">Account Name</th>
              <th className="border p-2">Status</th>
              <th className="border p-2">Actions</th>
            </tr>
          </thead>

          <tbody>
            {accounts.map((account, index) => (
              <tr key={index}>
                <td className="border p-2">{account.platform}</td>
                <td className="border p-2">{account.accountName}</td>
                <td className="border p-2 text-green-600">
                  {account.status}
                </td>
                <td className="border p-2">
                  <button
                    onClick={() => handleDisconnect(index)}
                    className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded"
                  >
                    Disconnect
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        <button
          onClick={() => setShowModal(true)}
          className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          + Connect New Account
        </button>
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h2 className="text-xl font-bold mb-4">
              Connect New Account
            </h2>

            <input
              type="text"
              placeholder="Platform"
              value={platform}
              onChange={(e) => setPlatform(e.target.value)}
              className="w-full border p-2 mb-3 rounded"
            />

            <input
              type="text"
              placeholder="Account Name"
              value={accountName}
              onChange={(e) => setAccountName(e.target.value)}
              className="w-full border p-2 mb-4 rounded"
            />

            <div className="flex justify-end gap-2">
              <button
                onClick={() => {
                  setShowModal(false);
                  setPlatform("");
                  setAccountName("");
                }}
                className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded"
              >
                Cancel
              </button>

              <button
                onClick={handleSave}
                className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}