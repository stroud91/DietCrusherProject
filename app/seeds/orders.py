from app.models import db, Order, environment, SCHEMA
from datetime import datetime
from sqlalchemy.sql import text

def seed_orders():
   
    order1 = Order(
        user_id=1,
        total_price=25.99,
        order_date=datetime.utcnow(),
        delivery_address="123 Main St, Sample City",
        status="On the way",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    order2 = Order(
        user_id=2,
        total_price=15.49,
        order_date=datetime.utcnow(),
        delivery_address="456 Elm St, Sample City",
        status="Preparing",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    order3 = Order(
        user_id=3,
        total_price=55.89,
        order_date=datetime.utcnow(),
        delivery_address="789 Maple St, Sample City",
        status="Delivered",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    order4 = Order(
        user_id=4,
        total_price=45.67,
        order_date=datetime.utcnow(),
        delivery_address="101 Pine St, Sample City",
        status="Cancelled",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    order5 = Order(
    user_id=5,
    total_price=60.50,
    order_date=datetime.utcnow(),
    delivery_address="11 Oak St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order6 = Order(
    user_id=6,
    total_price=40.40,
    order_date=datetime.utcnow(),
    delivery_address="12 Birch St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order7 = Order(
    user_id=7,
    total_price=20.20,
    order_date=datetime.utcnow(),
    delivery_address="13 Cedar St, Sample City",
    status="Delivered",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order8 = Order(
    user_id=8,
    total_price=30.30,
    order_date=datetime.utcnow(),
    delivery_address="14 Pine St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order9 = Order(
    user_id=9,
    total_price=50.50,
    order_date=datetime.utcnow(),
    delivery_address="15 Elm St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order10 = Order(
    user_id=10,
    total_price=70.70,
    order_date=datetime.utcnow(),
    delivery_address="16 Maple St, Sample City",
    status="Cancelled",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order11 = Order(
    user_id=11,
    total_price=80.80,
    order_date=datetime.utcnow(),
    delivery_address="17 Oak St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order12 = Order(
    user_id=12,
    total_price=90.90,
    order_date=datetime.utcnow(),
    delivery_address="18 Birch St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order13 = Order(
    user_id=13,
    total_price=65.65,
    order_date=datetime.utcnow(),
    delivery_address="19 Cedar St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order14 = Order(
    user_id=14,
    total_price=75.75,
    order_date=datetime.utcnow(),
    delivery_address="20 Pine St, Sample City",
    status="Delivered",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order15 = Order(
    user_id=15,
    total_price=85.85,
    order_date=datetime.utcnow(),
    delivery_address="21 Ash St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order16 = Order(
    user_id=16,
    total_price=95.95,
    order_date=datetime.utcnow(),
    delivery_address="22 Beech St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order17 = Order(
    user_id=17,
    total_price=55.55,
    order_date=datetime.utcnow(),
    delivery_address="23 Cherry St, Sample City",
    status="Delivered",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order18 = Order(
    user_id=18,
    total_price=45.45,
    order_date=datetime.utcnow(),
    delivery_address="24 Dogwood St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order19 = Order(
    user_id=19,
    total_price=35.35,
    order_date=datetime.utcnow(),
    delivery_address="25 Elder St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order20 = Order(
    user_id=20,
    total_price=25.25,
    order_date=datetime.utcnow(),
    delivery_address="26 Fir St, Sample City",
    status="Cancelled",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order21 = Order(
    user_id=21,
    total_price=15.15,
    order_date=datetime.utcnow(),
    delivery_address="27 Gum St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order22 = Order(
    user_id=22,
    total_price=5.05,
    order_date=datetime.utcnow(),
    delivery_address="28 Hickory St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order23 = Order(
    user_id=23,
    total_price=10.10,
    order_date=datetime.utcnow(),
    delivery_address="29 Ironwood St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order24 = Order(
    user_id=24,
    total_price=20.20,
    order_date=datetime.utcnow(),
    delivery_address="30 Juniper St, Sample City",
    status="Delivered",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)
    order25 = Order(
    user_id=25,
    total_price=65.65,
    order_date=datetime.utcnow(),
    delivery_address="31 Kite St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order26 = Order(
    user_id=26,
    total_price=75.75,
    order_date=datetime.utcnow(),
    delivery_address="32 Lemon St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order27 = Order(
    user_id=27,
    total_price=85.85,
    order_date=datetime.utcnow(),
    delivery_address="33 Mango St, Sample City",
    status="Delivered",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order28 = Order(
    user_id=28,
    total_price=50.50,
    order_date=datetime.utcnow(),
    delivery_address="34 Nutmeg St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order29 = Order(
    user_id=29,
    total_price=60.60,
    order_date=datetime.utcnow(),
    delivery_address="35 Olive St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order30 = Order(
    user_id=30,
    total_price=30.30,
    order_date=datetime.utcnow(),
    delivery_address="36 Peach St, Sample City",
    status="Cancelled",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order31 = Order(
    user_id=31,
    total_price=40.40,
    order_date=datetime.utcnow(),
    delivery_address="37 Quince St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order32 = Order(
    user_id=32,
    total_price=20.20,
    order_date=datetime.utcnow(),
    delivery_address="38 Raspberry St, Sample City",
    status="On the way",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order33 = Order(
    user_id=33,
    total_price=10.10,
    order_date=datetime.utcnow(),
    delivery_address="39 Strawberry St, Sample City",
    status="Preparing",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)

    order34 = Order(
    user_id=34,
    total_price=70.70,
    order_date=datetime.utcnow(),
    delivery_address="40 Tangerine St, Sample City",
    status="Delivered",
    created_at=datetime.utcnow(),
    updated_at=datetime.utcnow()
)


    db.session.add_all([order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12, order13, order14,
                        order15, order16, order17, order18, order19, order20, order21, order22, order23, order24,
                        order25, order26, order27, order28, order29, order30, order31, order32, order33, order34])
    db.session.commit()


def undo_orders():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM orders"))

    db.session.commit()
