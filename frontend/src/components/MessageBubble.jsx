function MessageBubble({ sender, text }) {
  const isUser = sender === "User";

  return (
    <div
      className={`message ${
        isUser ? "user" : "bot"
      }`}
    >
      <strong>{sender}</strong>
      <p>{text}</p>
    </div>
  );
}

export default MessageBubble;