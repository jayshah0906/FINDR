# 🚀 Render Deployment Guide

Complete step-by-step guide to deploy your project on Render.

---

## 📋 What You'll Deploy

- **Backend:** Python FastAPI app with ML model
- **Frontend:** React + Vite static site
- **Database:** MongoDB Atlas (already set up ✅)

**Total Time:** 15-20 minutes  
**Cost:** FREE (with limitations)

---

## Part 1: Deploy Backend on Render

### Step 1: Create Render Account

1. Go to https://render.com
2. Click **"Get Started"**
3. Sign up with **GitHub**
4. Authorize Render to access your repositories

### Step 2: Create Web Service

1. Click **"New +"** (top right)
2. Select **"Web Service"**
3. Click **"Connect account"** if needed
4. Find and select: **AI_BASED_PARKING_AVAILABILITY_PREDICTOR**
5. Click **"Connect"**

### Step 3: Configure Backend Service

Fill in these settings:

**Basic Settings:**
```
Name: parking-backend
Region: Oregon (US West) or closest to you
Branch: main
Root Directory: backend
```

**Build & Deploy:**
```
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Instance Type:**
```
Select: Free
```

### Step 4: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Add these variables:

```
DATABASE_URL
mongodb+srv://parking_admin:jay123@cluster-parking-system.uyhmitw.mongodb.net/parking_db?retryWrites=true&w=majority

USE_ML_MODEL
true

PYTHON_VERSION
3.11.0
```

### Step 5: Deploy Backend

1. Click **"Create Web Service"**
2. Wait 5-10 minutes (first deploy is slow)
3. Watch the logs for progress
4. Look for: **"Your service is live 🎉"**

### Step 6: Get Backend URL

1. Once deployed, you'll see your URL at the top
2. Copy it: `https://parking-backend-xxxx.onrender.com`
3. Test it: `https://parking-backend-xxxx.onrender.com/api/v1/health`

---

## Part 2: Deploy Frontend on Render

### Step 1: Create Static Site

1. Click **"New +"** (top right)
2. Select **"Static Site"**
3. Select your repository: **AI_BASED_PARKING_AVAILABILITY_PREDICTOR**
4. Click **"Connect"**

### Step 2: Configure Frontend

Fill in these settings:

**Basic Settings:**
```
Name: parking-frontend
Branch: main
Root Directory: frontend
```

**Build Settings:**
```
Build Command: npm install && npm run build
Publish Directory: dist
```

### Step 3: Add Environment Variable

Click **"Advanced"** → **"Add Environment Variable"**

```
VITE_API_URL
https://parking-backend-xxxx.onrender.com/api/v1
```

**⚠️ IMPORTANT:** Replace `parking-backend-xxxx` with YOUR actual backend URL from Part 1!

### Step 4: Deploy Frontend

1. Click **"Create Static Site"**
2. Wait 2-3 minutes
3. Watch the build logs
4. Look for: **"Your site is live 🎉"**

### Step 5: Get Frontend URL

1. Copy your URL: `https://parking-frontend-xxxx.onrender.com`
2. Open it in browser
3. Test the app!

---

## Part 3: Update CORS Settings

### Step 1: Update Backend Config

1. Open `backend/app/config.py` in your code editor
2. Find the `CORS_ORIGINS` list
3. Add your Render frontend URL:

```python
CORS_ORIGINS: list = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://parking-frontend-xxxx.onrender.com",  # Add this line
]
```

### Step 2: Commit and Push

```bash
git add backend/app/config.py
git commit -m "Add Render frontend URL to CORS"
git push origin main
```

### Step 3: Redeploy Backend

1. Go to Render dashboard
2. Click on your backend service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**
4. Wait 2-3 minutes

---

## 🧪 Testing Your Deployment

### Test Backend

```bash
# Health check
curl https://parking-backend-xxxx.onrender.com/api/v1/health

# ML status
curl https://parking-backend-xxxx.onrender.com/api/v1/ml-status

# Get zones
curl https://parking-backend-xxxx.onrender.com/api/v1/zones
```

### Test Frontend

1. Open: `https://parking-frontend-xxxx.onrender.com`
2. Try to register a new account
3. Login with your account
4. Select a zone and get predictions
5. Check if recommendations work
6. Verify map displays correctly

---

## ⚠️ Important Notes About Render Free Tier

### Backend (Web Service):
- ✅ Free for 750 hours/month
- ⚠️ **Spins down after 15 minutes of inactivity**
- ⚠️ **Cold start takes 30-60 seconds**
- ⚠️ Limited to 512 MB RAM
- ⚠️ ML model (103 MB) might cause issues

### Frontend (Static Site):
- ✅ Completely free
- ✅ Always on (no spin down)
- ✅ Fast CDN delivery
- ✅ Automatic HTTPS

