import React from "react";
import { NavLink, useLocation } from 'react-router-dom';
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import Search from "../Search";
import "./Navigation.css";
import dcSmall from "../../images/dc.png";
import shopCart from "../../images/shoppingcart.jpg";
function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const location = useLocation();

  return (
    <div className="nav-container">
      <div className="nav-left">
        <NavLink exact to="/">
          <img className="small-logo" src={dcSmall} alt="" />
        </NavLink>
      </div>
      {/* {location.pathname === '/' && ( */}
        <div className='searchbar'>
          <Search />
        </div>
      {/* // )} */}
      {sessionUser && (
        <NavLink exact to="/view-cart">
        <img className="small-logo2" src={shopCart} alt="" />
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
