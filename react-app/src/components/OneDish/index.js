import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useParams } from 'react-router-dom';
import { fetchOneBusiness, getAllBusinesses } from '../../store/business';
import { fetchReviewsForDish, createReview, updateReview, deleteReview } from '../../store/review';
import { getDishesForBusiness, getSingleDish, removeDishForBusiness } from '../../store/dish';
import { addItemToCart } from '../../store/cart';
import CreateReviewModal from '../CreateReviewModal';
import EditReviewModal from '../UpdateReviewModal';
import DeleteReviewModal from '../DeleteReviewModal';
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import addToCart from '../CartComponent';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import LoadingAnimation from '../Loading';

function DishDetail() {
    const dispatch = useDispatch();
    const { id } = useParams();
    const { setModalContent, closeModal } = useModal();
    const history = useHistory()
    const [loading, setLoading] = useState(true);

    const currentUser = useSelector(state => state.session.user);
    const currentDish = useSelector(state => state.dish.current);

    const currentReviews = useSelector(state => state.review.reviewsForDish);

    const currentBusiness = useSelector(state => state.business.list).find(biz => biz.id === currentDish.business_id);


  useEffect(() => {

        async function fetchData() {
            setLoading(true);
            
            await dispatch(getSingleDish(id));
            await dispatch(getAllBusinesses());
            await dispatch(fetchReviewsForDish(id));


            setTimeout(() => {
                setLoading(false);
              }, 100);
        }
        fetchData();
    }, [dispatch, id ]);

    const handleAddToCart = () => {

        if (currentDish) {
            dispatch(addItemToCart(currentDish.id, 1));

        }
    }

    const handleEditDish = async (business_id, id) => {
        // if (!currentDish) return;
        // await dispatch(removeDishForBusiness(currentDish.business_id, dishId));
        history.push(`/business/${currentBusiness.id}/update-dish/${id}`)
    };

    const handleDeleteDish = async (dishId) => {
        if (!currentDish) return;
        await dispatch(removeDishForBusiness(currentDish.business_id, dishId));
        history.push(`/business/${currentBusiness.id}`);
    };


    if (loading) {
        return <div><LoadingAnimation /></div>;
      }

    return (
        <div className="dishDetail-container">

            <img src={currentDish.image_id} alt={currentDish.name} className="dishDetail-image" />
            <h3 className="dishDetail-name">{currentDish.name}</h3>
            <p className="dishDetail-description">{currentDish.description}</p>
            <span className="dishDetail-price">${currentDish.price.toFixed(2)}</span>
            {currentUser && currentUser.id === currentBusiness.owner_id && (
                <div className="dishDetail-buttons">
                    {/* <Link to={`/business/${currentBusiness.id}/update-dish/${id}`} className="dishDetail-delete-button">Edit</Link> */}
                    <button className="dishDetail-delete-button" onClick={() => handleEditDish(currentBusiness.id,id)}>Edit</button>
                    <button className="dishDetail-delete-button" onClick={() => handleDeleteDish(currentDish.id)}>Delete</button>
                </div>
            )}

{currentUser && (
  <div className="action-buttons-container">
    {currentUser.id !== currentBusiness.owner_id && (
      <button className="action-button" onClick={handleAddToCart}>Add to Cart</button>
    )}
    {currentUser.id !== currentBusiness.owner_id && !currentReviews.some(review => review.user_id === currentUser.id) && (
      <OpenModalButton
        buttonText="Add a review"
        modalComponent={<CreateReviewModal id={id} currentUser={currentUser.id} />}
        id="dishDetail-postReview-button"
        className="action-button"
      />
    )}
  </div>
)}

<div className="dishDetail-reviews">
  <h4 className="dishDetail-reviewsTitle">Reviews</h4>
  {currentReviews.map(review => (
  <div key={review.id} className="dishDetail-reviewItem">
    <img src={review.profile_image_id} alt={review.user_name} className="dishDetail-reviewUserPhoto" />
    <div className="dishDetail-reviewContent">
      <div className="dishDetail-reviewUserDetails">
        <h5 className="dishDetail-reviewUserName">{review.user_name}</h5>
        <span className="dishDetail-reviewTime">Posted this review at : {new Date(review.created_at).toLocaleString()}</span>
      </div>
      <p className="dishDetail-reviewComment">{review.comment}</p>
      <div className="dishDetail-reviewRating">
        {[...Array(5)].map((_, index) => (
          <span key={index} className={index < review.rating ? "on" : "off"}>
            <i className="fa fa-star"></i>
          </span>
        ))}
      </div>
    </div>
      {currentUser && currentUser.id === review.user_id && (
        <div className="dishDetail-reviewButtons">
          <OpenModalButton
            buttonText="Edit"
            modalComponent={<EditReviewModal id={id} review={review} />}
            id="dishDetail-reviewEdit-button"
          />
          <OpenModalButton
            buttonText="Delete"
            modalComponent={<DeleteReviewModal id={id} reviewId={review.id} />}
            id="dishDetail-reviewDelete-button"
          />
        </div>
      )}
    </div>
  ))}
</div>

        </div>
    );
}

export default DishDetail;
