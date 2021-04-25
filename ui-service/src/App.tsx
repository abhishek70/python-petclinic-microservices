import React from 'react';
import './App.css';
import NavBar from './components/NavBar';
import Footer from './components/Footer';
import About from './components/About';

function App() {
    return (
        <React.Fragment>
            <NavBar/>
            <Footer/>
        </React.Fragment>
    );
}

export default App;
