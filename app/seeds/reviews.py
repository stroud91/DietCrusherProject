from app.models import db, Review, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_reviews():

    review1 = Review(
        user_id=1,
        dish_id=1,
        rating=5,
        comment="Delicious! One of the best dishes I've ever tried.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review2 = Review(
        user_id=2,
        dish_id=2,
        rating=4,
        comment="Really good but a tad too spicy for my taste.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review3 = Review(
        user_id=3,
        dish_id=3,
        rating=3,
        comment="It's alright. Not what I expected but still decent.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review4 = Review(
        user_id=4,
        dish_id=4,
        rating=4,
        comment="Yummy! Would definitely order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review5 = Review(
        user_id=5,
        dish_id=5,
        rating=5,
        comment="A must-try. I can't wait to have it again!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review6 = Review(
        user_id=6,
        dish_id=6,
        rating=3,
        comment="It was just average. I expected more.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review7 = Review(
        user_id=7,
        dish_id=7,
        rating=5,
        comment="Incredibly delicious! I'll definitely come back for more.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review8 = Review(
        user_id=6,
        dish_id=8,
        rating=5,
        comment="Incredibly delicious! I'll definitely come back for more.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    review9 = Review(
        user_id=5,
        dish_id=9,
        rating=5,
        comment="Absolutely loved it! Will order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review10 = Review(
        user_id=5,
        dish_id=10,
        rating=5,
        comment="Absolutely loved it! Will order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review11 = Review(
        user_id=6,
        dish_id=11,
        rating=4,
        comment="Tasty, but could use a bit more spice.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review12 = Review(
        user_id=7,
        dish_id=12,
        rating=3,
        comment="It was alright. Might try something different next time.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review13 = Review(
        user_id=8,
        dish_id=13,
        rating=4,
        comment="Quite delightful. The texture was perfect.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review32 = Review(
        user_id=2,
        dish_id=32,
        rating=5,
        comment="Highly recommended! A must-try.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review34 = Review(
        user_id=34,
        dish_id=34,
        rating=4,
        comment="Very tasty, but I wish the portion was bigger.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review35 = Review(
        user_id=35,
        dish_id=35,
        rating=4,
        comment="Delicious, but it could use a bit more salt.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review36 = Review(
        user_id=36,
        dish_id=36,
        rating=5,
        comment="This dish exceeded my expectations. Truly delightful!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review37 = Review(
        user_id=37,
        dish_id=37,
        rating=4,
        comment="Quite good, but lacked a bit in presentation.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review38 = Review(
        user_id=38,
        dish_id=38,
        rating=3,
        comment="An okay dish, but not memorable.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review39 = Review(
        user_id=39,
        dish_id=39,
        rating=5,
        comment="Absolutely delicious! Can't wait to order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review40 = Review(
        user_id=40,
        dish_id=40,
        rating=4,
        comment="A delightful treat! Will recommend to friends.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review41 = Review(
        user_id=41,
        dish_id=41,
        rating=5,
        comment="The flavors melded together perfectly. A masterpiece!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review42 = Review(
        user_id=42,
        dish_id=42,
        rating=4,
        comment="Good, but I've had better elsewhere.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review43 = Review(
        user_id=43,
        dish_id=43,
        rating=3,
        comment="Was expecting more given the price.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review44 = Review(
        user_id=44,
        dish_id=44,
        rating=5,
        comment="Perfect dish! Just the right amount of everything.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review45 = Review(
        user_id=45,
        dish_id=45,
        rating=4,
        comment="Pleasantly surprised by the taste and presentation.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review46 = Review(
        user_id=46,
        dish_id=46,
        rating=2,
        comment="Didn't live up to the hype, unfortunately.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review47 = Review(
        user_id=47,
        dish_id=47,
        rating=5,
        comment="One of the best dishes I've ever tasted!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review48 = Review(
        user_id=48,
        dish_id=48,
        rating=3,
        comment="Average taste, nothing special.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review49 = Review(
        user_id=49,
        dish_id=49,
        rating=4,
        comment="Great dish, just a bit too spicy for my liking.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review50 = Review(
        user_id=50,
        dish_id=50,
        rating=5,
        comment="Perfect balance of flavors. Highly recommend!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review51 = Review(
        user_id=51,
        dish_id=51,
        rating=3,
        comment="It was alright, might try something else next time.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review52 = Review(
        user_id=52,
        dish_id=52,
        rating=4,
        comment="Enjoyed the dish, but the portion size was a bit small.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review53 = Review(
        user_id=53,
        dish_id=53,
        rating=2,
        comment="Not a fan of this dish. Found it a bit bland.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review54 = Review(
        user_id=54,
        dish_id=54,
        rating=5,
        comment="Amazing flavors! Will definitely order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review55 = Review(
        user_id=55,
        dish_id=55,
        rating=4,
        comment="Good dish overall. The sauce was the highlight.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review56 = Review(
        user_id=56,
        dish_id=56,
        rating=4,
        comment="This was pretty good. The seasoning was just right.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review57 = Review(
        user_id=57,
        dish_id=57,
        rating=5,
        comment="Absolutely delicious! Will order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review58 = Review(
        user_id=58,
        dish_id=58,
        rating=3,
        comment="Average taste, might not order again.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review59 = Review(
        user_id=59,
        dish_id=59,
        rating=1,
        comment="I didn't like this at all. Way too greasy.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review60 = Review(
        user_id=60,
        dish_id=60,
        rating=5,
        comment="Impressive flavor and presentation!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review61 = Review(
        user_id=61,
        dish_id=59,
        rating=4,
        comment="Really good, though I'd prefer a little less salt.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review62 = Review(
        user_id=62,
        dish_id=55,
        rating=3,
        comment="It was okay, a bit underwhelming.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review63 = Review(
        user_id=63,
        dish_id=58,
        rating=2,
        comment="Not my cup of tea. Found it too spicy.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review64 = Review(
        user_id=64,
        dish_id=56,
        rating=5,
        comment="Fantastic! Loved every bite of it.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review65 = Review(
        user_id=65,
        dish_id=54,
        rating=4,
        comment="Tasty, but could use more veggies.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review66 = Review(
        user_id=66,
        dish_id=52,
        rating=4,
        comment="The sauce was perfect but the chicken was a bit dry.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review67 = Review(
        user_id=67,
        dish_id=51,
        rating=2,
        comment="Wasn't what I was expecting. Needs more flavor.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review68 = Review(
        user_id=68,
        dish_id=50,
        rating=5,
        comment="Mouth-watering and succulent. Highly recommended!",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review69 = Review(
        user_id=69,
        dish_id=49,
        rating=3,
        comment="It's decent but I've had better at this price point.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review70 = Review(
        user_id=70,
        dish_id=40,
        rating=4,
        comment="Really satisfying, especially with the dipping sauce.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review71 = Review(
        user_id=71,
        dish_id=41,
        rating=3,
        comment="Enjoyable but not memorable.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review72 = Review(
        user_id=72,
        dish_id=41,
        rating=5,
        comment="This dish was an explosion of flavors! Absolutely amazing.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    review73 = Review(
        user_id=73,
        dish_id=43,
        rating=4,
        comment="Would have liked a bit more spice, but still quite good.",
        review_date=datetime.datetime.now(),
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )


    db.session.add_all([
        review1, review2, review3, review4, review5, review6, review7, review8, review9, review10,
        review11, review12, review13, review32,  review34, review35,
        review36, review37, review38, review39, review40,
        review41, review42, review43, review44, review45,
        review46, review47, review48, review49, review50,
        review51, review52, review53, review54, review55,
        review56, review57, review58, review59, review60,
        review61, review62, review63, review64, review65,
        review66, review67, review68, review69, review70,
        review71, review72, review73 ,
    ])

    db.session.commit()

def undo_reviews():
    if environment == "production":
       db.session.execute(text(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;"))
    else:
       db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
