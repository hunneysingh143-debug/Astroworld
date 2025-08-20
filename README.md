# Jyotish Desktop (Electron + React) — Parashara-class Scaffold

This is an MVP scaffold to build a desktop astrology suite with feature parity goals similar to Parashara’s Light 9.0 (without copying proprietary content).

## Features (MVP)
- Electron + React shell (Dashboard, Charts, Panchang, Dashas, Reports)
- SQLite (better-sqlite3) for chart storage
- SVG chart renderer scaffold (North-Indian style boxes)
- IPC wiring for future PDF export

## Roadmap to Parity
1. **Astronomy & Ephemeris**
   - Use [`astronomia`](https://github.com/commenthol/astronomia) or Swiss Ephemeris (optional, via `swisseph`) for planetary longitudes.
   - Implement ayanamsa (Lahiri default).
2. **Core Jyotish**
   - Rashis, Nakshatras, Bhavas with multiple house systems.
   - Shadbala, Ashtakavarga.
   - Yogas (catalog + detector).
   - Vimshottari, Yogini, Ashtottari, Kalachakra Dashas.
3. **Utilities**
   - Panchang (Tithi, Nakshatra, Yoga, Karana; Sunrise/Sunset).
   - Muhurta, Match-making (Guna Milan), Varshaphala.
4. **UX & Reports**
   - North & South Indian charts, Divisional charts (D1..D60).
   - Multi-language reports (Hindi/English), PDF export via Puppeteer.

## Dev Scripts
```bash
npm i
npm run dev
# In dev: Vite (React) runs on :5173 and Electron loads it.
npm run build  # bundles renderer and builds installers via electron-builder
```

## Notes
- Swiss Ephemeris provides high-precision results but needs native binaries and a license for redistribution. Use at your discretion.
- Do **not** use the name “Parashara’s Light” in your product branding; it is a registered trademark. This project only targets open re-implementation of publicly described features.
