import * as React from 'react';
import { Link } from 'react-router-dom';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import Button from '../components/Button';
import Typography from '../components/Typography';
import CurvyLines from '../../images/productCurvyLines.png';
import KeyboardHideOutlinedIcon from '@mui/icons-material/KeyboardHideOutlined';
import AutorenewOutlinedIcon from '@mui/icons-material/AutorenewOutlined';
import AssignmentOutlinedIcon from '@mui/icons-material/AssignmentOutlined';

const item = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    px: 5,
};

const number = {
    fontSize: 24,
    fontFamily: 'default',
    color: 'secondary.main',
    fontWeight: 'medium',
};

function ProductHowItWorks() {
    return (
        <Box
            component="section"
            sx={{
                display: 'flex',
                bgcolor: 'secondary.light',
                overflow: 'hidden',
            }}
        >
            <Container
                sx={{
                    mt: 10,
                    mb: 15,
                    position: 'relative',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Box
                    component="img"
                    src={CurvyLines}
                    alt="curvy lines"
                    sx={{
                        pointerEvents: 'none',
                        position: 'absolute',
                        top: -180,
                        opacity: 0.7,
                    }}
                />
                <Typography
                    variant="h4"
                    marked="center"
                    component="h2"
                    sx={{ mb: 14 }}
                >
                    How it works
                </Typography>
                <div>
                    <Grid container spacing={5}>
                        <Grid item xs={12} md={4}>
                            <Box sx={item}>
                                <Box sx={number}>1.</Box>
                                <Box
                                    display="flex"
                                    justifyContent="center"
                                    alignItems="center"
                                    height="160px"
                                >
                                    <KeyboardHideOutlinedIcon
                                        sx={{ fontSize: '5em' }}
                                    />
                                </Box>
                                <Typography variant="h5" align="center">
                                    Enter your myanimelist username.
                                </Typography>
                            </Box>
                        </Grid>
                        <Grid item xs={12} md={4}>
                            <Box sx={item}>
                                <Box sx={number}>2.</Box>
                                <Box
                                    display="flex"
                                    justifyContent="center"
                                    alignItems="center"
                                    height="160px"
                                >
                                    <AutorenewOutlinedIcon
                                        sx={{ fontSize: '5em' }}
                                    />
                                </Box>
                                <Typography variant="h5" align="center">
                                    Start the search and wait for the system to
                                    come up with recommendations.
                                </Typography>
                            </Box>
                        </Grid>
                        <Grid item xs={12} md={4}>
                            <Box sx={item}>
                                <Box sx={number}>3.</Box>
                                <Box
                                    display="flex"
                                    justifyContent="center"
                                    alignItems="center"
                                    height="160px"
                                >
                                    <AssignmentOutlinedIcon
                                        sx={{ fontSize: '5em' }}
                                    />
                                </Box>
                                <Typography variant="h5" align="center">
                                    {
                                        'Receive a list of fresh animes to enjoy :)'
                                    }
                                </Typography>
                            </Box>
                        </Grid>
                    </Grid>
                </div>
                <Link
                    to="/recommeder"
                    style={{ color: 'white', textDecoration: 'none' }}
                >
                    <Button
                        color="secondary"
                        size="large"
                        variant="contained"
                        component="a"
                        sx={{ mt: 8 }}
                    >
                        Get started
                    </Button>
                </Link>
            </Container>
        </Box>
    );
}

export default ProductHowItWorks;
