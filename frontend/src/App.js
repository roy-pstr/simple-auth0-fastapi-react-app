
import logo from './logo.svg';
import './App.css';
import React from 'react';

function App() {
  return (
    <div className="App">
      <form>
        <input type="text" id="login-email" placeholder="email"></input>
        <input type="password" id="login-password" placeholder="password"></input>
      </form> 
      <button onClick={() => {
        const payload = new URLSearchParams();
        payload.append("username", document.getElementById("login-email").value);
        payload.append("password", document.getElementById("login-password").value);

        fetch(`${process.env.REACT_APP_BACKEND_URL}/token`, {
          method: 'POST',
          body: payload
        })
          .then(response => response.json())
          .then(data => {
            if (data.access_token) {
              alert("Login Successful")
            } else {
              alert("Login Failed")
            }
          });
      }}>Login</button>

      <button onClick={() => {
        window.location.href =`https://${process.env.REACT_APP_AUTH0_DOMAIN}/authorize?response_type=token&scope=openid%20profile%20email&audience=${process.env.REACT_APP_AUTH0_API_DEFAULT_AUDIENCE}&client_id=OMRVnZSFCuvHe3PVRBykkQYqxXoul6Cn&redirect_uri=${window.location.origin}/login/callback&connection=google-oauth2`;
      }}>Continue with Google</button>
    
      <button onClick={() => {
        fetch(`${process.env.REACT_APP_BACKEND_URL}/user`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: document.getElementById("login-email").value,
            password: document.getElementById("login-password").value,
            name: document.getElementById("login-email").value
          }),
        })
          .then(response => response.json())
          .then(data => {
            console.log(data);
          });
      }}>Sign Up</button>
    </div>
  );
}

export default App;
