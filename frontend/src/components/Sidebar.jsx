function Sidebar({ clearChat }) {
  return (
    <div className="sidebar">

      <button
        className="new-chat-btn"
        onClick={clearChat}
      >
        + New Chat
      </button>

      <h3>Recent Chats</h3>

      <div className="chat-item">
        Admission Process
      </div>

      <div className="chat-item">
        Hostel Fees
      </div>

      <div className="chat-item">
        Documents Required
      </div>

    </div>
  );
}

export default Sidebar;