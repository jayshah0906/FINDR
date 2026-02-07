# 🚀 Deployment Guide

Complete guide to deploy your AI Parking Prediction System.

---

## 📋 Deployment Options

### Best Combination (Recommended):
- **Frontend:** Vercel (Free, easy, fast)
- **Backend:** Railway or Render (Free tier available)
- **Database:** MongoDB Atlas (Already set up ✅)

---

## 🎯 Quick Deployment (15-20 minutes)

### Option 1: Vercel + Railway (Easiest) ⭐⭐⭐

**Frontend on Vercel:**
1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "New Project"
4. Import your repository
5. Configure:
   - Framework: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
6. Add Environment Variable:
   - `VITE_API_URL` = `https://your-backend-url.railway.app/api/v1`
7. Deploy!

**Backend on Railway:**
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Configure:
   - Root Directory: `backend`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add Environment Variables:
   - `DATABASE_URL` = (your MongoDB Atlas connection string)
   - `USE_ML_MODEL` = `true`
7. Deploy!

---

## 📝 Detailed Step-by-Step Instructions

### Part 1: Deploy Backend (Railway)

#### Step 1: Create Railway Account
```
1. Go to https://railway.app
2. Click "Login" → "Login with GitHub"
3. Authorize Railway
```

#### Step 2: Create New Project
```
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose: AI_BASED_PARKING_AVAILABILITY_PREDICTOR
4. Railway will detect Python automatically
```

#### Step 3: Configure Backend
```
1. Click on your service
2. Go to "Settings" tab
3. Set Root Directory: backend
4. Set Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

#### Step 4: Add Environment Variables
```
1. Go to "Variables" tab
2. Click "New Variable"
3. Add these:

DATABASE_URL = mongodb+srv://parking_admin:YOUR_PASSWORD@cluster-parking-system.uyhmitw.mongodb.net/parking_db?retryWrites=true&w=majority

USE_ML_MODEL = true

PORT = 8001
```

#### Step 5: Deploy
```
1. Railway will auto-deploy
2. Wait 2-3 minutes
3. Get your URL from "Settings" → "Domains"
4. Click "Generate Domain"
5. Your backend URL: https://your-app.railway.app
```

#### Step 6: Test Backend
```bash
# Test health endpoint
curl https://your-app.railway.app/api/v1/health

# Should return: {"status":"healthy",...}
```

---

### Part 2: Deploy Frontend (Vercel)

#### Step 1: Create Vercel Account
```
1. Go to https://vercel.com
2. Click "Sign Up" → "Continue with GitHub"
3. Authorize Vercel
```

#### Step 2: Import Project
```
1. Click "Add New..." → "Project"
2. Import your GitHub repository
3. Vercel will detect Vite automatically
```

#### Step 3: Configure Frontend
```
1. Framework Preset: Vite
2. Root Directory: frontend
3. Build Command: npm run build
4. Output Directory: dist
5. Install Command: npm install
```

#### Step 4: Add Environment Variable
```
1. Click "Environment Variables"
2. Add:
   Key: VITE_API_URL
   Value: https://your-backend.railway.app/api/v1
   
   (Replace with your actual Railway backend URL)
```

#### Step 5: Deploy
```
1. Click "Deploy"
2. Wait 1-2 minutes
3. Your site will be live!
4. URL: https://your-project.vercel.app
```

#### Step 6: Test Frontend
```
1. Visit your Vercel URL
2. Try to register/login
3. Check if predictions work
4. Verify map displays correctly
```

---

## 🔧 Alternative: Render (Both Frontend & Backend)

### Backend on Render

#### Step 1: Create Render Account
```
1. Go to https://render.com
2. Sign up with GitHub
```

#### Step 2: Create Web Service
```
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - Name: parking-backend
   - Root Directory: backend
   - Environment: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

#### Step 3: Add Environment Variables
```
DATABASE_URL = (your MongoDB connection string)
USE_ML_MODEL = true
```

#### Step 4: Deploy
```
1. Click "Create Web Service"
2. Wait 5-10 minutes (first deploy is slow)
3. Get your URL: https://parking-backend.onrender.com
```

### Frontend on Render

#### Step 1: Create Static Site
```
1. Click "New +" → "Static Site"
2. Connect your repository
3. Configure:
   - Name: parking-frontend
   - Root Directory: frontend
   - Build Command: npm run build
   - Publish Directory: dist
```

#### Step 2: Add Environment Variable
```
VITE_API_URL = https://parking-backend.onrender.com/api/v1
```

#### Step 3: Deploy
```
1. Click "Create Static Site"
2. Wait 2-3 minutes
3. Your site: https://parking-frontend.onrender.com
```

---

## ⚠️ Important: Update CORS Settings

After deploying, update your backend CORS settings:

