# Diet Crusher

**Eat well. Delivered.** Diet Crusher is a full-stack food-delivery app. The storefront is styled after Apple's product pages and the ordering flow follows Uber Eats: browse local kitchens, fill a cart, check out, and track the order live. Restaurant owners get a live order board with sales stats.

Author: **Ledian Fekaj** ([GitHub](https://github.com/stroud91) · [LinkedIn](https://www.linkedin.com/in/ledian-f-47b586143/))

Stack: React 18 · Redux · React Router 6 · Flask 3 · SQLAlchemy 2 · Alembic · PostgreSQL (Render) / SQLite (local)

---

## Features

**Customers**
- Cinematic home page: full-bleed hero, scroll-reveal sections, cuisine chips, promo cards, and scrollers for top-rated and most-ordered dishes
- Browse with cuisine filters, a "Rated 4.5+" toggle, and sorting by recommended, rating, delivery fee, speed, or A–Z
- Live search across restaurants (name, cuisine, city) and dishes, with debouncing
- Restaurant pages with sticky, auto-highlighting menu category tabs, one-tap quick add, Google Maps directions, and share (Web Share API or copy link)
- Dish pages with a quantity stepper, calories, a rating histogram, and reviews (one per user per dish; edit and delete your own)
- Slide-out cart drawer. Carts hold one restaurant at a time; adding from another restaurant asks before starting a new cart
- Checkout with delivery address, courier note, tip presets or a custom tip, and promo codes (`CRUSH10`, `WELCOME5`, `FREEDELIVERY`). The server prices every order
- Order tracking timeline (Placed → Preparing → On the way → Delivered) that refreshes itself, plus cancel (before the kitchen starts) and one-tap reorder
- Favorites (heart any restaurant), an account page (profile, avatar, password change), and light/dark/automatic appearance
- Mobile-first: iOS-style bottom tab bar, bottom-sheet dialogs, safe-area insets, and installable as a PWA

**Restaurant owners**
- Create, edit, and delete restaurants with a live preview, delivery fee, and prep time
- Menu management: add or edit dishes (with calories and category), mark items sold out, delete
- Live order board that refreshes every 15 s, with one-click status advancement
- Stats: revenue, order count, average order value, rating, and best-seller bars

## Security

- Global CSRF protection (double-submit token in the `X-CSRFToken` header) on every write
- Every route checks ownership, so no IDOR: carts, orders, order status, menus, reviews, and favorites
- Businesses are always owned by the logged-in user (client-supplied `owner_id` is ignored)
- Prices, taxes, discounts, and totals are computed on the server; client totals are ignored
- Rate limiting on login, signup, password change, and checkout (Flask-Limiter)
- Login uses one generic error message, so it can't be used to check which emails have accounts
- Passwords require 8+ characters with a letter and a number, and are hashed with Werkzeug
- Public user endpoints never expose email, phone, or address
- Security headers: strict CSP (no inline scripts), HSTS, X-Frame-Options DENY, nosniff, Referrer-Policy, Permissions-Policy, COOP
- Hardened cookies (HttpOnly, Secure, SameSite), HTTPS redirect behind Render's proxy (`ProxyFix`), 1 MB request cap
- Image URLs must be http(s), so `javascript:` and `data:` URLs are rejected
- SQL echo is off in production; `/api/docs` is available in development only; errors never leak stack traces

## Local development

```bash
# Backend (Python 3.11+)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # then set SECRET_KEY
flask db upgrade
flask seed all
flask run                       # http://localhost:5000

# Frontend (Node 18+), in a second terminal
cd react-app
npm install
npm start                       # http://localhost:3000 (proxies /api to Flask)
```

Demo login: `alice@wonderland.ioo` / `passwordAlice` (or click **Explore with the demo account**).

## Deploying to Render (PostgreSQL)

1. Create a **PostgreSQL** instance on Render and copy its *Internal Database URL*.
2. Create a **Web Service** from this repo:
   - **Build command**
     ```
     npm install --prefix react-app && npm run build --prefix react-app && pip install -r requirements.txt && flask db upgrade && flask seed all
     ```
   - **Start command**: `gunicorn app:app`
3. Environment variables:

   | Key | Value |
   | --- | --- |
   | `FLASK_ENV` | `production` |
   | `FLASK_APP` | `app` |
   | `SECRET_KEY` | long random string |
   | `DATABASE_URL` | Render Internal Database URL (`postgres://` is fine) |
   | `SCHEMA` | e.g. `diet_crusher_schema` |

`flask db upgrade` applies only new migrations, so an existing database is upgraded in place. `flask seed all` resets the demo data on each deploy. Python is pinned in `.python-version`, and Node needs version 18 or later.

## API overview

| Area | Endpoints |
| --- | --- |
| Auth | `GET /api/auth/` · `POST /api/auth/login` · `POST /api/auth/signup` · `POST /api/auth/logout` · `PATCH /api/auth/profile` · `POST /api/auth/password` |
| Restaurants | `GET/POST /api/business/` · `GET /api/business/mine` · `GET/PUT/DELETE /api/business/:id` |
| Menu | `GET /api/menu/:id` · `POST /api/menu/business/:id` · `PUT/DELETE /api/menu/:id` · `PATCH /api/menu/:id/availability` · `GET /api/menu/top-rated` · `GET /api/menu/top-ordered` |
| Reviews | `GET /api/review/dish/:id` · `POST /api/review/` · `PUT/DELETE /api/review/:id` |
| Cart | `GET/DELETE /api/cart/` · `POST /api/cart/items` · `PATCH/DELETE /api/cart/items/:id` |
| Orders | `POST /api/orders/quote` · `GET/POST /api/orders/` · `GET /api/orders/:id` · `POST /api/orders/:id/cancel` · `POST /api/orders/:id/reorder` |
| Owner | `GET /api/owner/business/:id/orders` · `GET /api/owner/business/:id/stats` · `PATCH /api/owner/orders/:id/status` |
| Discover | `GET /api/search?q=` · `GET /api/categories` · `GET /api/promos` · `GET/PUT/DELETE /api/favorites/…` |
