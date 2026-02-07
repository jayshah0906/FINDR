# 🔐 ParkSmart Authentication System

## Overview

A complete authentication system has been added to the ParkSmart parking prediction application. Users must now register/login to access the parking prediction features.

## 🎨 New Features

### Landing Page
- **Hero Section**: Eye-catching gradient background with animated cards
- **Features Showcase**: 6 feature cards highlighting app capabilities
- **How It Works**: 4-step process visualization
- **Call-to-Action**: Prominent signup buttons throughout
- **Responsive Design**: Mobile-friendly layout
- **Modern Animations**: Smooth transitions and hover effects

### Authentication
- **User Registration**: Email, username, full name, password
- **User Login**: Username/password authentication
- **JWT Tokens**: Secure token-based authentication
- **Protected Routes**: Dashboard only accessible after login
- **Session Management**: Persistent login with localStorage
- **Logout Functionality**: Clean session termination

### User Interface
- **Top Navigation**: User info display with logout button
- **Modern Color Scheme**: Purple/blue gradient theme
- **Professional Design**: Clean, modern interface
- **Smooth Animations**: Enhanced user experience

## 🎨 Color Scheme

The application now uses a modern, professional color palette:

```css
Primary: #6366f1 (Indigo)
Success: #10b981 (Green)  
Warning: #f59e0b (Amber)
Danger: #ef4444 (Red)
Dark: #0f172a (Slate)
Background: #f8fafc (Light Gray)
```

## 📁 New Files Created

### Backend
```
backend/app/models/
  ├── user_model.py           # User database model
  └── auth_schemas.py         # Pydantic schemas for auth

backend/app/routes/
  └── auth_routes.py          # Authentication endpoints

backend/app/services/
  └── auth_service.py         # Auth logic (JWT, password hashing)
```

### Frontend
```
frontend/src/pages/
  ├── LandingPage.jsx         # New landing page component
  └── LandingPage.css         # Landing page styles

frontend/src/components/
  └── ProtectedRoute.jsx      # Route protection wrapper
```

## 🔧 Modified Files

### Backend
- `backend/app/main.py` - Added auth routes
- `backend/requirements.txt` - Added auth dependencies
- `backend/init_db.py` - Added User model import

### Frontend
- `frontend/src/App.jsx` - Added landing page and protected routes
- `frontend/src/pages/MainPage.jsx` - Added navigation and logout
- `frontend/src/pages/MainPage.css` - Updated color scheme

## 🚀 Quick Start

### Option 1: Automated Setup

```bash
./setup_auth.sh
```

### Option 2: Manual Setup

#### Backend
```bash
cd backend
pip install -r requirements.txt
python init_db.py
python run_server.py
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📡 API Endpoints

### Authentication

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "securepass123",
  "full_name": "John Doe"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "johndoe",
    "full_name": "John Doe",
    "created_at": "2026-02-07T10:30:00"
  }
}
```

#### Login User
```http
POST /auth/login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "securepass123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "johndoe",
    "full_name": "John Doe",
    "created_at": "2026-02-07T10:30:00"
  }
}
```

#### Get Current User
```http
GET /auth/me
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...

Response:
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "created_at": "2026-02-07T10:30:00"
}
```

## 🔒 Security Features

### Password Security
- **Bcrypt Hashing**: Passwords are hashed using bcrypt
- **Salt Rounds**: Automatic salt generation
- **No Plain Text**: Passwords never stored in plain text

### Token Security
- **JWT Tokens**: JSON Web Tokens for stateless auth
- **Expiration**: Tokens expire after 7 days
- **Secure Algorithm**: HS256 algorithm

### Validation
- **Email Validation**: Valid email format required
- **Username Length**: 3-50 characters
- **Password Length**: Minimum 6 characters
- **Unique Constraints**: Email and username must be unique

## 🎯 User Flow

1. **Landing Page** → User sees features and benefits
2. **Click "Get Started"** → Auth modal opens
3. **Register/Login** → User creates account or logs in
4. **Redirect to Dashboard** → User accesses parking predictions
5. **Use Application** → Full access to all features
6. **Logout** → Session ends, redirect to landing page

## 📱 Responsive Design

The landing page and dashboard are fully responsive:

- **Desktop**: Full-width layout with side-by-side sections
- **Tablet**: Adjusted grid layouts
- **Mobile**: Stacked layout, simplified navigation

## 🎨 Design Highlights

### Landing Page
- Gradient hero section with animated floating cards
- Feature cards with hover effects
- Step-by-step "How It Works" section
- Prominent call-to-action buttons
- Professional footer

### Dashboard
- Clean top navigation with user info
- Gradient header section
- Modern input cards with focus states
- Color-coded availability indicators
- Smooth transitions and animations

## 🔧 Configuration

### Backend Configuration

Edit `backend/app/services/auth_service.py`:

```python
# Change these for production
SECRET_KEY = "your-secret-key-here"  # Use env variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
```

### Frontend Configuration

Edit `frontend/src/services/api.js` if backend URL changes:

```javascript
const API_URL = 'http://localhost:8001'
```

## 🐛 Troubleshooting

### "Could not validate credentials"
- Token expired or invalid
- Clear localStorage and login again
- Check if backend is running

### "Email already registered"
- Email is already in use
- Use different email or login

### CORS Errors
- Check backend CORS settings
- Ensure frontend URL is allowed
- Verify API_URL in frontend config

### Database Errors
- Run `python init_db.py`
- Check database file exists
- Verify SQLAlchemy models

## 🚀 Production Deployment

### Backend
1. Set `SECRET_KEY` via environment variable
2. Use production database (PostgreSQL recommended)
3. Enable HTTPS
4. Configure CORS for production domain
5. Use Gunicorn/Uvicorn workers

### Frontend
1. Build production bundle: `npm run build`
2. Serve static files via Nginx/Apache
3. Update API_URL to production backend
4. Enable HTTPS
5. Configure CDN for assets

## 📈 Future Enhancements

Potential additions:
- Email verification
- Password reset via email
- OAuth integration (Google, Facebook)
- Two-factor authentication
- User profile page
- Parking history
- Favorite zones
- Email notifications
- User preferences/settings
- Admin dashboard

## 📝 License

MIT License - Built for IITG Hackathon 2026

## 👥 Support

For issues or questions:
1. Check SETUP_INSTRUCTIONS.md
2. Review API documentation at `/docs`
3. Check browser console for errors
4. Verify backend logs
