import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { registerStudent } from "../services/authService";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    password: "",
    phone: "",
    jee_percentile: "",
    branch_preference: "",
  });

  const [error, setError] = useState("");

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");

    try {
      await registerStudent(formData);

      alert("Registration Successful!");
      navigate("/");
    } catch (err) {
      setError(
        err.response?.data?.detail || "Registration failed"
      );
    }
  }

  return (
    <div className="register-page">
      <div className="register-card">
        <h1>Welcome</h1>
        <h2>Student Registration</h2>
        <p>Create your account to continue</p>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="full_name"
            placeholder="Full Name"
            value={formData.full_name}
            onChange={handleChange}
            required
          />

          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="phone"
            placeholder="Phone Number"
            value={formData.phone}
            onChange={handleChange}
            required
          />

          <input
            type="number"
            name="jee_percentile"
            placeholder="JEE Percentile"
            value={formData.jee_percentile}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="branch_preference"
            placeholder="Preferred Branch"
            value={formData.branch_preference}
            onChange={handleChange}
            required
          />

          <button type="submit">Register</button>
        </form>

        {error && (
          <p style={{ color: "red", marginTop: "15px" }}>
            {error}
          </p>
        )}

        <Link to="/">Already have an account? Login</Link>
      </div>
    </div>
  );
}

export default Register;