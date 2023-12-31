import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { useHistory } from "react-router-dom/";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const history = useHistory()

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
    }
  };

  const demoUser = async (e) => {
    e.preventDefault()
    let email = "alice@wonderland.ioo"
    let password = "passwordAlice"
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      history.push("/")
      closeModal()
    }
  }

  const handleOutsideClick = (e) => {
    if (e.target.className === 'modal-background') {
      closeModal();
    }
  };

  return (
    <div className="modal-background" onClick={handleOutsideClick}>
        <div className="modal-container">
            <h1 className="modal-title">Log In</h1>
            <form onSubmit={handleSubmit} className="modal-form">
                <ul className="error-messages">
                    {errors.map((error, idx) => (
                        <li key={idx}>{error}</li>
                    ))}
                </ul>
                <label>
                    Email
                    <input
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </label>
                <label>
                    Password
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </label>
                <button type="submit">Log In</button>
            </form>
            <button onClick={demoUser} className="btn-demo">
                Log In as Demo User
            </button>
        </div>
    </div>
);
}

export default LoginFormModal;
