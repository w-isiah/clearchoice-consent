import React, { useState } from "react";
import { chat } from "../api/api";

function Chat() {
  const [userId] = useState("user123");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleChat = async () => {
    if (!question.trim()) return;
    const res = await chat(userId, question);
    setAnswer(res.answer || "⚠️ No response from server");
  };

  return (
    <div>
      <h2>Chat Advisor</h2>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
      />
      <br />
      <button onClick={handleChat}>Ask</button>
      {answer && (
        <div>
          <h3>Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default Chat;
