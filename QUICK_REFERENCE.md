# 🚀 Quick Reference - ParkSmart Auth System

## Installation Commands

```bash
# Backend
cd backend
pip install -r requirements.txt
python init_db.py
python run_server.py

# Frontend  
cd frontend
npm install
npm run dev
```

## URLs

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8001
- **API Docs**: http://localhost:8001/docs

## Test Credentials

Create your own via the registration form, or use API:

```bash
curl -X POST http://localhost:8001/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "test123",
    "full_name": "Test User"
  }'
```

## API Quick Reference

### Register
```bash
POST /auth/register
{
  "email": "user@example.com",
  "username": "username",
  "password": "password",
  "full_name": "Full Name"
}
```

### Login
```bash
POST /auth/login
{
  "username": "username",
  "password": "password"
}
```

### Get User Info
```bash
GET /auth/me
Authorization: Bearer <token>
```

### Get Zones
```bash
GET /zones
```

### Predict Parking
```bash
POST /predict
{
  "zone_id": 1,
  "date": "2026-02-07",
  "hour": 14,
  "day_of_week": 4
}
```

## File Structure

```
backend/
├── app/
│   ├── models/
│   │   ├── user_model.py          # NEW
│   │   └── auth_schemas.py        # NEW
│   ├── routes/
│   │   └── auth_routes.py         # NEW
│   ├── services/
│   │   └── auth_service.py        # NEW
│   └── main.py                    # MODIFIED
├── requirements.txt               # MODIFIED
└── init_db.py                     # MODIFIED

frontend/
├── src/
│   ├── pages/
│   │   ├── LandingPage.jsx        # NEW
│   │   ├── LandingPage.css        # NEW
│   │   ├── MainPage.jsx           # MODIFIED
│   │   └── MainPage.css           # MODIFIED
│   ├── components/
│   │   └── ProtectedRoute.jsx     # NEW
│   └── App.jsx                    # MODIFIED
```

## Key Components

### Backend

**User Model** (`user_model.py`)
- id, email, username, hashed_password, full_name
- created_at, updated_at

**Auth Service** (`auth_service.py`)
- Password hashing (bcrypt)
- JWT token generation
- User authentication

**Auth Routes** (`auth_routes.py`)
- POST /auth/register
- POST /auth/login
- GET /auth/me

### Frontend

**LandingPage** (`LandingPage.jsx`)
- Hero section
- Features showcase
- Auth modal
- Registration/Login forms

**ProtectedRoute** (`ProtectedRoute.jsx`)
- Checks for token
- Redirects to landing if not authenticated

**MainPage** (`MainPage.jsx`)
- Top navigation with user info
- Logout functionality
- Parking prediction interface

## Environment Variables

### Backend (Production)

Create `.env` file:
```env
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/dbname
CORS_ORIGINS=https://yourdomain.com
```

Update `auth_service.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
```

## Common Issues & Fixes

### Issue: CORS Error
**Fix**: Check `backend/app/middleware/cors.py`
```python
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    # Add your production domain
]
```

### Issue: Token Invalid
**Fix**: Clear localStorage and login again
```javascript
localStorage.clear()
```

### Issue: Database Error
**Fix**: Reinitialize database
```bash
cd backend
rm parking_prediction.db
python init_db.py
python scripts/seed_zones.py
```

### Issue: Module Not Found
**Fix**: Install dependencies
```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

## Testing Checklist

- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Landing page loads
- [ ] Can open auth modal
- [ ] Can register new user
- [ ] Redirects to dashboard after registration
- [ ] Can logout
- [ ] Can login with existing credentials
- [ ] Protected routes work (redirect if not logged in)
- [ ] User info displays in navigation
- [ ] Can select date and time
- [ ] Map loads correctly
- [ ] Can select zone
- [ ] Predictions load
- [ ] Color scheme is correct

## Color Reference

```css
--primary: #6366f1        /* Buttons, links */
--success: #10b981        /* High availability */
--warning: #f59e0b        /* Medium availability */
--danger: #ef4444         /* Low availability */
--dark: #0f172a           /* Text */
--bg: #f8fafc             /* Background */
```

## Dependencies Added

### Backend
- `python-jose[cryptography]` - JWT tokens
- `passlib[bcrypt]` - Password hashing
- `python-dotenv` - Environment variables

### Frontend
- No new dependencies (uses existing React Router)

## Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Use environment variables
- [ ] Enable HTTPS in production
- [ ] Set secure CORS origins
- [ ] Use strong passwords (min 6 chars)
- [ ] Validate all inputs
- [ ] Sanitize user data
- [ ] Set token expiration
- [ ] Implement rate limiting (future)
- [ ] Add CSRF protection (future)

## Performance Tips

### Backend
- Use connection pooling
- Add caching for zones
- Optimize database queries
- Use async endpoints

### Frontend
- Lazy load components
- Optimize images
- Use React.memo for expensive components
- Implement virtual scrolling for long lists

## Deployment Checklist

### Backend
- [ ] Set SECRET_KEY via env variable
- [ ] Use production database
- [ ] Configure CORS for production domain
- [ ] Enable HTTPS
- [ ] Set up logging
- [ ] Configure Gunicorn/Uvicorn
- [ ] Set up monitoring

### Frontend
- [ ] Build production bundle
- [ ] Update API_URL
- [ ] Configure CDN
- [ ] Enable HTTPS
- [ ] Optimize assets
- [ ] Set up error tracking
- [ ] Configure analytics

## Useful Commands

### Backend
```bash
# Run server
python run_server.py

# Initialize DB
python init_db.py

# Seed zones
python scripts/seed_zones.py

# Run tests
pytest tests/
```

### Frontend
```bash
# Development
npm run dev

# Build
npm run build

# Preview build
npm run preview

# Lint
npm run lint
```

### Database
```bash
# View database
sqlite3 backend/parking_prediction.db

# List tables
.tables

# View users
SELECT * FROM users;

# Exit
.quit
```

## Support Resources

- **Setup Guide**: SETUP_INSTRUCTIONS.md
- **Full Documentation**: AUTH_SYSTEM_README.md
- **Visual Guide**: VISUAL_GUIDE.md
- **API Docs**: http://localhost:8001/docs

## Quick Debug

```bash
# Check if backend is running
curl http://localhost:8001/

# Check if frontend is running
curl http://localhost:5173/

# Test registration
curl -X POST http://localhost:8001/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","username":"test","password":"test123"}'

# Test login
curl -X POST http://localhost:8001/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'
```

---

**Need Help?** Check the full documentation files or API docs at `/docs`
