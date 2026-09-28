import React from 'react';
import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-grid">
        <div>
          <strong>Diet Crusher</strong>
          <p className="muted small">Local kitchens. Honest food. Delivered.</p>
        </div>
        <div className="footer-links">
          <Link to="/all">Restaurants</Link>
          <Link to="/create-business">Add your restaurant</Link>
          <Link to="/orders">Your orders</Link>
        </div>
        <div className="footer-links">
          <a href="https://github.com/stroud91" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a href="https://www.linkedin.com/in/ledian-f-47b586143/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        </div>
      </div>
      <div className="container footer-legal muted small">
        © {new Date().getFullYear()} Diet Crusher · Designed and built by Ledian Fekaj · React · Flask · PostgreSQL
      </div>
    </footer>
  );
}
