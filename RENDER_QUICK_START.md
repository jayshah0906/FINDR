# 🚀 Render Quick Start (10 Minutes)

## Step 1: Deploy Backend (5 min)

1. Go to https://render.com → Sign up with GitHub
2. New + → Web Service → Select your repo
3. Configure:
   ```
   Name: parking-backend
   Root Directory: backend
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
4. Add Environment Variables:
   ```
   DATABASE_URL = mongodb+srv://parking_admin:jay123@cluster-parking-system.uyhmitw.mongodb.net/parking_db?retryWrites=true&w=majority
   USE_ML_MODEL = true
   PYTHON_VERSION = 3.11.0
   ```
5. Create Web Service → Wait 5-10 min
6. Copy your backend URL: `https://parking-backend-xxxx.onrender.com`

---

## Step 2: Deploy Frontend (3 min)

1. New + → Static Site → Select your repo
2. Configure:
   ```
   Name: parking-frontend
   Root Directory: frontend
   Build Command: npm install && npm run build
   Publish Directory: dist
   ```
3. Add Environment Variable:
   ```
   VITE_API_URL = https://parking-backend-xxxx.onrender.com/api/v1
   ```
   (Use YOUR backend URL from Step 1!)
4. Create Static Site → Wait 2-3 min
5. Copy your frontend URL: `https://parking-frontend-xxxx.onrender.com`

---

## Step 3: Update CORS (2 min)

1. Edit `backend/app/config.py`:
   ```python
   CORS_ORIGINS: list = [
       "http://localhost:5173",
       "https://parking-frontend-xxxx.onrender.com",  # Add this
   ]
   ```
2. Commit and push:
   ```bash
   git add backend/app/config.py
   git commit -m "Add Render CORS origin"
   git push origin main
   ```
3. In Render dashboard → Backend service → Manual Deploy

---

## Step 4: Test (2 min)

1. Open your frontend URL
2. Register/Login
3. Test predictions
4. Done! 🎉

---

## ⚠️ Important Notes

**Free Tier Limitations:**
- Backend spins down after 15 min inactivity
- First request takes 30-60 seconds (cold start)
- This is NORMAL for free tier

**If Backend is Slow:**
- Wait 60 seconds on first load
- Use UptimeRobot to keep it warm (free)
- Or upgrade to $7/month for always-on

---

## 🎯 Your Live URLs

```
Frontend: https://parking-frontend-xxxx.onrender.com
Backend: https://parking-backend-xxxx.onrender.com
API Docs: https://parking-backend-xxxx.onrender.com/docs
```

**Add these to your hackathon submission!**

---

For detailed instructions, see: **RENDER_DEPLOYMENT_GUIDE.md**
