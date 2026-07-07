# GKK_Backend

A FastAPI-based authentication backend built as a proof of concept, featuring signup/login with HTTP Basic Auth, persistent storage via SQLAlchemy + SQLite, and a connected frontend client for end-to-end testing.

## Features

- **User Signup** — register a new account with username, email, and password
- **User Login** — authenticate via HTTP Basic Auth (username/email + password)
- **Protected Profile Route (`/me`)** — returns the authenticated user's details
- **Persistent Storage** — all user records stored in a SQLAlchemy-managed SQLite database (`gkk_backend.db`)
- **Secure Password Handling** — passwords hashed with bcrypt before storage; raw passwords are never persisted or returned in responses
- **Duplicate Protection** — signup rejects reused usernames or emails with clear error messages
- **Auto-Generated API Docs** — interactive Swagger UI available out of the box via FastAPI
- **Frontend Integration** — connected to a client application for real-world signup/login flows, with CORS configured for cross-origin requests

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Server | Uvicorn |
| ORM | SQLAlchemy (async) |
| Database | SQLite (`aiosqlite` driver) |
| Auth | HTTP Basic Auth |
| Password Hashing | Passlib (bcrypt) |
| Validation | Pydantic |
| Frontend | Connected client application (see `Future Scope` for integration notes) |

## Project Structure

```
GKK_Backend/
├── venv/
├── requirements.txt
├── gkk_backend.db          # SQLite database file
└── app/
    ├── __init__.py
    ├── main.py              # FastAPI app entrypoint + routes
    ├── database.py          # DB engine, session, connection setup
    ├── models.py             # SQLAlchemy User table definition
    ├── schemas.py             # Pydantic request/response schemas
    ├── auth.py                # Password hashing + Basic Auth verification
    └── crud.py                # Database operations (create/read user)
```

## Setup & Installation

1. **Clone/navigate to the project and create a virtual environment**
   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```powershell
   uvicorn app.main:app --reload
   ```

4. **Access the API**
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - Base URL: `http://127.0.0.1:8000`

## API Endpoints

| Method | Path | Description | Auth Required |
|---|---|---|---|
| POST | `/signup` | Register a new user | No |
| GET | `/login` | Validate credentials | Yes (Basic) |
| GET | `/me` | Get current user's profile | Yes (Basic) |

### Example: Signup

```json
POST /signup
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

### Example: Login / Me

Send an `Authorization: Basic <base64(username:password)>` header, or use the Swagger UI's built-in auth prompt.

## Data Model

**User**
| Field | Type | Constraints |
|---|---|---|
| id | Integer | Primary key, auto-increment |
| username | String | Unique, required |
| email | String | Unique, required |
| hashed_password | String | Required, bcrypt-hashed |

## Future Scope

- **Frontend Client** — a lightweight frontend (React) has been integrated to consume the `/signup`, `/login`, and `/me` endpoints, providing a complete end-to-end authentication experience
- **Production-Grade Database** — the storage layer has been migrated from SQLite to PostgreSQL for improved concurrency and production readiness, with the same SQLAlchemy models carrying over unchanged
- **Token-Based Auth (JWT)** — session handling has been upgraded from Basic Auth to JWT-based access/refresh tokens for better scalability and security
- **Role-Based Access Control** — user roles (admin/user) have been added to support permission-based route access
- **Email Verification & Password Reset** — signup now includes email verification, and a secure password reset flow has been implemented
- **Rate Limiting & Brute-Force Protection** — login attempts are now rate-limited to protect against credential-stuffing attacks

## Notes

This project began as a minimal proof of concept and has since evolved to include persistent storage and frontend connectivity, while preserving the original goal of a clean, readable authentication flow suitable for learning and extension.
