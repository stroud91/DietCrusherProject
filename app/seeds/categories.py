from app.models import db, Category, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_categories():
    asian = Category(name='Asian')
    european = Category(name='European')
    vegetarian = Category(name='Vegetarian')
    vegan = Category(name='Vegan')
    gluten_free = Category(name='Gluten-Free')
    seafood = Category(name='Seafood')
    fast_food = Category(name='Fast Food')
    bakery = Category(name='Bakery')
    dessert = Category(name='Dessert')
    drinks = Category(name='Drinks')
    breakfast = Category(name='Breakfast')
    snacks = Category(name='Snacks')
    barbecue = Category(name='Barbecue')
    salads = Category(name='Salads')
    soups = Category(name='Soups')

    db.session.add_all([asian, european, vegetarian, vegan, gluten_free, seafood, fast_food, bakery, dessert, drinks, breakfast, snacks, barbecue, salads, soups])
    db.session.commit()

def undo_categories():
    if environment == "production":
        db.session.execute(text(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;"))
    else:
        db.session.execute(text("DELETE FROM categories"))

    db.session.commit()
