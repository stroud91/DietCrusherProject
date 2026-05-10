import React from "react";
import { NavLink } from 'react-router-dom';
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import Search from "../Search";
import "./Navigation.css";
import dcSmall from "../../images/dc.png";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <div className="nav-container">
      <div className="nav-left">
        <NavLink exact to="/">
          <img className="small-logo" src={dcSmall} alt="DietCrusher" />
        </NavLink>
      </div>
      <div className='searchbar'>
        <Search />
      </div>
      {sessionUser && (
        <NavLink exact to="/view-cart" className="cart-nav-btn" title="View Cart">
          🛒
        </NavLink>
      )}
      {isLoaded && (
        <div>
          <ProfileButton user={sessionUser} />
        </div>
      )}
    </div>
  );
}

export default Navigation;
