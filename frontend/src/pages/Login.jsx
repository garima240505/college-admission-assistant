import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { loginStudent, isLoggedIn } from "../services/authService";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isLoggedIn()) {
      navigate("/chat");
    }
  }, [navigate]);

  async function handleLogin(e) {
    e.preventDefault();

    setLoading(true);

    try {
      await loginStudent(email, password);

      navigate("/chat");
    } catch (err) {
      alert(
        err.response?.data?.detail ||
          "Invalid email or password."
      );
    }

    setLoading(false);
  }

  return (
    <div className="login-page">
      <div className="login-card">

        <h1>🎓</h1>

        <h2>AIT Admission Assistant</h2>

        <p>
          Login to continue
        </p>

        <form onSubmit={handleLogin}>

          <input
            type="email"
            placeholder="Email Address"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            required
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            required
          />

          <button
            type="submit"
            disabled={loading}
          >
            {loading ? "Logging in..." : "Login"}
          </button>

        </form>

        <Link to="/register">
          Create a new account
        </Link>

      </div>
    </div>
  );
}

export default Login;