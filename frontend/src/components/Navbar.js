import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/">Dashboard</Link>
      <Link to="/tasks">Tasks</Link>
      <Link to="/teams">Teams</Link>
      <Link to="/login">Login</Link>
    </nav>
  );
};

export default Navbar;
