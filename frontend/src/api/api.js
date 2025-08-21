// frontend/src/api/api.js
import axios from "axios";

// Make sure this URL matches your backend
const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // FastAPI backend
});

export const summarize = async (userId, text) => {
  const res = await api.post("/summarize/", { user_id: userId, text });
  return res.data;
};

export const chat = async (userId, question) => {
  const res = await api.post("/chat/", { user_id: userId, question });
  return res.data;
};

export const savePreference = async (userId, preference) => {
  const res = await api.post("/preferences/", { user_id: userId, preference });
  return res.data;
};

export const getHistory = async (userId) => {
  const res = await api.get(`/history/?user_id=${userId}`);
  return res.data;
};

export default api;
