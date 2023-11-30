import * as React from 'react';
import Box from '@mui/material/Box';
import { Link as RouterLink } from 'react-router-dom';
import Link from '@mui/material/Link';
import AppBar from '../components/AppBar';
import Toolbar from '../components/Toolbar';

function AppAppBar() {
    return (
        <div>
            <AppBar position="fixed">
                <Toolbar sx={{ justifyContent: 'space-between' }}>
                    <Box sx={{ flex: 1 }} />
                    <RouterLink
                        to="/"
                        style={{ color: 'white', textDecoration: 'none' }}
                    >
                        <Link
                            variant="h6"
                            underline="none"
                            color="inherit"
                            sx={{ fontSize: 24 }}
                        >
                            {'animmender'}
                        </Link>
                    </RouterLink>
                    <Box
                        sx={{
                            flex: 1,
                            display: 'flex',
                            justifyContent: 'flex-end',
                        }}
                    />
                </Toolbar>
            </AppBar>
            <Toolbar />
        </div>
    );
}

export default AppAppBar;
