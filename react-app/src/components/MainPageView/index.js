import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import dcImg from "../../images/dl.png";
import './MainPageView.css';
import backgroundImage from "../../images/backgroundImage.jpg"
import LoadingAnimation from "../Loading";
function MainPage() {
  const [search, setSearch] = useState('');
  const [businesses, setBusinesses] = useState([]);
  const [topRatedDishes, setTopRatedDishes] = useState([]);
  const [topOrderedDishes, setTopOrderedDishes] = useState([]);
  const [isLoading, setIsLoading] = useState(true);


  const handleSubmit = (e) => {
    e.preventDefault();

  }

  const handleChange = (e) => {
    setSearch(e.target.value);
  }

  useEffect(() => {
    async function fetchData() {

      setIsLoading(true);

      const businessesResponse = await fetch("/api/business/");
      const businessesData = await businessesResponse.json();
      setBusinesses(businessesData);

      const topRatedResponse = await fetch("/api/menu/top-rated");
      const topRatedData = await topRatedResponse.json();
      setTopRatedDishes(topRatedData);

      const topOrderedResponse = await fetch("/api/menu/top-ordered");
      const topOrderedData = await topOrderedResponse.json();
      setTopOrderedDishes(topOrderedData);

      setTimeout(() => {
        setIsLoading(false);
      }, 1000);
    }

    fetchData();
  }, []);

  if (isLoading) {
    return <div><LoadingAnimation /></div>;
  }

  const getOrdinalIndicator = (index) => {
    const ordinals = ['1st Top Rated', '2nd Top Rated', '3rd Top Rated'];
    return ordinals[index] || `${index + 1}th Top Rated`;
  }

  return businesses.length > 0 ? (
    <div className='main-page-container' style={{ backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover', backgroundPosition: 'center' }}>

      <header className='main-header'>
        {/* <Search handleSubmit={handleSubmit} handleChange={handleChange} search={search} /> */}
      </header>

      <div className="main-page-image-container">
        <img src={dcImg} alt="Cover" />
        <div className="image-text">Discover your new favorite restaurant</div>
      </div>

      <section className="top-rated-dish">
  <h2>Top Rated Dish</h2>
  <div className="dish-container">
    {topRatedDishes.map(dish => (
      <Link key={dish.id} to={`/dish/${dish.id}`} className="dish-card">
        <div className="image-for-top-rated">
          <img src={dish.image_id} alt={dish.name} />
        </div>
        <div className="dish-card-content">
          <p>{dish.name}</p>
          <p>{parseFloat(dish.rating).toFixed(2)} ★</p>
          <p>{dish.description}</p>
        </div>
      </Link>
    ))}
  </div>
</section>


<section className="top-ordered-dish">
      <h2>Top Ordered Dish</h2>
      <div className="dish-container">
        {topOrderedDishes.map((dish, index) => (
          <Link key={dish.id} to={`/dish/${dish.id}`} className="dish-card">
            <div className="image-for-top-picked">
              <img src={dish.image_id} alt={dish.name} />
            </div>
            <div className="dish-card-content">
              <p>{dish.name}</p>
              <p>{dish.description}</p>

              <p>{getOrdinalIndicator(index)}</p>
            </div>
          </Link>
        ))}
      </div>
    </section>

    <footer className='main-footer'>
  <p>
    &copy; 2023 Capstone Project - Developed by
    <a href="https://github.com/stroud91"> </a>
       <i className="fab fa-github"> </i>
    <a href="https://www.linkedin.com/in/ledian-f-47b586143/"> <a/>
      <i className="fab fa-linkedin"></i> Ledian Fekaj
    </a> - React - Python - Flask - SQLAlchemy - PostgreSQL - Redux
  </p>
</footer>

    </div>
  ) : (
    <div><LoadingAnimation /></div>
  );
}

export default MainPage;
