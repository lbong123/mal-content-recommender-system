import * as React from 'react';
import Home from './modules/pages/Home';
import Recommender from './modules/pages/Recommender';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import withRoot from './modules/withRoot';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/recommender" element={<Recommender />} />
            </Routes>
        </BrowserRouter>
    );
}

export default withRoot(App);
