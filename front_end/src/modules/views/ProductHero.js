import * as React from 'react';
import Button from '../components/Button';
import Typography from '../components/Typography';
import ProductHeroLayout from './ProductHeroLayout';
import { Link } from 'react-router-dom';

const backgroundImage = 'https://images3.alphacoders.com/132/1322308.jpeg';

export default function ProductHero() {
    return (
        <ProductHeroLayout
            sxBackground={{
                backgroundImage: `url(${backgroundImage})`,
                backgroundColor: '#7fc7d9', // Average color of the background image.
                backgroundPosition: 'center',
            }}
        >
            {/* Increase the network loading priority of the background image. */}
            <img
                style={{ display: 'none' }}
                src={backgroundImage}
                alt="increase priority"
            />
            <Typography
                color="inherit"
                align="center"
                variant="h2"
                marked="center"
            >
                MAL Anime Recommender
            </Typography>
            <Typography
                color="inherit"
                align="center"
                variant="h5"
                sx={{ mb: 4, mt: { xs: 4, sm: 10 } }}
            >
                Start receiving fresh personal anime recommendations based on
                your own profiles
            </Typography>
            <Link
                to="/recommeder"
                style={{ color: 'white', textDecoration: 'none' }}
            >
                <Button
                    color="secondary"
                    variant="contained"
                    size="large"
                    component="a"
                    href="/premium-themes/onepirate/sign-up/"
                    sx={{ minWidth: 200 }}
                >
                    Get Recommendations
                </Button>
            </Link>
            <Typography variant="body2" color="inherit" sx={{ mt: 2 }}>
                Discover the experience
            </Typography>
        </ProductHeroLayout>
    );
}
