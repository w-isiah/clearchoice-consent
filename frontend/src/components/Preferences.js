import React, { useState } from "react";
import { savePreference } from "../api/api";

function Preferences() {
  const [userId] = useState("user123");
  const [preference, setPreference] = useState("");
  const [message, setMessage] = useState("");

  const handleSave = async () => {
    if (!preference.trim()) return;
    try {
      await savePreference(userId, preference);
      setMessage("✅ Preference saved successfully!");
      setPreference("");
    } catch (err) {
      console.error("Error saving preference:", err);
    }
  };

  return (
    <div className="card">
      <h2>⚙️ Manage Preferences</h2>
      <input
        className="input-field"
        type="text"
        placeholder="Enter preference"
        value={preference}
        onChange={(e) => setPreference(e.target.value)}
      />
      <button className="btn" onClick={handleSave}>Save</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Preferences;
