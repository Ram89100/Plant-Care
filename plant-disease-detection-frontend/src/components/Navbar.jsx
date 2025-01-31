import React from 'react';
import { NavLink } from 'react-router-dom';
import '../styles/Navbar.css';

const NavbarComponent = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">Plant Disease Detection</div>
      <ul className="navbar-links">
        <li><NavLink exact to="/" activeClassName="active">Home</NavLink></li>
        <li><NavLink to="/about" activeClassName="active">About Us</NavLink></li>
        <li><NavLink to="/contact" activeClassName="active">Contact</NavLink></li>
        <li><NavLink to="/predict" activeClassName="active">Predict</NavLink></li>
      </ul>
    </nav>
  );
};

export default NavbarComponent;
