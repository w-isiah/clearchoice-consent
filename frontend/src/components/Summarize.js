import React, { useState } from "react";
import { summarize } from "../api/api";

function Summarize() {
  const [userId] = useState("user123");
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");

  const handleSummarize = async () => {
    if (!text.trim()) return;
    const res = await summarize(userId, text);
    setSummary(res.summary || "⚠️ No summary returned");
  };

  return (
    <div>
      <h2>Summarize Text</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text to summarize..."
      />
      <br />
      <button onClick={handleSummarize}>Summarize</button>
      {summary && (
        <div>
          <h3>Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default Summarize;
