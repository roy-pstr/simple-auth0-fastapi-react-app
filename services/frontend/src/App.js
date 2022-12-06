import React, { useState } from 'react'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import './App.css'
import Login from './components/login/Login'
import LandingPage from './components/landing_page/LandingPage'

const App = () => {

  const [token, setToken] = useState(null);

  return (
    <Router>
      {token
      ?
          <Routes>
            <Route 
              path='/' 
              element={
                <LandingPage 
                  token={token}
                />
              } 
            />
            {/* <Route 
              path='/login' 
              element={
                <Login 
                  setToken={setToken} 
                />
              } 
            /> */}
          </Routes>
      :
        <>
          <Login 
              setToken={setToken} 
            />
        </>
      }
    </Router>
  )
}

export default App;
