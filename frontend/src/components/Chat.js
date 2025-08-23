// src/components/Chat.js
import React, { useState, useRef, useEffect } from "react";
import axios from "../api/api"; // ensure axios baseURL is configured
import "./Chat.css"; // import chat-specific styles

function Chat() {
  const [userId] = useState("user123"); // demo user
  const [messages, setMessages] = useState([
    { role: "system", content: "Welcome to Consent Guardian!" },
  ]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

  // Scroll to bottom when messages update
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // Send user message
  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);
    setInput("");

    try {
      const res = await axios.post("/chat/", {
        user_id: userId,
        question: input,
      });

      setMessages((prev) => [
        ...newMessages,
        { role: "assistant", content: res.data.answer },
      ]);
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...newMessages,
        { role: "assistant", content: "Error: Unable to fetch response." },
      ]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-window">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={msg.role === "user" ? "chat-user" : "chat-assistant"}
          >
            {msg.content}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="chat-input">
        <input
          type="text"
          value={input}
          placeholder="Type your message..."
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default Chat;