**File:** `backend/app/config.py`

```python
# Add your deployed frontend URL
CORS_ORIGINS: list = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://your-project.vercel.app",  # Add this
    "https://parking-frontend.onrender.com",  # Or this
]
```

**Then commit and push:**
```bash
git add backend/app/config.py
git commit -m "Add production CORS origins"
git push origin main
```

Railway/Render will auto-redeploy.

---

## 🔍 Troubleshooting Deployment

### Backend Issues

**Problem: "Application failed to start"**
```
Solution:
1. Check Railway/Render logs
2. Verify DATABASE_URL is correct
3. Ensure all dependencies in requirements.txt
4. Check Python version (should be 3.9+)
```

**Problem: "Module not found"**
```
Solution:
1. Add missing package to requirements.txt
2. Redeploy
```

**Problem: "Database connection failed"**
```
Solution:
1. Check MongoDB Atlas IP whitelist
2. Add 0.0.0.0/0 to allow all IPs
3. Verify connection string in environment variables
```

### Frontend Issues

**Problem: "API calls failing"**
```
Solution:
1. Check VITE_API_URL is correct
2. Verify backend is running
3. Check CORS settings in backend
4. Test backend URL directly
```

**Problem: "Build failed"**
```
Solution:
1. Check package.json is correct
2. Verify all dependencies are listed
3. Check for syntax errors
4. Try building locally first
```

**Problem: "Environment variable not working"**
```
Solution:
1. Ensure variable starts with VITE_
2. Redeploy after adding variable
3. Check variable is set in Vercel/Render dashboard
```

---

## 📊 Deployment Checklist

### Before Deploying:
- [ ] MongoDB Atlas is set up and accessible
- [ ] Backend runs locally without errors
- [ ] Frontend runs locally without errors
- [ ] All tests passing
- [ ] Environment variables documented

### Backend Deployment:
- [ ] Railway/Render account created
- [ ] Repository connected
- [ ] Environment variables added
- [ ] Backend deployed successfully
- [ ] Health endpoint responding
- [ ] ML model loading correctly

### Frontend Deployment:
- [ ] Vercel/Render account created
- [ ] Repository connected
- [ ] VITE_API_URL configured
- [ ] Frontend deployed successfully
- [ ] Can access landing page
- [ ] API calls working

### Post-Deployment:
- [ ] CORS updated with production URLs
- [ ] Test registration/login
- [ ] Test predictions
- [ ] Test recommendations
- [ ] Verify map displays
- [ ] Check mobile responsiveness

---

## 🎯 Quick Commands Reference

### Test Deployed Backend:
```bash
# Health check
curl https://your-backend.railway.app/api/v1/health

# ML status
curl https://your-backend.railway.app/api/v1/ml-status

# Get zones
curl https://your-backend.railway.app/api/v1/zones
```

### Update Deployment:
```bash
# Just push to GitHub - auto-deploys!
git add .
git commit -m "Update feature"
git push origin main
```

### View Logs:
```
Railway: Dashboard → Your Service → Logs
Render: Dashboard → Your Service → Logs
Vercel: Dashboard → Your Project → Deployments → View Logs
```

---

## 💰 Cost Breakdown

### Free Tier Limits:

**Vercel (Frontend):**
- ✅ Unlimited deployments
- ✅ 100 GB bandwidth/month
- ✅ Custom domain
- ✅ Automatic HTTPS

**Railway (Backend):**
- ✅ $5 free credit/month
- ✅ ~500 hours runtime
- ✅ Automatic HTTPS
- ⚠️  May need to upgrade for 24/7

**Render (Alternative):**
- ✅ Free tier available
- ⚠️  Spins down after 15 min inactivity
- ⚠️  Slow cold starts

**MongoDB Atlas:**
- ✅ 512 MB storage free
- ✅ Shared cluster
- ✅ Already set up

**Total Cost: $0-5/month**

---

## 🚀 After Deployment

### Share Your Live Demo:
```
Frontend: https://your-project.vercel.app
Backend API: https://your-backend.railway.app
API Docs: https://your-backend.railway.app/docs
```

### Update README.md:
Add live demo links to your README:
```markdown
## 🌐 Live Demo

- **Frontend:** https://your-project.vercel.app
- **Backend API:** https://your-backend.railway.app
- **API Docs:** https://your-backend.railway.app/docs
```

### Update Hackathon Submission:
Add your live demo URL to the hackathon submission form!

---

## 📞 Need Help?

**Railway Support:**
- Discord: https://discord.gg/railway
- Docs: https://docs.railway.app

**Vercel Support:**
- Discord: https://vercel.com/discord
- Docs: https://vercel.com/docs

**Render Support:**
- Discord: https://render.com/discord
- Docs: https://render.com/docs

---

**Good luck with deployment! 🚀**
