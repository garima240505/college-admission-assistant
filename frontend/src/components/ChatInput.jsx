function ChatInput({
  message,
  setMessage,
  handleSend,
  loading,
}) {
  function handleKeyDown(e) {
    if (e.key === "Enter" && !loading) {
      handleSend();
    }
  }

  return (
    <div className="input-container">
      <input
        type="text"
        placeholder="Ask your question..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={handleKeyDown}
      />

      <button
        onClick={handleSend}
        disabled={loading}
      >
        {loading ? "Sending..." : "Send"}
      </button>
    </div>
  );
}

export default ChatInput;