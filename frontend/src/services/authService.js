import axios from "axios";

const API = "http://127.0.0.1:8000/students";

export async function registerStudent(studentData) {
  const response = await axios.post(
    `${API}/register`,
    studentData
  );

  return response.data;
}

export async function loginStudent(email, password) {
  const response = await axios.post(
    `${API}/login`,
    {
      email,
      password,
    }
  );

  localStorage.setItem(
    "access_token",
    response.data.access_token
  );

  return response.data;
}

export async function getCurrentStudent() {
  const token = localStorage.getItem("access_token");

  const response = await axios.get(
    `${API}/me`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
}

export async function updateProfile(profileData) {
  const token = localStorage.getItem("access_token");

  const response = await axios.put(
    `${API}/profile`,
    profileData,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
}

export function logout() {
  localStorage.removeItem("access_token");
}

export function isLoggedIn() {
  return localStorage.getItem("access_token") !== null;
}