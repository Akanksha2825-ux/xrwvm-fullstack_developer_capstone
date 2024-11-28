import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import axios from 'axios';
import Register from './components/Register'; // Ensure this path is correct for your project

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginStatus, setLoginStatus] = useState('');

  const handleLogin = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('/login', { username, password });
      if (response.data.status === 'success') {
        setLoginStatus(`Logged in as ${response.data.username}`);  // Corrected syntax here
      } else {
        setLoginStatus('Login failed: ' + response.data.message);
      }
    } catch (error) {
      setLoginStatus('Error: ' + error.message);
    }
  };

  return (
    <Router>
      <Routes>
        {/* Route for the login page */}
        <Route 
          path="/" 
          element={
            <div>
              <h2>Login</h2>
              <form onSubmit={handleLogin}>
                <input
                  type="text"
                  placeholder="Username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
                <input
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
                <button type="submit">Login</button>
              </form>
              {loginStatus && <p>{loginStatus}</p>}
            </div>
          } 
        />
        
        {/* Route for the Register component */}
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
