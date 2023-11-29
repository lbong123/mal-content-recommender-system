import * as React from 'react';
import ProductCategories from './../views/ProductCategories';
import AppFooter from './../views/AppFooter';
import ProductHero from './../views/ProductHero';
import ProductHowItWorks from './../views/ProductHowItWorks';
import AppAppBar from './../views/AppAppBar';
import withRoot from './../withRoot';

function Home() {
  return (
    <React.Fragment>
      <AppAppBar />
      <ProductHero />
      <ProductHowItWorks />
      <ProductCategories />
      <AppFooter />
    </React.Fragment>
  );
}

export default withRoot(Home);
