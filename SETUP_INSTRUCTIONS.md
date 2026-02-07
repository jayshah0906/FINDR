# Setup Instructions for Authentication System

## Backend Setup

### 1. Install New Dependencies

```bash
cd backend
pip install python-jose[cryptography] passlib[bcrypt] python-dotenv
```

Or install all requirements:

```bash
pip install -r requirements.txt
```

### 2. Initialize Database with User Table

```bash
python init_db.py
```

This will create the `users` table in your database.

### 3. Run the Backend Server

```bash
python run_server.py
```

The API will be available at: http://localhost:8001

## Frontend Setup

### 1. Install Dependencies (if not already done)

```bash
cd frontend
npm install
```

### 2. Run the Frontend

```bash
npm run dev
```

The frontend will be available at: http://localhost:5173

## Testing the Authentication

### 1. Open the Landing Page

Navigate to: http://localhost:5173

### 2. Register a New User

- Click "Get Started" or "Sign In" button
- Click "Sign Up" in the modal
- Fill in:
  - Full Name: Your Name
  - Email: your@email.com
  - Username: yourusername
  - Password: yourpassword (min 6 characters)
- Click "Create Account"

### 3. You'll be automatically logged in and redirected to the dashboard

### 4. Test Logout

- Click the "Logout" button in the top right
- You'll be redirected back to the landing page

### 5. Test Login

- Click "Sign In"
- Enter your username and password
- Click "Sign In"

## API Endpoints

### Authentication Endpoints

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user info (requires authentication)

### Existing Endpoints

- `GET /zones` - Get all parking zones
- `POST /predict` - Get parking prediction
- `GET /events` - Get events

## Features Implemented

### Backend
✅ User registration with email validation
✅ Secure password hashing (bcrypt)
✅ JWT token authentication
✅ Protected routes
✅ User model with SQLAlchemy

### Frontend
✅ Beautiful landing page with hero section
✅ Features showcase
✅ How it works section
✅ Authentication modal (login/register)
✅ Protected routes (requires login)
✅ User info display in navigation
✅ Logout functionality
✅ Modern purple/blue color scheme
✅ Responsive design
✅ Smooth animations

## Security Notes

⚠️ **IMPORTANT**: Change the `SECRET_KEY` in `backend/app/services/auth_service.py` before deploying to production!

Current key is for development only:
```python
SECRET_KEY = "your-secret-key-change-this-in-production-use-env-variable"
```

For production, use environment variables:
```python
import os
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-key")
```

## Troubleshooting

### Issue: "Could not validate credentials"
- Make sure you're logged in
- Check if token is stored in localStorage
- Try logging out and logging in again

### Issue: "Email already registered"
- Use a different email address
- Or login with existing credentials

### Issue: Backend connection error
- Make sure backend is running on port 8001
- Check CORS settings in `backend/app/middleware/cors.py`

### Issue: Database error
- Run `python init_db.py` to create tables
- Check if `parking_prediction.db` exists

## Color Scheme

The new color scheme uses modern, professional colors:

- **Primary**: #6366f1 (Indigo)
- **Success**: #10b981 (Green)
- **Warning**: #f59e0b (Amber)
- **Danger**: #ef4444 (Red)
- **Dark**: #0f172a (Slate)
- **Background**: #f8fafc (Light Gray)

## Next Steps

You can now:
1. Customize the landing page content
2. Add more user profile features
3. Implement password reset
4. Add email verification
5. Create user preferences/settings
6. Add user parking history
7. Implement favorites/saved zones
