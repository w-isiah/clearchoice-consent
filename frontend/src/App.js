import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Summarize from "./components/Summarize";
import Chat from "./components/Chat";
import Preferences from "./components/Preferences";
import History from "./components/History";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/summarize">Summarize</Link> | 
        <Link to="/chat">Chat</Link> | 
        <Link to="/preferences">Preferences</Link> | 
        <Link to="/history">History</Link>
      </nav>
      <Routes>
        <Route path="/summarize" element={<Summarize />} />
        <Route path="/chat" element={<Chat />} />
        <Route path="/preferences" element={<Preferences />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </Router>
  );
}

export default App;
