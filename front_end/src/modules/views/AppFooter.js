import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Link from '@mui/material/Link';
import Container from '@mui/material/Container';
import Typography from '../components/Typography';

function Copyright() {
  return (
    <React.Fragment>
      {'© '}
      <Link color="inherit" href="https://liam-bong.onrender.com/">
        My Portfolio
      </Link>{' '}
      {new Date().getFullYear()}
    </React.Fragment>
  );
}

const iconStyle = {
  width: 38,
  height: 38,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundColor: 'secondary.main',
  mr: 1,
  '&:hover': {
    bgcolor: 'secondary.dark',
  },
};

export default function AppFooter() {
  return (
    <Typography
      component="footer"
      sx={{ display: 'flex', bgcolor: 'secondary.light' }}
    >
      <Container sx={{ my: 8, display: 'flex' }}>
        <Grid container spacing={5}>
          <Grid item xs={6} sm={4} md={3}>
            <Grid
              container
              direction="column"
              justifyContent="flex-end"
              spacing={2}
              sx={{ height: 50 }}
            >
              <Grid item sx={{ display: 'flex' }}>
                <Box component="a" href="https://github.com/lbong123" sx={iconStyle}>
                  <img
                    src="https://cdn-icons-png.flaticon.com/512/25/25231.png"
                    alt="github"
                    height="38px"
                    width="38px"
                  />
                </Box>
                <Box component="a" href="https://www.linkedin.com/in/liam-bong-602997235/" sx={iconStyle}>
                  <img
                    src="https://cdn-icons-png.flaticon.com/512/61/61109.png"
                    alt="linkedin"
                    height="38px"
                    width="38px"
                  />
                </Box>
              </Grid>
              <Grid item>
                <Copyright />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Container>
    </Typography>
  );
}
