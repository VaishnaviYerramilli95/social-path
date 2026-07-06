import React, { useState } from 'react';

export default function Scheduler() {
  const [showModal, setShowModal] = useState(false);

  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* Sidebar Placeholder */}
      <div className="w-64 bg-indigo-700 text-white p-5 hidden md:block">
        <h2 className="text-2xl font-bold mb-6">SocialPilot</h2>
        <p className="opacity-75">Scheduler Module (Week 1)</p>
      </div>

      {/* Main Content */}
      <div className="flex-1 p-8">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800">Content Calendar</h1>
          <button 
            onClick={() => setShowModal(true)}
            className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-lg shadow-md transition-all">
            + Schedule New Post
          </button>
        </div>

        {/* Calendar Grid Box Setup */}
        <div className="bg-white p-6 rounded-xl shadow-md min-h-[500px] flex items-center justify-center border border-gray-200">
          <div className="text-center">
            <p className="text-gray-500 text-lg font-medium mb-2">Interactive Calendar View Coming Soon</p>
            <p className="text-gray-400 text-sm">Week 2 integration will connect the backend pipelines here.</p>
          </div>
        </div>
      </div>

      {/* Create Post Modal Component */}
      {showModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50 animate-fade-in">
          <div className="bg-white rounded-xl shadow-2xl max-w-md w-full p-6 relative">
            <h3 className="text-xl font-bold text-gray-900 mb-4">Create & Schedule Post</h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Post Caption</label>
                <textarea className="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-indigo-500 outline-none" rows="3" placeholder="Write your content here..."></textarea>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Schedule Time</label>
                <input type="datetime-local" className="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-indigo-500 outline-none" />
              </div>
            </div>

            <div className="mt-6 flex justify-end space-x-3">
              <button onClick={() => setShowModal(false)} className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg transition-all">Cancel</button>
              <button onClick={() => { alert('Post drafted successfully!'); setShowModal(false); }} className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition-all">Save Draft</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}