### Solutions for Backend Limitations:

**Option 1: Keep Backend Warm**
- Use a service like UptimeRobot to ping your backend every 10 minutes
- Free tier: https://uptimerobot.com

**Option 2: Deploy ML Model Separately**
- Set `USE_ML_MODEL=false` for faster cold starts
- Use fallback predictions

**Option 3: Upgrade to Paid Plan**
- $7/month for always-on backend
- No cold starts
- More RAM for ML model

---

## 🔧 Troubleshooting

### Backend Issues

**Problem: "Build failed"**
```
Solution:
1. Check Render logs for specific error
2. Verify requirements.txt is correct
3. Check Python version is 3.11
4. Ensure Root Directory is set to "backend"
```

**Problem: "Out of memory"**
```
Solution:
1. ML model (103 MB) might be too large for free tier
2. Set USE_ML_MODEL=false
3. Or upgrade to paid plan ($7/month)
```

**Problem: "Service unavailable" or slow**
```
Solution:
1. This is normal for free tier (cold start)
2. Wait 30-60 seconds and try again
3. Use UptimeRobot to keep it warm
4. Or upgrade to paid plan
```

**Problem: "Database connection failed"**
```
Solution:
1. Check DATABASE_URL is correct
2. Go to MongoDB Atlas
3. Network Access → Add IP: 0.0.0.0/0
4. Verify connection string has correct password
```

### Frontend Issues

**Problem: "Build failed"**
```
Solution:
1. Check build logs for specific error
2. Verify package.json is correct
3. Ensure Root Directory is set to "frontend"
4. Check Build Command: npm install && npm run build
5. Check Publish Directory: dist
```

**Problem: "API calls failing"**
```
Solution:
1. Check VITE_API_URL is correct
2. Verify backend is running (not spun down)
3. Check CORS settings in backend
4. Test backend URL directly
```

**Problem: "Environment variable not working"**
```
Solution:
1. Ensure variable is named VITE_API_URL (must start with VITE_)
2. Redeploy after adding variable
3. Clear browser cache
4. Check variable in Render dashboard
```

---

## 📊 Deployment Checklist

### Before Deploying:
- [x] MongoDB Atlas is set up
- [x] Backend runs locally
- [x] Frontend runs locally
- [x] requirements.txt updated with pydantic[email]
- [x] All tests passing

### Backend Deployment:
- [ ] Render account created
- [ ] Web Service created
- [ ] Root Directory: backend
- [ ] Build Command: pip install -r requirements.txt
- [ ] Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
- [ ] Environment variables added
- [ ] Backend deployed successfully
- [ ] Health endpoint responding

### Frontend Deployment:
- [ ] Static Site created
- [ ] Root Directory: frontend
- [ ] Build Command: npm install && npm run build
- [ ] Publish Directory: dist
- [ ] VITE_API_URL configured
- [ ] Frontend deployed successfully
- [ ] Can access landing page

### Post-Deployment:
- [ ] CORS updated with Render frontend URL
- [ ] Backend redeployed
- [ ] Test registration/login
- [ ] Test predictions
- [ ] Test recommendations
- [ ] Verify map displays

---

## 🎯 Your Live URLs

After deployment, you'll have:

```
Frontend: https://parking-frontend-xxxx.onrender.com
Backend: https://parking-backend-xxxx.onrender.com
API Docs: https://parking-backend-xxxx.onrender.com/docs
```

**Add these to your hackathon submission!**

---

## 📝 Update README.md

Add your live demo links to README:

```markdown
## 🌐 Live Demo

- **Frontend:** https://parking-frontend-xxxx.onrender.com
- **Backend API:** https://parking-backend-xxxx.onrender.com
- **API Docs:** https://parking-backend-xxxx.onrender.com/docs

**Note:** Backend may take 30-60 seconds to wake up on first request (free tier limitation).
```

---

## 🆘 Need Help?

**Render Support:**
- Discord: https://render.com/discord
- Docs: https://render.com/docs
- Community: https://community.render.com

**Common Issues:**
- Backend slow/unavailable → Normal for free tier (cold start)
- Out of memory → ML model too large, set USE_ML_MODEL=false
- CORS errors → Update CORS_ORIGINS in backend/app/config.py

---

## 💡 Pro Tips

1. **Keep Backend Warm:**
   - Use UptimeRobot to ping every 10 minutes
   - Prevents cold starts

2. **Monitor Deployments:**
   - Check Render dashboard regularly
   - Watch logs for errors

3. **Test Before Submitting:**
   - Test all features on live site
   - Check mobile responsiveness
   - Verify predictions work

4. **Backup Plan:**
   - If backend is too slow, mention it's free tier
   - Provide local setup instructions
   - Record demo video as backup

---

**Good luck with your deployment! 🚀**
