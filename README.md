



# 🏋️ My Home Workout — Flask API (Backend)

This is the RESTful API backend for the My Home Workout full-stack application.  
It handles authentication, user data, and workout tracking, and exposes protected endpoints for the React frontend to consume.

---

## 🧰 Tech Stack

| Tool                  | Use Case                      |
| --------------------- | ----------------------------- |
| **Python 3.8+**       | Core language                 |
| **Flask**             | Web framework                 |
| **Flask SQLAlchemy**  | ORM for database models       |
| **Flask-Migrate**     | Database migrations           |
| **Flask-JWT-Extended**| Token-based authentication    |
| **Flask-Bcrypt**      | Secure password hashing       |
| **Flask-CORS**        | Enable frontend connections   |
| **SQLite**            | Lightweight local DB          |
| **Pipenv**            | Dependency management         |

---

## 📁 Folder Structure

```

backend/
├─ app/
│   ├─ **init**.py         ■ App factory, extensions, config
│   ├─ models.py           ■ SQLAlchemy models
│   └─ routes/
│       ├─ **init**.py     ■ Blueprint registration
│       ├─ auth\_routes.py  ■ /register, /login
│       ├─ workout\_routes.py ■ /workouts endpoints
│       └─ user\_routes.py  ■ /profile route
│
├─ seed.py                 ■ Seed file for sample data
├─ run.py                  ■ Entrypoint for running server
├─ Pipfile                 ■ Dependency manifest
├─ Pipfile.lock            ■ Lockfile
└─ .env                    ■ Secrets & DB URI

````

---

## 🧪 Setup Instructions

```bash
# 1. Navigate to backend folder
cd backend

# 2. Create virtual environment + install packages
pipenv install

# 3. Activate the virtual environment
pipenv shell

# 4. Create .env file (see below)

# 5. Initialize the database
pipenv run flask db init
pipenv run flask db migrate -m "Initial migration"
pipenv run flask db upgrade

# 6. Seed the database (optional)
pipenv run python seed.py

# 7. Run the server
pipenv run flask run
````

---

## 🔐 .env Example

Create a `.env` file in the root of the backend folder:

```
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=superjwtsecretkey
DATABASE_URI=sqlite:///workout.db
```

---

## 🔌 API Endpoints

| Method | URL                           | Auth Required? | Description                |
| ------ | ----------------------------- | -------------- | -------------------------- |
| POST   | `/api/register`               | ❌              | Register new user          |
| POST   | `/api/login`                  | ❌              | Login, returns JWT token   |
| GET    | `/api/profile`                | ✅              | Get current user's profile |
| GET    | `/api/workouts`               | ✅              | Fetch all workouts         |
| POST   | `/api/workouts`               | ✅              | Create a new workout       |
| PATCH  | `/api/workouts/<id>/complete` | ✅              | Mark workout as complete   |

---

## 🛠 Example User

To test login on frontend before adding a user:

```json
{
  "email": "test@example.com",
  "password": "password123"
}
```

---

## 📌 Notes

* All JWT-protected routes require the token to be sent in an `Authorization` header like:

  ```
  Authorization: Bearer <your-token>
  ```

* CORS is enabled for all domains by default.

* Passwords are hashed with Bcrypt.

---

## 🧪 Running in Development

```bash
# Start backend API server
pipenv run flask run

# Access the API at:
http://localhost:5000/api/
```

The frontend expects this base URL in its `.env`:

```env
VITE_API_URL=http://localhost:5000/api
```

---

## 🔐 Auth Flow

1. User registers or logs in via frontend.
2. Backend returns JWT.
3. Frontend stores JWT in `localStorage`.
4. All protected requests send token via `Authorization` header.



---

## 🧹 Cleanup

To reset your database:

```bash
rm -rf migrations
rm app/workout.db
pipenv run flask db init
pipenv run flask db migrate -m "Reset"
pipenv run flask db upgrade
```



