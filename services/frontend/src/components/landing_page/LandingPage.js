import React from 'react'

import Box from '@mui/material/Box';
// import './LandingPage.css'

const LandingPage = ({ token }) => {

  return (
    <Box>
      Your token is: {token}
    </Box>
  )
}

export default LandingPage;