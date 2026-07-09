import React, {useState} from "react";

export default function SocialAccounts() {
    const [showModal, setShowModal] = useState(false);
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">
        Social Account Management
      </h1>

      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold mb-4">
          Connected Social Accounts
        </h2>

        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-200">
              <th className="border p-2">Platform</th>
              <th className="border p-2">Account Name</th>
              <th className="border p-2">Status</th>
              <th className="border p-2">Actions</th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td className="border p-2">Instagram</td>
              <td className="border p-2">@demo_user</td>
              <td className="border p-2 text-green-600">Connected</td>
              <td className="border p-2">
                <button className="bg-red-500 text-white px-3 py-1 rounded">
                  Disconnect
                </button>
              </td>
            </tr>

            <tr>
              <td className="border p-2">Facebook</td>
              <td className="border p-2">@demo_page</td>
              <td className="border p-2 text-green-600">Connected</td>
              <td className="border p-2">
                <button className="bg-red-500 text-white px-3 py-1 rounded">
                  Disconnect
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        <button 
            onClick={() => setShowModal(true)}
            className="mt-6 bg-blue-600 text-white px-4 py-2 rounded"
          >
            + Connect New Account
          </button>
      </div>
    </div>
  );
}