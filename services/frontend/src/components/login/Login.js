import React, { useState, useEffect } from 'react'

import { useLocation, useNavigate } from 'react-router-dom'

import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
// import LoginIcon from '@mui/icons-material/Login';
import IconButton from '@mui/material/IconButton';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';
import Visibility from '@mui/icons-material/Visibility';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputAdornment from '@mui/material/InputAdornment';
import VisibilityOff from '@mui/icons-material/VisibilityOff';

import './Login.css'

const GoogleIcon = () => {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18">
      <path d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18Z" fill="#4285F4"/>
      <path d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17Z" fill="#34A853"/>
      <path d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07Z" fill="#FBBC05"/>
      <path d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3Z" fill="#EA4335"/>
    </svg>
  )
}

const Login = ({ setToken }) => {
  const location = useLocation()
  const navigator = useNavigate()
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const [showPassword, setShowPassword] = useState(false)
  
  // TODO: fix it
  useEffect(() => {
    let hash = window.location.hash
    let params = hash.slice(1,).split("&")
    for (let i = 0; i < params.length; i++) {
      let param = params[i].split("=")
      if (param[0] === "access_token") {
        setToken(param[1])
        navigator(`/`)
      }
    }

  },[location])

  function validatePassword() {
    return true
  }

  function validateEmail() {
    return true
  }

  function onLogin() {
    if (!validateEmail() || !validatePassword()) {
      return
    }

    let params = new URLSearchParams()
    params.append("username", email);
    params.append("password", password);

    fetch(
      `${process.env.REACT_APP_BACKEND_URL}/token`, {
          method: "POST",
          body: params
      }
      ).then(response => {
          return response.json()
      }).then(res => {
          setToken(res.access_token)
      })
  }

  function onLoginWithGoogle() {
    window.location.href =`https://${process.env.REACT_APP_AUTH0_DOMAIN}/authorize?response_type=token&scope=openid%20profile%20email&audience=${process.env.REACT_APP_AUTH0_API_DEFAULT_AUDIENCE}&client_id=OMRVnZSFCuvHe3PVRBykkQYqxXoul6Cn&redirect_uri=${window.location.origin}/login/callback&connection=google-oauth2`;
  }

  function onSignUp() {
    if (!validateEmail() || !validatePassword()) {
      return
    }

    let params = new URLSearchParams()
    params.append("username", email);
    params.append("password", password);

    fetch(
      `${process.env.REACT_APP_BACKEND_URL}/token`, {
          method: "POST",
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: email,
            password: password,
            name: email
          }),
      }
      ).then(response => {
          return response.json()
      }).then(res => {
          console.log(res)
      })
  }

  return (
    <Box className='login-container'>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='login-box'>
      <Stack direction='column' spacing={1}>
        <Box sx={{textAlign: 'center'}}>
            <FormControl sx={{ m: 1, width: '95%' }} variant="outlined">
                <InputLabel>
                    Email
                </InputLabel>
                <OutlinedInput
                    type={'text'}
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                    label="Username"
                />
            </FormControl>
        </Box>

        <Box sx={{textAlign: 'center'}}>
          <FormControl sx={{ m: 1, width: '95%' }} variant="outlined">
            <InputLabel>
                Password
            </InputLabel>
              <OutlinedInput
                type={showPassword ? 'text' : 'password'}
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={() => setShowPassword(!showPassword)}
                      onMouseDown={(event) => event.preventDefault()}
                      edge="end"
                    >
                      {showPassword ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                }
                label="Password"
              />
            </FormControl>
          </Box>

          <Box sx={{textAlign: 'center'}}>
            <Button  
                sx={{
                    backgroundColor: "#313131", 
                '&:hover': {
                    backgroundColor: '#1f1f1f',
                  }
                }}
                variant="contained" 
                // endIcon={<LoginIcon />}
                onClick={() => onLogin()}
            >
                Login
            </Button>
          </Box>

          <Box className='or'>
            OR
          </Box>

          <Box sx={{textAlign: 'center'}}>
            <Button  
              sx={{
                  backgroundColor: "#313131", 
              '&:hover': {
                  backgroundColor: '#1f1f1f',
                }
              }}
              variant="contained"
              startIcon={<GoogleIcon />}
              onClick={() => onLoginWithGoogle()}
            >
              Continue With Google
            </Button>
          </Box>

          <Box className='or'>
            OR
          </Box>

          <Box sx={{textAlign: 'center'}}>
            <Button  
                sx={{
                    backgroundColor: "#313131", 
                '&:hover': {
                    backgroundColor: '#1f1f1f',
                  }
                }}
                variant="contained" 
                onClick={() => onSignUp()}
            >
                Sign Up
            </Button>
          </Box>
          
        </Stack>
      </Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
    </Box>
  )
}

export default Login;