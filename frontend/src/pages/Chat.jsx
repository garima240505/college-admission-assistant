import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import { sendMessage } from "../services/chatbotService";
import {
  getCurrentStudent,
  logout,
} from "../services/authService";

function Chat() {
  const navigate = useNavigate();

  const [student, setStudent] = useState(null);
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([
    {
      sender: "Bot",
      text: "Hello! How can I help you today?",
    },
  ]);

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function loadStudent() {
      try {
        const data = await getCurrentStudent();
        setStudent(data);
      } catch (error) {
        logout();
        navigate("/");
      }
    }

    loadStudent();
  }, [navigate]);

  async function handleSend() {
    if (message.trim() === "") return;

    const question = message;

    setMessages((prev) => [
      ...prev,
      {
        sender: "User",
        text: question,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const answer = await sendMessage(question);

      setMessages((prev) => [
        ...prev,
        {
          sender: "Bot",
          text: answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "Bot",
          text: "Unable to connect to the server.",
        },
      ]);
    }

    setLoading(false);
  }

  function handleLogout() {
    logout();
    navigate("/");
  }

  return (
    <div className="app">
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h1>🎓 Admission Assistant</h1>

        <button onClick={handleLogout}>
          Logout
        </button>
      </div>

      {student && (
        <p>
          Welcome, <b>{student.full_name}</b>
        </p>
      )}

      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ChatInput
        message={message}
        setMessage={setMessage}
        handleSend={handleSend}
        loading={loading}
      />
    </div>
  );
}

export default Chat;