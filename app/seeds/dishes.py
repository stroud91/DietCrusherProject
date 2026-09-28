from app.models import db, Dish, Business, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_dishes():

    # Dishes for "Rita's Italian Ice & Frozen Custard"
    dish1 = Dish(
        business_id=1,
        name="Vanilla Italian Ice",
        description="Smooth and creamy classic vanilla flavor.",
        image_id="data:image/jpeg;base64,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",
        price=4.50,
        category_id=9,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    dish2 = Dish(
        business_id=1,
        name="Chocolate Frozen Custard",
        description="Rich and indulgent frozen custard with deep chocolate flavor.",
        image_id="data:image/jpeg;base64,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",
        price=5.00,
        category_id=9,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Dishes for "Bella's Bagels"
    dish3 = Dish(
        business_id=2,
        name="Classic Plain Bagel",
        description="A classic plain bagel, crispy on the outside and soft on the inside.",
        image_id="data:image/jpeg;base64,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",
        price=1.50,
        category_id=8,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    dish4 = Dish(
        business_id=2,
        name="Bagel with Cream Cheese",
        description="A delicious bagel slathered with creamy cheese.",
        image_id="data:image/jpeg;base64,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",
        price=2.50,
        category_id=8,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Dishes for "Gaspare's Pizza House & Italian Restaurant"
    dish5 = Dish(
        business_id=3,
        name="Margherita Pizza",
        description="Classic pizza with fresh tomatoes, mozzarella, and basil.",
        image_id="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsEdft2BtcWK-1ZQsatmTKrPNodMGgCDq5GA&usqp=CAU",
        price=14.99,
        category_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    dish6 = Dish(
        business_id=3,
        name="Spaghetti Carbonara",
        description="Classic Italian pasta dish with bacon, egg, and cheese.",
        image_id="https://images.unsplash.com/photo-1588013273468-315fd88ea34c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8c3BhZ2hldHRpJTIwY2FyYm9uYXJhfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
        price=13.99,
        category_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    # Dishes for "Roma Antica"
    dish7 = Dish(
    business_id=4,
    name="Penne Arrabbiata",
    description="Penne pasta in a spicy tomato sauce with garlic and chili peppers.",
    image_id="https://images.unsplash.com/photo-1501934398334-266c81d54888?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8UGVubmUlMjBBcnJhYmJpYXRhfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=12.99,
    category_id=2,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish8 = Dish(
    business_id=4,
    name="Fettuccine Alfredo",
    description="Creamy pasta dish made with fettuccine and rich alfredo sauce.",
    image_id="https://images.unsplash.com/photo-1693609929945-b01ae4f2d602?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZmV0dHVjY2luZSUyMGFsZnJlZG98ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=14.99,
    category_id=3,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "The Italian Homemade Company"
    dish9 = Dish(
    business_id=5,
    name="Tiramisu",
    description="Classic Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cheese.",
    image_id="https://images.unsplash.com/photo-1639744211487-b27e3551b07c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8VGlyYW1pc3V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=6.50,
    category_id=9,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish10 = Dish(
    business_id=5,
    name="Ravioli",
    description="Homemade pasta filled with ricotta cheese and spinach, served with tomato sauce.",
    image_id="https://images.unsplash.com/photo-1587740908075-9e245070dfaa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8UmF2aW9saXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=15.99,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Fiorella - Sunset"
    dish11 = Dish(
    business_id=6,
    name="Quattro Formaggi Pizza",
    description="Four cheese pizza with mozzarella, gorgonzola, parmesan, and ricotta.",
    image_id="https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8UXVhdHRybyUyMEZvcm1hZ2dpJTIwUGl6emF8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=16.99,
    category_id=3,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish12 = Dish(
    business_id=6,
    name="Calzone",
    description="Folded pizza filled with cheese, ham, and mushrooms.",
    image_id="https://images.unsplash.com/photo-1641244999574-5afea228bd26?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Q2Fsem9uZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=14.99,
    category_id=2,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Cielito Lindo"
    dish13 = Dish(
    business_id=7,
    name="Taco Al Pastor",
    description="Tacos filled with marinated pork, pineapple, and cilantro.",
    image_id="https://images.unsplash.com/photo-1606168152642-aae9b879f3bd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8VGFjbyUyMEFsJTIwUGFzdG9yfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=3.50,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish14 = Dish(
    business_id=7,
    name="Guacamole",
    description="Freshly made guacamole with ripe avocados, tomatoes, onions, and cilantro.",
    image_id="https://images.unsplash.com/photo-1595016111459-799a195e7452?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8R3VhY2Ftb2xlfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=5.99,
    category_id=3,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Sunset Cantina"
    dish15 = Dish(
    business_id=8,
    name="Chicken Enchiladas",
    description="Tortillas filled with seasoned chicken and topped with red chili sauce and cheese.",
    image_id="https://images.unsplash.com/photo-1570461226513-e08b58a52c53?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Q2hpY2tlbiUyMEVuY2hpbGFkYXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=12.99,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish16 = Dish(
    business_id=8,
    name="Churros",
    description="Deep-fried dough pastries, dusted with sugar and served with chocolate dipping sauce.",
    image_id="https://images.unsplash.com/photo-1624371414361-e670edf4898d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Q2h1cnJvc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=5.50,
    category_id=5,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    # Dishes for "Otra"
    dish17 = Dish(
    business_id=9,
    name="Taco de Chorizo",
    description="Soft tortillas filled with spicy Mexican sausage, topped with onions and cilantro.",
    image_id="https://images.unsplash.com/photo-1604467715878-83e57e8bc129?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8VGFjbyUyMGRlJTIwQ2hvcml6b3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=3.25,
    category_id=5,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish18 = Dish(
    business_id=9,
    name="Ceviche Tostada",
    description="Fresh seafood marinated in citrus juices, mixed with tomatoes, onions, and cilantro. Served on a crispy tostada.",
    image_id="https://images.unsplash.com/photo-1533658266890-8bd362930725?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Q2V2aWNoZSUyMFRvc3RhZGF8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=9.99,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Santeria"
    dish19 = Dish(
    business_id=10,
    name="Mole Enchiladas",
    description="Chicken-filled tortillas smothered in rich mole sauce, topped with sesame seeds.",
    image_id="https://plus.unsplash.com/premium_photo-1664648234239-a0bc3fcd6ded?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8RW5jaGlsYWRhc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=12.50,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish20 = Dish(
    business_id=10,
    name="Tamales",
    description="Steamed corn dough filled with seasoned pork, served with salsa on the side.",
    image_id="https://images.unsplash.com/photo-1587569906338-f79d500d7122?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8VGFtYWxlc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=10.99,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "El Farolito"
    dish21 = Dish(
    business_id=11,
    name="Super Burrito",
    description="Large flour tortilla filled with rice, beans, cheese, guacamole, and choice of meat.",
    image_id="https://images.unsplash.com/photo-1662116765994-1e4200c43589?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8U3VwZXIlMjBCdXJyaXRvfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=9.75,
    category_id=1,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish22 = Dish(
    business_id=11,
    name="Quesadilla Suiza",
    description="Large grilled tortilla filled with melted cheese, meat, and served with guacamole and sour cream.",
    image_id="https://images.unsplash.com/photo-1618040996337-56904b7850b9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8UXVlc2FkaWxsYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=8.99,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Caliente Bistro Kitchen"
    dish23 = Dish(
    business_id=12,
    name="Chili Relleno",
    description="Fried poblano pepper stuffed with cheese, served in tomato sauce.",
    image_id="https://plus.unsplash.com/premium_photo-1664475990295-e4518c63edaf?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Q2hpbGklMjBSZWxsZW5vfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=10.50,
    category_id=10,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish24 = Dish(
    business_id=12,
    name="Sopa de Tortilla",
    description="Traditional Mexican tortilla soup with chicken, tomatoes, and avocado.",
    image_id="https://images.unsplash.com/photo-1653402998238-4f35e960ea80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8U29wYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=7.50,
    category_id=10,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish25 = Dish(
    business_id=12,
    name="Nachos Supreme",
    description="Tortilla chips topped with cheese, beans, jalapenos, sour cream, guacamole, and choice of meat.",
    image_id="https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8TmFjaG9zfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=9.99,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish26 = Dish(
    business_id=12,
    name="Carnitas Tacos",
    description="Soft tacos filled with slow-cooked pork, onions, and cilantro.",
    image_id="https://images.unsplash.com/photo-1551504734-5ee1c4a1479b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8VGFjb3N8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=8.99,
    category_id=5,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    # Dishes for "Mazra"
    dish27 = Dish(
    business_id=13,
    name="Shawarma Platter",
    description="Grilled spiced meat, served with rice, pita, and a side of tahini sauce.",
    image_id="https://images.unsplash.com/photo-1542528180-1c2803fa048c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8U2hhd2FybWElMjBQbGF0dGVyfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=14.50,
    category_id=6,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish28 = Dish(
    business_id=13,
    name="Hummus Bowl",
    description="Creamy chickpea spread, topped with olive oil and served with pita bread.",
    image_id="https://plus.unsplash.com/premium_photo-1667428304100-a1e05281347f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8SHVtbXVzJTIwQm93bHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=7.99,
    category_id=3,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Beit Rima"
    dish29 = Dish(
    business_id=14,
    name="Falafel Plate",
    description="Crispy chickpea balls, served with salad, pickles, and tahini sauce.",
    image_id="https://images.unsplash.com/photo-1681072530653-db8fe2538631?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fEZhbGFmZWwlMjBQbGF0ZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=12.75,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish30 = Dish(
    business_id=14,
    name="Mujaddara",
    description="A mix of lentils, rice, and caramelized onions, served with a side of yogurt.",
    image_id="https://www.themediterraneandish.com/wp-content/uploads/2022/03/mujadara-recipe-209-1024x1536.jpg",
    price=10.50,
    category_id=5,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Abu Salim Middle Eastern Grill"
    dish31 = Dish(
    business_id=15,
    name="Kebab Combo",
    description="A combination of chicken and beef skewers, grilled to perfection, served with rice and salad.",
    image_id="https://images.unsplash.com/photo-1579630941903-4ff514d6fa1f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8S2ViYWIlMjBDb21ib3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=15.99,
    category_id=6,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish32 = Dish(
    business_id=15,
    name="Baba Ganoush",
    description="Smoky roasted eggplant spread, blended with tahini and spices, served with pita.",
    image_id="https://images.unsplash.com/photo-1684706311852-c0b8941f2674?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8QmFiYSUyMEdhbm91c2h8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=8.25,
    category_id=7,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Beit Rima (86 Carl St)"
    dish33 = Dish(
    business_id=16,
    name="Stuffed Grape Leaves",
    description="Grape leaves filled with rice and herbs, served with yogurt dip.",
    image_id="https://plus.unsplash.com/premium_photo-1667545476089-a233da1e89ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8U3R1ZmZlZCUyMEdyYXBlJTIwTGVhdmVzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=9.50,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish34 = Dish(
    business_id=16,
    name="Za'atar Manakeesh",
    description="Flatbread topped with za'atar spice blend and olive oil, baked until crispy.",
    image_id="https://images.unsplash.com/photo-1630500187389-67b620ffa15e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8WmEnYXRhciUyME1hbmFrZWVzaHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=7.75,
    category_id=9,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish35 = Dish(
    business_id=16,
    name="Fattoush Salad",
    description="Mixed salad with tomatoes, cucumbers, onions, and crispy pita chips, dressed in lemon and olive oil.",
    image_id="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8RmF0dG91c2glMjBTYWxhZHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=8.99,
    category_id=10,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    # Dishes for "Reems"
    dish36 = Dish(
    business_id=17,
    name="Spinach Fatayer",
    description="Savory pastry filled with a mix of spinach, onions, and sumac.",
    image_id="https://images.unsplash.com/photo-1515363578674-99f41329ab4c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8U3BpbmFjaCUyMEZhdGF5ZXJ8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=5.25,
    category_id=1,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish37 = Dish(
    business_id=17,
    name="Ka'ak Bread",
    description="Traditional street bread, topped with sesame seeds, perfect for sandwiches or dips.",
    image_id="https://images.unsplash.com/photo-1509440159596-0249088772ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8S2EnYWslMjBCcmVhZHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=3.50,
    category_id=2,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Old Jerusalem Restaurant"
    dish38 = Dish(
    business_id=18,
    name="Chicken Shawarma Plate",
    description="Marinated and grilled chicken, thinly sliced, served with rice, hummus, and salad.",
    image_id="https://images.unsplash.com/photo-1514843319620-4f042827c481?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Q2hpY2tlbiUyMFNoYXdhcm1hJTIwUGxhdGV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=14.99,
    category_id=3,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish39 = Dish(
    business_id=18,
    name="Mansaf",
    description="Traditional dish made with lamb cooked in a yogurt sauce, served over rice.",
    image_id="https://www.fufuskitchen.com/wp-content/uploads/2023/09/89412345-D8D8-4764-9666-76B2F628E4F7.webp",
    price=16.50,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Shoshin Sushi"
    dish40 = Dish(
    business_id=19,
    name="Nigiri Platter",
    description="Assorted fish over pressed rice. Chef's selection.",
    image_id="https://images.unsplash.com/photo-1556845754-6f01a6cf8d21?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8TmlnaXJpJTIwUGxhdHRlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=21.00,
    category_id=5,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish41 = Dish(
    business_id=19,
    name="Dragon Roll",
    description="Eel, cucumber, and avocado roll topped with thin slices of avocado.",
    image_id="https://images.unsplash.com/photo-1611143669185-af224c5e3252?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8RHJhZ29uJTIwUm9sbCUyMHN1c2hpfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=13.50,
    category_id=6,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Yuji"
    dish42 = Dish(
    business_id=20,
    name="Udon Soup",
    description="Thick noodles in a flavorful broth, topped with green onions and tempura bits.",
    image_id="https://plus.unsplash.com/premium_photo-1664299332779-5cadf16015a7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8VWRvbiUyMFNvdXB8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=10.99,
    category_id=7,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish43 = Dish(
    business_id=20,
    name="Teriyaki Chicken Bowl",
    description="Grilled chicken glazed with teriyaki sauce, served over rice with steamed vegetables.",
    image_id="",
    price=12.75,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish44 = Dish(
    business_id=20,
    name="Tempura Platter",
    description="Assortment of deep-fried vegetables and shrimp, served with a dipping sauce.",
    image_id="https://images.unsplash.com/photo-1636401870585-a8852371e84a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8VGVyaXlha2klMjBDaGlja2VuJTIwQm93bHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=14.25,
    category_id=9,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)


    # Dishes for "Japateam Sushi"
    dish45 = Dish(
    business_id=21,
    name="Salmon Sashimi",
    description="Fresh slices of raw salmon, served with wasabi and soy sauce.",
    image_id="https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c2FsbW9ufGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=12.00,
    category_id=10,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish46 = Dish(
    business_id=21,
    name="Miso Ramen",
    description="Noodle soup with a miso-flavored broth, topped with pork slices, bamboo shoots, and egg.",
    image_id="https://images.unsplash.com/photo-1623341214825-9f4f963727da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cmFtZW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=14.50,
    category_id=1,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Bento Peak"
    dish47 = Dish(
    business_id=22,
    name="Chicken Katsu Bento",
    description="Crispy breaded chicken cutlet served with rice, salad, and pickled vegetables.",
    image_id="https://images.unsplash.com/photo-1597075561373-cf8898ec7290?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Q2hpY2tlbiUyMEthdHN1fGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=13.99,
    category_id=2,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish48 = Dish(
    business_id=22,
    name="Tempura Udon",
    description="Thick noodles in a clear broth, served with shrimp and vegetable tempura on the side.",
    image_id="https://images.unsplash.com/photo-1498601761256-9e93c6f5c181?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8VGVtcHVyYSUyMFVkb258ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=12.50,
    category_id=3,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Nara Restaurant & Sake Bar"
    dish49 = Dish(
    business_id=23,
    name="Tuna Tataki",
    description="Lightly seared tuna slices with a citrusy ponzu sauce.",
    image_id="https://images.unsplash.com/photo-1501595091296-3aa970afb3ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8dHVuYXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=14.00,
    category_id=4,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish50 = Dish(
    business_id=23,
    name="Nara Special Roll",
    description="Sushi roll with crab, avocado, and cucumber, topped with seared salmon and a special sauce.",
    image_id="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8c3VzaGl8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=16.00,
    category_id=5,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Izakaya Mayumi"
    dish51 = Dish(
    business_id=24,
    name="Grilled Skewers Platter",
    description="Assorted skewers of meat and vegetables, grilled to perfection.",
    image_id="https://images.unsplash.com/photo-1598511796318-7b8256bd2b20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8R3JpbGxlZCUyMFNrZXdlcnMlMjBQbGF0dGVyfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=18.50,
    category_id=6,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish52 = Dish(
    business_id=24,
    name="Sake-steamed Clams",
    description="Fresh clams steamed in sake, infused with the flavors of garlic and herbs.",
    image_id="https://images.unsplash.com/photo-1448043552756-e747b7a2b2b8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3RlYW1lZCUyMENsYW1zfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=15.25,
    category_id=7,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)


    # More dishes for "Izakaya Mayumi"
    dish53 = Dish(
    business_id=24,
    name="Shoyu Ramen",
    description="Soy sauce based broth with pork belly, egg, and bamboo shoots.",
    image_id="https://images.unsplash.com/photo-1618889482923-38250401a84e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8cmFtZW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=14.99,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish54 = Dish(
    business_id=24,
    name="Spicy Tuna Roll",
    description="Sushi roll with spicy tuna mixture, cucumber, and topped with sesame seeds.",
    image_id="https://images.unsplash.com/photo-1556906905-4f33f9367b6e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8U3BpY3klMjBUdW5hJTIwUm9sbHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=9.50,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "Hard Rock Cafe"
    dish55 = Dish(
    business_id=25,
    name="Classic Cheeseburger",
    description="Juicy beef patty with cheddar cheese, lettuce, and tomato on a toasted bun.",
    image_id="https://images.unsplash.com/photo-1555658094-ca794654362c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Q2xhc3NpYyUyMENoZWVzZWJ1cmdlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
    price=13.50,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish56 = Dish(
    business_id=25,
    name="Veggie Burger",
    description="Plant-based patty with lettuce, tomato, and a vegan mayo dressing.",
    image_id="https://images.unsplash.com/photo-1520072959219-c595dc870360?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8VmVnZ2llJTIwQnVyZ2VyfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=12.00,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "The Garden Club"
    dish57 = Dish(
    business_id=26,
    name="Grilled Chicken Salad",
    description="Grilled chicken breast on a bed of fresh greens with vinaigrette.",
    image_id="https://images.unsplash.com/photo-1625937286074-9ca519d5d9df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fEdyaWxsZWQlMjBDaGlja2VuJTIwU2FsYWR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=10.99,
    category_id=2,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish58 = Dish(
    business_id=26,
    name="Pancake Stack",
    description="Fluffy pancakes served with maple syrup and butter.",
    image_id="https://images.unsplash.com/photo-1619592982310-7b7d51e4207f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8UGFuY2FrZSUyMFN0YWNrfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=8.99,
    category_id=9,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

# Dishes for "The Snug"
    dish59 = Dish(
    business_id=27,
    name="Lobster Roll",
    description="Fresh lobster meat in a creamy mayo dressing on a toasted bun.",
    image_id="https://images.unsplash.com/photo-1511421585906-57a6e6dc3a2f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8TG9ic3RlciUyMFJvbGx8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
    price=19.50,
    category_id=8,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)

    dish60 = Dish(
    business_id=27,
    name="Truffle Fries",
    description="Crispy fries seasoned with truffle oil and parmesan.",
    image_id="https://images.unsplash.com/photo-1579065934361-0a0c8771812a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8VHJ1ZmZsZSUyMEZyaWVzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
    price=7.00,
    category_id=10,
    created_at=datetime.datetime.now(),
    updated_at=datetime.datetime.now()
)


    db.session.add_all([
    dish1, dish2, dish3, dish4, dish5, dish6,
    dish7, dish8, dish9, dish10, dish11, dish12,
    dish13, dish14, dish15, dish16, dish17, dish18,
    dish19, dish20, dish21, dish22, dish23, dish24,
    dish25, dish26, dish27, dish28, dish29, dish30,
    dish31, dish32, dish33, dish34, dish35, dish36,
    dish37, dish38, dish39, dish40, dish41, dish42,
    dish43, dish44, dish45, dish46, dish47, dish48,
    dish49, dish50, dish51, dish52, dish53, dish54,
    dish55, dish56, dish57, dish58, dish59, dish60
    ])

    db.session.commit()

def undo_dishes():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.dishes RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM dishes"))

    db.session.commit()
