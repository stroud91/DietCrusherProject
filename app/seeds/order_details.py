from app.models import db, OrderDetail, environment, SCHEMA
from sqlalchemy.sql import text

def seed_order_details():

    order_detail1 = OrderDetail(
        order_id=1,
        dish_id=1,
        quantity=2,
        subtotal_price=49.98
    )

    order_detail2 = OrderDetail(
        order_id=2,
        dish_id=2,
        quantity=1,
        subtotal_price=15.49
    )

    order_detail3 = OrderDetail(
        order_id=3,
        dish_id=3,
        quantity=3,
        subtotal_price=167.67
    )

    order_detail4 = OrderDetail(
        order_id=4,
        dish_id=4,
        quantity=2,
        subtotal_price=91.34
    )

    order_detail5 = OrderDetail(
        order_id=5,
        dish_id=5,
        quantity=4,
        subtotal_price=242.00
    )

    order_detail6 = OrderDetail(
        order_id=6,
        dish_id=6,
        quantity=2,
        subtotal_price=80.80
    )

    order_detail7 = OrderDetail(
        order_id=7,
        dish_id=7,
        quantity=1,
        subtotal_price=20.20
    )

    order_detail8 = OrderDetail(
        order_id=8,
        dish_id=8,
        quantity=3,
        subtotal_price=90.90
    )

    order_detail9 = OrderDetail(
        order_id=9,
        dish_id=9,
        quantity=2,
        subtotal_price=101.00
    )

    order_detail10 = OrderDetail(
        order_id=10,
        dish_id=10,
        quantity=2,
        subtotal_price=141.40
    )
    order_detail11 = OrderDetail(
        order_id=11,
        dish_id=11,
        quantity=3,
        subtotal_price=70.35
    )

    order_detail12 = OrderDetail(
        order_id=12,
        dish_id=12,
        quantity=4,
        subtotal_price=130.60
    )

    order_detail13 = OrderDetail(
        order_id=13,
        dish_id=13,
        quantity=2,
        subtotal_price=90.90
    )

    order_detail14 = OrderDetail(
        order_id=14,
        dish_id=14,
        quantity=1,
        subtotal_price=50.50
    )

    order_detail15 = OrderDetail(
        order_id=15,
        dish_id=15,
        quantity=3,
        subtotal_price=120.45
    )

    order_detail16 = OrderDetail(
        order_id=16,
        dish_id=16,
        quantity=4,
        subtotal_price=150.60
    )

    order_detail17 = OrderDetail(
        order_id=17,
        dish_id=17,
        quantity=1,
        subtotal_price=30.30
    )

    order_detail18 = OrderDetail(
        order_id=18,
        dish_id=18,
        quantity=2,
        subtotal_price=75.75
    )

    order_detail19 = OrderDetail(
        order_id=19,
        dish_id=19,
        quantity=3,
        subtotal_price=99.99
    )

    order_detail20 = OrderDetail(
        order_id=20,
        dish_id=20,
        quantity=4,
        subtotal_price=145.80
    )
    db.session.add_all([order_detail1, order_detail2, order_detail3, order_detail4, order_detail5,
                        order_detail6, order_detail7, order_detail8, order_detail9, order_detail10,
                        order_detail11, order_detail12, order_detail13, order_detail14, order_detail15,
                        order_detail16, order_detail17, order_detail18, order_detail19, order_detail20])
    db.session.commit()

def undo_order_details():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.orderdetails RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM orderdetails"))
    db.session.commit()
