# 🚀 Quick Deployment Checklist

## Step 1: Deploy Backend (Railway) - 5 minutes

1. Go to https://railway.app
2. Login with GitHub
3. New Project → Deploy from GitHub repo
4. Select your repository
5. Add Environment Variables:
   ```
   DATABASE_URL = mongodb+srv://parking_admin:jay123@cluster-parking-system.uyhmitw.mongodb.net/parking_db?retryWrites=true&w=majority
   USE_ML_MODEL = true
   ```
6. Settings → Root Directory: `backend`
7. Settings → Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
8. Generate Domain → Copy your backend URL

**Your Backend URL:** `https://__________.railway.app`

---

## Step 2: Deploy Frontend (Vercel) - 5 minutes

1. Go to https://vercel.com
2. Login with GitHub
3. New Project → Import your repository
4. Root Directory: `frontend`
5. Framework: Vite
6. Add Environment Variable:
   ```
   VITE_API_URL = https://your-backend.railway.app/api/v1
   ```
   (Replace with your actual Railway URL from Step 1)
7. Deploy!

**Your Frontend URL:** `https://__________.vercel.app`

---

## Step 3: Update CORS - 2 minutes

1. Edit `backend/app/config.py`
2. Add your Vercel URL to CORS_ORIGINS:
   ```python
   CORS_ORIGINS: list = [
       "http://localhost:5173",
       "https://your-project.vercel.app",  # Add this line
   ]
   ```
3. Commit and push:
   ```bash
   git add backend/app/config.py
   git commit -m "Add production CORS origin"
   git push origin main
   ```
4. Railway will auto-redeploy

---

## Step 4: Test Your Deployment - 2 minutes

1. Visit your Vercel URL
2. Try to register a new account
3. Login
4. Check if predictions work
5. Verify map displays

---

## ✅ Done!

**Live Demo URLs:**
- Frontend: https://__________.vercel.app
- Backend: https://__________.railway.app
- API Docs: https://__________.railway.app/docs

**Add these to your hackathon submission!**

---

## 🆘 If Something Goes Wrong

**Backend not starting:**
- Check Railway logs
- Verify DATABASE_URL is correct
- Check MongoDB Atlas IP whitelist (add 0.0.0.0/0)

**Frontend can't connect to backend:**
- Verify VITE_API_URL is correct
- Check CORS settings
- Test backend URL directly

**Need help?** See DEPLOYMENT_GUIDE.md for detailed instructions.
