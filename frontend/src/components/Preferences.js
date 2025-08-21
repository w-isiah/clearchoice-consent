import React, { useState } from "react";
import { savePreference } from "../api/api";

function Preferences() {
  const [userId] = useState("user123");
  const [preference, setPreference] = useState("");
  const [status, setStatus] = useState("");

  const handleSave = async () => {
    if (!preference.trim()) return;
    await savePreference(userId, preference);
    setStatus("✅ Preference saved!");
  };

  return (
    <div>
      <h2>User Preferences</h2>
      <input
        type="text"
        value={preference}
        onChange={(e) => setPreference(e.target.value)}
        placeholder="Enter your preference..."
      />
      <button onClick={handleSave}>Save</button>
      {status && <p>{status}</p>}
    </div>
  );
}

export default Preferences;
