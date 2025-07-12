# BlogAPI

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Docs](https://img.shields.io/badge/docs-Swagger/redoc-blue.svg)](https://blogapi-production-82e1.up.railway.app/swagger/)

A **Django REST Framework** API for managing blog posts with JWT authentication, role‑based permissions, and interactive documentation via **Swagger** and **ReDoc**.

## 🚀 Live Demo & Documentation

- **Swagger UI**: https://blogapi-production-82e1.up.railway.app/swagger/  
- **ReDoc**: https://blogapi-production-82e1.up.railway.app/redoc/  

## 🔗 Repository

https://github.com/vyshnavm345/BlogAPI

## 📦 Tech Stack

- **Django** 5.x  
- **Django REST Framework** 3.x  
- **Simple JWT** for token-based auth  
- **drf-yasg** for auto-generated docs  
- **PostgreSQL** (production) / **SQLite** (development)  
- **WhiteNoise** for static file serving  

## 🛠️ Features

- **User registration** with password confirmation  
- **JWT authentication** (`/api/token/`, `/api/token/refresh/`)  
- **Blog Post CRUD** with author-based permissions  
- **Role-based access**: only authors or admins can edit/delete posts  
- **Demonstrated behavior**: multiple users can create posts and list all, but only the post’s author or an admin can update or delete it  
- **Interactive API docs** via Swagger and ReDoc  
- **Admin interface** for manual data management

## 📝 Getting Started

### Prerequisites

- Python 3.10+  
- Git  
- (Optional) PostgreSQL for local testing  

### Local Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/vyshnavm345/BlogAPI.git
   cd BlogAPI
   ```

2. **Create a virtual environment & activate**  
   ```bash
   python3 -m venv env
   source env/bin/activate       # Windows: env\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Copy & configure environment variables**  
   ```bash
   cp .env.example .env
   ```
   Edit `.env` to set `SECRET_KEY`, `DEBUG=True`, `ALLOWED_HOSTS=localhost,127.0.0.1` and optionally `DATABASE_URL`.

5. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**  
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

8. **Access the app**  
   - API root: http://127.0.0.1:8000/api/  
   - Swagger UI: http://127.0.0.1:8000/swagger/  
   - ReDoc: http://127.0.0.1:8000/redoc/  
   - Admin: http://127.0.0.1:8000/admin/

## 🎯 API Endpoints

### Authentication

| Endpoint                   | Method | Description                              |
| -------------------------- | ------ | ---------------------------------------- |
| `/api/register/`           | POST   | Register new user (username, email, password, password2) |
| `/api/token/`              | POST   | Obtain JWT access & refresh tokens       |
| `/api/token/refresh/`      | POST   | Refresh access token using refresh token |

### Blog Posts

| Endpoint                   | Method   | Description                                           |
| -------------------------- | -------- | ----------------------------------------------------- |
| `/api/posts/`              | GET      | List all posts (requires auth)                        |
| `/api/posts/`              | POST     | Create a new post (author set from token)             |
| `/api/posts/{id}/`         | GET      | Retrieve a single post                                |
| `/api/posts/{id}/`         | PATCH    | Partially update a post (author/admin only)           |
| `/api/posts/{id}/`         | DELETE   | Delete a post (author/admin only)                     |

## ⚙️ Deployment

The app is deployed on Railway. To switch to PostgreSQL in production, set the `DATABASE_URL` environment variable in Railway and run migrations via the CLI:  
```bash
railway run python3 manage.py migrate
```

## 📚 License

This project is open‑source under the **MIT License**. See [LICENSE](LICENSE) for details.

---

*Happy coding!*
