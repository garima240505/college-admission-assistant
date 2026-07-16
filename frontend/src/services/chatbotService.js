import axios from "axios";

const API_URL = "http://127.0.0.1:8000/chat/";

export async function sendMessage(question) {
  const token = localStorage.getItem("access_token");

  const response = await axios.post(
    API_URL,
    {
      question,
    },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data.answer;
}