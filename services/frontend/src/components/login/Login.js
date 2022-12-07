import React, { useState, useEffect, forwardRef } from 'react'

import { useLocation, useNavigate } from 'react-router-dom'

import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import MuiAlert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
// import LoginIcon from '@mui/icons-material/Login';
import IconButton from '@mui/material/IconButton';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';
import Visibility from '@mui/icons-material/Visibility';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputAdornment from '@mui/material/InputAdornment';
import FormHelperText from '@mui/material/FormHelperText';
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

  // password
  const [password, setPassword] = useState("")
  const [passwordError, setPasswordError] = useState(false)
  const [passwordErrorMsg, setPasswordErrorMsg] = useState("")
  const [showPassword, setShowPassword] = useState(false)

  // email
  const [email, setEmail] = useState("")
  const [emailError, setEmailError] = useState(false)
  const [emailErrorMsg, setEmailErrorMsg] = useState("")

  // snackbar alert
  const [snackbar, setSnackbar] = useState("")
  const Alert = forwardRef(function Alert(props, ref) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
  });
  
  
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

  function onSetPassword(val) {
    setPasswordError(false)
    setPasswordErrorMsg("")
    setPassword(val)
  }

  function onSetEmail(val) {
    setEmailError(false)
    setEmailErrorMsg("")
    setEmail(val)
  }

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
          if (res.detail) {
            setSnackbar(res.detail)
          }
          else {
            setToken(res.access_token)
          }
          console.log(res)
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
      `${process.env.REACT_APP_BACKEND_URL}/user`, {
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
        if (res.detail) {
          if (res.detail.includes("Password")) {
            setPasswordError(true)
            setPasswordErrorMsg(res.detail)
          }
          if (res.detail.includes("email") || res.detail.includes("user already exists")) {
            setEmailError(true)
            setEmailErrorMsg(res.detail)
          }
          console.log(res.detail)
        }
      })
  }

  return (
    <Box className='login-container'>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='margin'></Box>
      <Box className='login-box'>
        <Snackbar open={snackbar !== ""} autoHideDuration={3000} onClose={() => setSnackbar("")}>
          <Alert onClose={() => setSnackbar("")} severity="error" sx={{ width: '100%' }}>
              {snackbar}
          </Alert>
        </Snackbar>
        <Stack direction='column' spacing={1}>
          <Box sx={{textAlign: 'center'}}>
            <FormControl sx={{ m: 1, width: '95%' }} variant="outlined">
                <InputLabel>
                    Email
                </InputLabel>
                <OutlinedInput
                    type={'text'}
                    value={email}
                    onChange={(event) => onSetEmail(event.target.value)}
                    error={emailError}
                    label="Username"
                />
                {emailError && (
                  <FormHelperText error>
                    {emailErrorMsg}
                  </FormHelperText>
                )}
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
                onChange={(event) => onSetPassword(event.target.value)}
                error={passwordError}
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
              {passwordError && (
                <FormHelperText error>
                  {passwordErrorMsg}
                </FormHelperText>
              )}
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