# Technology Stack Documentation

This document explains the technical libraries and systems implemented in **SocialPilot**.

---

## 🎨 Frontend Stack

### 1. React.js (v18+)
- **Role**: View Layer.
- **Rationale**: Enables declarative UI building. It manages page states (e.g. modals, tabs, active filters, form validation) efficiently.

### 2. Vite (v6+)
- **Role**: Bundler & Development Server.
- **Rationale**: Offers extremely fast Hot Module Replacement (HMR) and optimized build times compared to legacy bundlers.

### 3. Tailwind CSS (v3+)
- **Role**: Utility-First CSS Framework.
- **Rationale**: Delivers premium glassmorphism layouts, clean spacing, dark/light visual modes, and full desktop/mobile responsive properties.

### 4. Recharts (v2+)
- **Role**: Charting Engine.
- **Rationale**: Renders interactive SVG line graphs, area comparisons, and donut charts reflecting database performance metrics.

### 5. Axios
- **Role**: HTTP client.
- **Rationale**: Simplifies routing to the backend. An Axios interceptor automatically appends the JWT access token from `localStorage` into request headers.

---

## 🐍 Backend Stack

### 1. Python (3.10+)
- **Role**: Runtime Programming Language.

### 2. FastAPI
- **Role**: REST API Service Scaffolding.
- **Rationale**: High-performance HTTP server built on ASGI principles, with self-documenting Swagger OpenAPI generation out of the box.

### 3. SQLAlchemy (v2+)
- **Role**: Object-Relational Mapper (ORM).
- **Rationale**: Provides class mapping to database tables, handling relationships and sanitizing input parameters to block SQL injections.

### 4. SQLite
- **Role**: Database Engine.
- **Rationale**: Zero-configuration, file-based SQLite database for simple local development and offline integration testing.

### 5. Passlib [Bcrypt]
- **Role**: Cryptographic Hashing.
- **Rationale**: Securely salts and hashes passwords before storing them in the DB.

### 6. Python-Jose (JWT)
- **Role**: Bearer Token Signatures.
- **Rationale**: Generates secure JSON Web Tokens containing user sub claims, enforcing session validation across routes.
