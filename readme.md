# 🔗 FastAPI URL Shortener

A modern, scalable, and secure URL shortener built with FastAPI, MongoDB, Redis, and Docker. This service allows you to shorten URLs with optional user authentication, custom aliases, usage analytics, and caching for optimal performance.

## 🚀 Features

- ✅ Shorten any valid URL
- 🔐 Optional user authentication (OAuth2/JWT)
- ✏️ Custom aliases for your short links
- ⚡ Redis caching for fast redirects
- 🐳 Dockerized for easy deployment

## 📦 Tech Stack

- **FastAPI** – Web framework
- **MongoDB** – Database for storing URLs
- **Redis** – Caching layer for performance
- **Pydantic** – Data validation
- **JWT / OAuth2** – Authentication
- **Docker** – Containerized app

## 📁 Project Structure

```
fastapi-url-shortener/
│
├── deploy/
│   ├── app/                   # Application source code
│   │   ├── controllers/       # Route handlers
│   │   ├── core/              # Configuration & DB setup
│   │   ├── models/            # Pydantic and MongoDB models
│   │   ├── routes/            # FastAPI routers
│   │   ├── schemas/           # Request/Response schemas
│   │   ├── services/          # Business logic
│   │   ├── utils/             # Utility functions
│   │   ├── __init__.py
│   │   └── main.py            # Entry point
│   │
│   ├── Dockerfile             # Docker build instructions
│   ├── docker-compose.yml     # Multi-container setup
│   └── requirements.txt       # Python dependencies
│
└── env/                       # Environment variables
```

## 🏁 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-url-shortener.git
cd fastapi-url-shortener
```

### 2. Set up environment variables

Create a `.env` file in the `env/` directory and configure the following:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
MONGO_URI=mongodb://mongo:27017
REDIS_URL=redis://redis:6379
REDIS_PASSWORD=your-redis-password
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

For Redis Cloud, use the provided URL with username and password. The REDIS_PASSWORD is required when using Redis Cloud as a service.

### 3. Run with Docker

Navigate to the `deploy/` directory and run:

```bash
cd deploy
docker-compose up --build
```

The application will be available at: http://localhost:8000/docs

## 🐳 Docker Setup

This project uses Docker Compose to run:

- FastAPI app on port 8000
- MongoDB on port 27017
- Redis on port 6379

You can inspect the full setup in `deploy/docker-compose.yml`.

## 📌 API Endpoints

| Method | Endpoint             | Description                  | Auth Required |
|--------|----------------------|------------------------------|--------------|
| POST   | /v1/shorten          | Shorten URL (unauthenticated)| ❌           |
| POST   | /v2/shorten          | Shorten URL (authenticated)  | ✅           |
| GET    | /{short_hash}        | Redirect to original URL     | ❌           |
| POST   | /api/auth/register   | Register a new user          | ❌           |
| POST   | /api/auth/login      | Login and get access token   | ❌           |




## 🛠️ Development

### Running with Docker (Recommended)

The recommended way to run this application is using Docker, which takes care of all dependencies and services:

1. Make sure Docker and Docker Compose are installed on your system
2. Navigate to the deploy directory:
```bash
cd deploy
```
3. Build and start the containers:
```bash
docker-compose up --build
```

This will start the FastAPI application, MongoDB, and Redis all configured to work together.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Charles

Built with ❤️ using FastAPI

## 🔗 Demo

https://fastapi-url-shortener-i8ag.onrender.com/redoc