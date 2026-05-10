import React, { useEffect,useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOneBusiness} from "../../store/business";
import {getDishesForBusiness} from "../../store/dish"
import { useParams, useHistory } from "react-router-dom";
import { deleteBusiness } from "../../store/business";
import { addItemToCart } from "../../store/cart";
import { fetchSingleBusinessReviews } from "../../store/review";
import {removeDishForBusiness} from '../../store/dish'
import DishCreationForm from '../CreateDishForm'
import OpenModalButton from "../OpenModalButton";
import DeleteDishModal from "../DeleteDishModal";
import "./OneBusiness.css";
import plusImage from '../../images/plusimage.jpg'
import { useModal } from "../../context/Modal";
import addToCart from '../CartComponent';
import LoadingAnimation from "../Loading";

function BusinessDetails() {

    const history = useHistory();
    const dispatch = useDispatch();
    const { id } = useParams();
    const { setModalContent } = useModal();


    const [loading, setLoading] = useState(true);
    const [showAddDishForm, setShowAddDishForm] = useState(false);
    const [showAddBusinesshForm, setShowAddBusinessForm] = useState(false);
    const selectedBusiness = useSelector((state) => state.business.selectedBusiness);
    const dishes = useSelector((state) => state.dish.dishesForBusiness);
    const currentUser = useSelector((state) => state.session.user);
    const reviews = useSelector((state) => state.review.allReviews);
    const user = currentUser;


    const showAddDishFormFunction = () => {
        history.push(`/create-dish`);
    }

    const setSelectedDish = (id) => {

        history.push(`/dish/${id}`);
    }

    const handleEdit = (businessId, id, event) => {
        event.stopPropagation();
        history.push(`/business/${businessId}/update-dish/${id}`);
    }

    const handleAddToCart = (dishId, event) => {

        event.stopPropagation();
        dispatch(addItemToCart(dishId, 1));
    };

    const handleDelete = (businessId, dishId, event) => {
        event.stopPropagation();
        setModalContent(<DeleteDishModal businessId={businessId} dishId={dishId} />);
    };


    useEffect(() => {
        let isMounted = true;

        async function fetchData() {
            if (isMounted) {
                await dispatch(fetchOneBusiness(id));
                await dispatch(getDishesForBusiness(id));
                await dispatch(fetchSingleBusinessReviews(id));
                setLoading(false);
            }
        }

        fetchData();

        return () => isMounted = false;
    }, [dispatch, id]);

    if (loading) {
        return <div><LoadingAnimation /></div>;
    }

    return (

        <div className="business-info-container">

    <div className="business-logo">
        <img src={selectedBusiness.logo_id} alt="Business Logo" />
    </div>
    <div className="business-name">
        {/* Name of the business */}
        {selectedBusiness.name}
    </div>
    <div className="business-details">
        <p>About: {selectedBusiness.about}</p>
        <p>Address: {selectedBusiness.address}, {selectedBusiness.city}</p>
        <p>Email: {selectedBusiness.email}</p>
        <p>Phone Number: {selectedBusiness.phone}</p>
    </div>


            <div className="dishes-container">
                {dishes.map(dish => (
                    <div className="dish" onClick={() => setSelectedDish(dish.id)}>
                        <div className="dish-photo-container">
                            <img src={dish.image_id} alt={dish.name} className="dish-image" />
                        </div>
                        <div className="dish-info">
                        <h4>{dish.name}</h4>
                        <h4>Price: ${dish.price}</h4>
                        </div>
                        {user && selectedBusiness.owner_id === user.id && (
                            <div className="dish-owner-actions">
                                <button className="edit-btn" onClick={(event) => handleEdit(selectedBusiness.id, dish.id, event)}>Edit</button>
                                <button className="delete-btn" onClick={(event) => handleDelete(selectedBusiness.id, dish.id, event)}>Delete</button>
                            </div>
                        )}
                        {user && (
  <div className="dish-user-actions">
    <button className="add-to-cart-btn" onClick={(event) => handleAddToCart(dish.id, event)}>Add to Cart</button>
  </div>
)}
                    </div>
                ))}
                {user && selectedBusiness.owner_id === user.id && (
                    <div className="add-new-dish" onClick={showAddDishFormFunction}>
                    <div className="add-dish-plus- container">
                            <img src={plusImage} alt=""className="plus-image" />
                        </div>
                 <p>Add a new dish</p>
                </div>
                )}
                {/* Conditionally render the DishCreationForm */}
                {showAddDishForm && <DishCreationForm />}
            </div>
        </div>

    );
}


export default BusinessDetails;
