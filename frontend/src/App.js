import React from "react";
import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";
import Chat from "./components/Chat";
import Summarize from "./components/Summarize";
import Preferences from "./components/Preferences";
import History from "./components/History";
import "./App.css"; // Import global styles

// Navbar Component
function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-title">Consent Guardian</div>
      <div className="navbar-links">
        <NavLink to="/chat" className={({ isActive }) => (isActive ? "active-link" : "")}>
          Chat
        </NavLink>
        <NavLink to="/summarize" className={({ isActive }) => (isActive ? "active-link" : "")}>
          Summarize
        </NavLink>
        <NavLink to="/preferences" className={({ isActive }) => (isActive ? "active-link" : "")}>
          Preferences
        </NavLink>
        <NavLink to="/history" className={({ isActive }) => (isActive ? "active-link" : "")}>
          History
        </NavLink>
      </div>
    </nav>
  );
}

// App Component
function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Top Navigation */}
        <Navbar />

        {/* Main Content */}
        <main className="container">
          <Routes>
            <Route path="/" element={<Chat />} />
            <Route path="/chat" element={<Chat />} />
            <Route path="/summarize" element={<Summarize />} />
            <Route path="/preferences" element={<Preferences />} />
            <Route path="/history" element={<History />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
