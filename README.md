# 🅿️ ParkSmart - Parking Availability Prediction System

An AI-powered system that predicts parking availability across different city zones based on time, location, events, and traffic patterns. **Now with secure user authentication and a professional landing page!**

## ✨ Features

### Core Features
- 🎯 **Zone-based Predictions**: Predict parking availability for specific city zones
- ⏰ **Time-aware**: Considers hour of day, day of week, and special dates
- 🎪 **Event Integration**: Factors in nearby events that affect parking demand
- 🚦 **Traffic Analysis**: Incorporates traffic patterns into predictions
- 📊 **Confidence Scores**: Provides reliability indicators for each prediction
- 🗺️ **Interactive Map**: Visual zone selection interface
- 📱 **Responsive Design**: Works on desktop and mobile devices

### 🆕 New Authentication Features
- 🔐 **Secure Authentication**: JWT token-based user authentication
- 👤 **User Accounts**: Register and login to access predictions
- 🎨 **Modern Landing Page**: Professional hero section with features showcase
- 🛡️ **Protected Routes**: Dashboard only accessible after login
- 💼 **User Management**: Profile display and session management
- 🎨 **New Design**: Modern purple/blue color scheme

## Project Structure

```
├── backend/          # FastAPI backend application
├── frontend/         # React frontend application
├── data/            # Data files (CSV, JSON)
└── docs/            # Documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Option 1: Automated Setup (Recommended)

```bash
./setup_auth.sh
```

### Option 2: Manual Setup

#### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python init_db.py
python run_server.py
```

Backend runs on `http://localhost:8001`

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:5173`

### First Time Usage

1. Open http://localhost:5173
2. Click "Get Started" or "Sign In"
3. Register a new account
4. Start predicting parking availability!

📚 **Need help?** See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) for detailed setup guide.

## 📖 Usage

### Getting Started
1. **Register/Login**: Create an account or sign in
2. **Select Date & Time**: Choose when you need parking
3. **View Map**: See color-coded availability across zones
4. **Select a Zone**: Click on a zone marker or choose from list
5. **View Predictions**: See hourly forecasts with confidence scores
6. **Plan Ahead**: Make informed parking decisions

### User Flow
```
Landing Page → Register/Login → Dashboard → Select Time → Choose Zone → View Predictions
```

## 📡 API Documentation

Once the backend is running, visit:
- **Swagger UI**: `http://localhost:8001/docs`
- **ReDoc**: `http://localhost:8001/redoc`

### 🆕 New Authentication Endpoints
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token
- `GET /auth/me` - Get current user info

### Existing Endpoints
- `GET /zones` - Get all parking zones
- `POST /predict` - Get parking predictions
- `GET /events` - Get events affecting parking

See [API_SPEC.md](docs/API_SPEC.md) and [AUTH_SYSTEM_README.md](AUTH_SYSTEM_README.md) for detailed API documentation.

## 📚 Documentation

### 🆕 Authentication System Documentation
- **[DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)** - Start here! Complete documentation guide
- **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** - Detailed installation and setup
- **[AUTH_SYSTEM_README.md](AUTH_SYSTEM_README.md)** - Complete authentication system docs
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick commands and API reference
- **[VISUAL_GUIDE.md](VISUAL_GUIDE.md)** - UI/UX mockups and design guide
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions
- **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - What was built
- **[BEFORE_AFTER_COMPARISON.md](BEFORE_AFTER_COMPARISON.md)** - See the improvements

### Original Documentation
- [API Specification](docs/API_SPEC.md)
- [Data Format](docs/DATA_FORMAT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Demo Script](docs/DEMO_SCRIPT.md)

## 🛠️ Technology Stack

### Backend
- FastAPI
- SQLAlchemy
- Pydantic
- scikit-learn
- **🆕 JWT Authentication** (python-jose)
- **🆕 Password Hashing** (bcrypt)

### Frontend
- React 18
- Vite
- React Router
- Axios
- Leaflet (Maps)

### Security
- JWT tokens for authentication
- Bcrypt password hashing
- Protected API routes
- Secure session management

## Development

### Running Tests

```bash
cd backend
pytest tests/
```

### Building for Production

```bash
# Frontend
cd frontend
npm run build

# Backend
# Use production ASGI server (Gunicorn + Uvicorn)
```

## 🎨 Screenshots

### Landing Page
- Modern hero section with gradient background
- Features showcase with 6 feature cards
- "How It Works" section
- Professional design with smooth animations

### Dashboard
- Top navigation with user info
- Interactive map with color-coded zones
- Hourly predictions with confidence scores
- Event alerts and traffic information

## 🔐 Security

- **Password Security**: Bcrypt hashing with automatic salt
- **Token Security**: JWT tokens with 7-day expiration
- **Protected Routes**: Authentication required for dashboard
- **Input Validation**: Pydantic schemas for all inputs
- **CORS Configuration**: Secure cross-origin requests

⚠️ **Important**: Change the `SECRET_KEY` in production! See [AUTH_SYSTEM_README.md](AUTH_SYSTEM_README.md) for details.

## 🚀 Deployment

### Production Checklist
- [ ] Set `SECRET_KEY` via environment variable
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Configure production CORS origins
- [ ] Set up monitoring and logging
- [ ] Configure rate limiting
- [ ] Set up automated backups

See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) for detailed deployment guide.

## 🆕 What's New in v2.0

- ✅ Complete authentication system
- ✅ Beautiful landing page
- ✅ User registration and login
- ✅ Protected dashboard routes
- ✅ Modern purple/blue color scheme
- ✅ User profile management
- ✅ Session persistence
- ✅ Comprehensive documentation

See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for complete list of changes.

## 📞 Support

Having issues? Check these resources:
1. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues and solutions
2. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick commands
3. [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) - All documentation
4. API Docs at http://localhost:8001/docs

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [React Documentation](https://react.dev)
- [JWT Introduction](https://jwt.io/introduction)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org)

## 📈 Project Stats

- **Lines of Code**: ~3,200 new lines
- **New Files**: 15 files
- **Documentation**: 8 comprehensive guides
- **Features**: 5 major new features
- **Security**: Production-ready authentication

## 🤝 Contributing

Contributions are welcome! Please read the documentation before contributing.

## 📄 License

MIT License

## 👥 Contributors

Built for IITG Hackathon 2026

---

**Ready to get started?** → [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)

**Need help?** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**Want to learn more?** → [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md)
