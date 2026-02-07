#!/bin/bash

echo "🚀 Setting up ParkSmart Authentication System"
echo "=============================================="
echo ""

# Backend setup
echo "📦 Installing backend dependencies..."
cd backend
pip install python-jose[cryptography] passlib[bcrypt] python-dotenv
echo "✅ Backend dependencies installed"
echo ""

# Initialize database
echo "🗄️  Initializing database with user table..."
python init_db.py
echo "✅ Database initialized"
echo ""

# Frontend setup
echo "📦 Installing frontend dependencies..."
cd ../frontend
npm install
echo "✅ Frontend dependencies installed"
echo ""

echo "=============================================="
echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  python run_server.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  npm run dev"
echo ""
echo "Then open: http://localhost:5173"
echo "=============================================="
