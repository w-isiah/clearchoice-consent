import React, { useState } from "react";
import { getHistory } from "../api/api";

function History() {
  const [userId] = useState("user123");
  const [history, setHistory] = useState([]);

  const fetchHistory = async () => {
    const res = await getHistory(userId);
    setHistory(res.history || []);
  };

  return (
    <div>
      <h2>User History</h2>
      <button onClick={fetchHistory}>Load History</button>
      <ul>
        {history.length > 0 ? (
          history.map((h, i) => (
            <li key={i}>
              {h.timestamp}: {h.action}
            </li>
          ))
        ) : (
          <p>No history yet</p>
        )}
      </ul>
    </div>
  );
}

export default History;
