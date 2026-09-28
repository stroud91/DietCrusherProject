import React, { useEffect, useMemo, useRef, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { api } from '../utils/api';
import { loadBusinesses } from '../store/business';
import { useReveal, useDocumentTitle } from '../utils/hooks';
import RestaurantCard from '../components/RestaurantCard';
import { DishTile } from '../components/DishCard';
import { SkeletonGrid } from '../components/ui/States';
import { SearchIcon, ChevronRight, ChevronLeft, TagIcon, BikeIcon, HeartIcon, ClockIcon } from '../components/ui/Icons';
import heroImage from '../images/backgroundImage.jpg';

function Section({ title, subtitle, to, children, className = '' }) {
  const ref = useReveal();
  return (
    <section className={`section reveal ${className}`} ref={ref}>
      <div className="section-head">
        <div>
          <h2>{title}</h2>
          {subtitle && <p className="muted">{subtitle}</p>}
        </div>
        {to && <Link to={to} className="see-all">See all <ChevronRight size={16} /></Link>}
      </div>
      {children}
    </section>
  );
}

function Scroller({ children }) {
  const ref = useRef(null);
  const nudge = (dir) => ref.current && ref.current.scrollBy({ left: dir * ref.current.clientWidth * 0.8, behavior: 'smooth' });
  return (
    <div className="scroller-wrap">
      <button className="scroller-btn left" onClick={() => nudge(-1)} aria-label="Scroll left"><ChevronLeft /></button>
      <div className="scroller" ref={ref}>{children}</div>
      <button className="scroller-btn right" onClick={() => nudge(1)} aria-label="Scroll right"><ChevronRight /></button>
    </div>
  );
}

export default function Home() {
  useDocumentTitle();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const businesses = useSelector((s) => s.business.list);
  const loaded = useSelector((s) => s.business.loaded);
  const [topRated, setTopRated] = useState([]);
  const [topOrdered, setTopOrdered] = useState([]);
  const [promos, setPromos] = useState([]);
  const [q, setQ] = useState('');
  const featuresRef = useReveal();

  useEffect(() => {
    dispatch(loadBusinesses());
    api('/menu/top-rated').then((d) => setTopRated(d.dishes)).catch(() => {});
    api('/menu/top-ordered').then((d) => setTopOrdered(d.dishes)).catch(() => {});
    api('/promos').then((d) => setPromos(d.promos)).catch(() => {});
  }, [dispatch]);

  const cuisines = useMemo(() => {
    const counts = {};
    businesses.forEach((b) => b.cuisines.forEach((c) => { counts[c] = (counts[c] || 0) + 1; }));
    return Object.entries(counts).sort((a, b) => b[1] - a[1]).slice(0, 14).map(([c]) => c);
  }, [businesses]);

  const featured = useMemo(
    () => [...businesses].sort((a, b) => (b.rating || 0) - (a.rating || 0)).slice(0, 8),
    [businesses]
  );

  const submit = (e) => {
    e.preventDefault();
    navigate(q.trim() ? `/search?q=${encodeURIComponent(q.trim())}` : '/all');
  };

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-media" style={{ backgroundImage: `url(${heroImage})` }} aria-hidden="true" />
        <div className="hero-content container">
          <p className="eyebrow">Diet Crusher Delivery</p>
          <h1 className="hero-title">
            Eat well.<br /><span className="gradient-text">Delivered.</span>
          </h1>
          <p className="hero-sub">The best local kitchens, crafted with care and brought to your door in minutes.</p>
          <form className="hero-search" onSubmit={submit} role="search">
            <SearchIcon size={20} />
            <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="What are you craving?" aria-label="Search food" />
            <button className="btn btn-accent">Find food</button>
          </form>
          <div className="hero-stats">
            <span><strong>{businesses.length || '30'}+</strong> restaurants</span>
            <span><strong>25</strong> min average</span>
            <span><strong>4.5★</strong> loved by locals</span>
          </div>
        </div>
      </section>

      <div className="container">
        {cuisines.length > 0 && (
          <div className="chip-row home-chips" aria-label="Cuisines">
            {cuisines.map((c) => (
              <Link key={c} to={`/all?cuisine=${encodeURIComponent(c)}`} className="chip">{c}</Link>
            ))}
          </div>
        )}

        {promos.length > 0 && (
          <Section title="Offers for you" subtitle="Apply at checkout. No strings attached.">
            <div className="promo-grid">
              {promos.map((p, i) => (
                <div key={p.code} className={`promo-card promo-${i % 3}`}>
                  <TagIcon size={22} />
                  <h3>{p.description}</h3>
                  <p>Use code <code>{p.code}</code></p>
                </div>
              ))}
            </div>
          </Section>
        )}

        {topRated.length > 0 && (
          <Section title="Top rated dishes" subtitle="What our community can't stop talking about.">
            <Scroller>
              {topRated.map((d) => <DishTile key={d.id} dish={d} />)}
            </Scroller>
          </Section>
        )}

        <Section title="Featured restaurants" subtitle="Hand-picked by rating." to="/all">
          {loaded ? (
            <div className="card-grid">{featured.map((b) => <RestaurantCard key={b.id} business={b} />)}</div>
          ) : <SkeletonGrid count={8} />}
        </Section>

        {topOrdered.length > 0 && (
          <Section title="Most ordered" subtitle="The dishes everyone's ordering right now.">
            <Scroller>
              {topOrdered.map((d, i) => <DishTile key={d.id} dish={d} badge={i < 3 ? `#${i + 1} most ordered` : null} />)}
            </Scroller>
          </Section>
        )}

        <section className="features reveal" ref={featuresRef}>
          <div className="feature">
            <BikeIcon size={28} />
            <h3>Fast, tracked delivery</h3>
            <p className="muted">Follow every order from the kitchen to your door.</p>
          </div>
          <div className="feature">
            <HeartIcon size={28} />
            <h3>Save your favorites</h3>
            <p className="muted">One tap to keep the places you love close.</p>
          </div>
          <div className="feature">
            <ClockIcon size={28} />
            <h3>Reorder in a tap</h3>
            <p className="muted">Your usual, back in the cart in a second.</p>
          </div>
        </section>
      </div>
    </div>
  );
}
