import React, { useState, useEffect, useCallback } from "react";
import axios from "../api/api";

function History() {
  const userId = "user123"; // fixed user id
  const [history, setHistory] = useState([]);

  const fetchHistory = useCallback(async () => {
    try {
      const res = await axios.get(`/history/?user_id=${userId}`);
      setHistory(res.data.history);
    } catch (err) {
      console.error(err);
    }
  }, [userId]);

  const clearHistory = async () => {
    if (!window.confirm("Are you sure you want to clear your history?")) return;
    try {
      await axios.delete(`/history/clear?user_id=${userId}`);
      setHistory([]); // clear frontend
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, [fetchHistory]);

  return (
    <div className="history-container">
      <h2>Your History</h2>
      <button className="clear-btn" onClick={clearHistory}>
        Clear History
      </button>
      <ul>
        {history.length ? (
          history.map((item, idx) => (
            <li key={idx}>
              {item.action} -{" "}
              {new Date(item.created_at || item.timestamp).toLocaleString()}
            </li>
          ))
        ) : (
          <li>No history yet.</li>
        )}
      </ul>
    </div>
  );
}

export default History;
