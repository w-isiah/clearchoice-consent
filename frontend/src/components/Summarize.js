import React, { useState } from "react";
import { summarize } from "../api/api";

function Summarize() {
  const [userId] = useState("user123");
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");

  const handleSummarize = async () => {
    if (!text.trim()) return;
    try {
      const res = await summarize(userId, text);
      setSummary(res.summary);
    } catch (err) {
      console.error("Error summarizing:", err);
    }
  };

  return (
    <div className="card">
      <h2>📝 Summarize Consent Text</h2>
      <textarea
        className="chat-input"
        placeholder="Paste text to summarize..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button className="btn" onClick={handleSummarize}>Summarize</button>
      {summary && (
        <div className="chat-response">
          <h3>Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default Summarize;
