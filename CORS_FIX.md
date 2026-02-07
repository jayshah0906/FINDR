# 🔧 CORS Fix - "Failed to Fetch" Error

## Problem
Your frontend can't connect to backend due to CORS (Cross-Origin Resource Sharing) restrictions.

---

## Quick Fix (2 minutes)

### Step 1: Get Your URLs

**Frontend URL:** `https://your-frontend.onrender.com`  
**Backend URL:** `https://your-backend.onrender.com`

### Step 2: Update CORS Settings

1. Open `backend/app/config.py`
2. Find the `CORS_ORIGINS` list (around line 70)
3. Add your Render frontend URL:

```python
# CORS Settings
CORS_ORIGINS: list = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:8080",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "https://your-frontend.onrender.com",  # ADD THIS LINE
]
```

**⚠️ IMPORTANT:** Replace `your-frontend.onrender.com` with YOUR actual Render frontend URL!

### Step 3: Commit and Push

```bash
git add backend/app/config.py
git commit -m "Add Render frontend URL to CORS"
git push origin main
```

### Step 4: Wait for Redeploy

- Render will automatically redeploy your backend (2-3 minutes)
- Watch the deployment in Render dashboard
- Wait for "Your service is live 🎉"

### Step 5: Test Again

1. Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Go to your frontend URL
3. Try signup again
4. Should work now! ✅

---

## Alternative: Allow All Origins (Quick Test Only)

**⚠️ NOT RECOMMENDED FOR PRODUCTION**

For quick testing, you can temporarily allow all origins:

```python
# CORS Settings
CORS_ORIGINS: list = ["*"]  # Allows all origins
```

This will work immediately but is NOT secure for production!

---

## Other Possible Issues

### Issue 1: Wrong Backend URL in Frontend

**Check:** Frontend environment variable

1. Go to Render dashboard → Your frontend service
2. Click "Environment" tab
3. Check `VITE_API_URL` value
4. Should be: `https://your-backend.onrender.com/api/v1`
5. If wrong, update it and redeploy

### Issue 2: Backend Not Running

**Check:** Backend status

1. Go to Render dashboard → Your backend service
2. Check if it says "Live"
3. If not, check logs for errors
4. Try manual deploy

**Test backend directly:**
```bash
curl https://your-backend.onrender.com/api/v1/health
```

Should return: `{"status":"healthy",...}`

### Issue 3: Backend Cold Start

**Symptom:** First request fails, second works

**Solution:** This is normal for Render free tier
- Backend spins down after 15 min
- First request wakes it up (30-60 seconds)
- Just wait and try again

### Issue 4: MongoDB Connection

**Check:** Database connection

1. Go to MongoDB Atlas
2. Network Access → Check IP whitelist
3. Should include: `0.0.0.0/0` (allow all)
4. If not, add it

---

## Debugging Steps

### 1. Check Browser Console

1. Open your frontend in browser
2. Press F12 (Developer Tools)
3. Go to "Console" tab
4. Try signup again
5. Look for error messages

**Common errors:**
- `CORS policy: No 'Access-Control-Allow-Origin'` → CORS issue (follow fix above)
- `net::ERR_CONNECTION_REFUSED` → Backend not running
- `Failed to fetch` → CORS or backend URL wrong

### 2. Check Network Tab

1. In Developer Tools, go to "Network" tab
2. Try signup again
3. Look for the request to `/api/v1/auth/register`
4. Click on it to see details

**Check:**
- Request URL: Should be your backend URL
- Status: Should be 200 or 201
- Response: Should have user data

### 3. Test Backend Directly

```bash
# Test health
curl https://your-backend.onrender.com/api/v1/health

# Test registration (replace with your backend URL)
curl -X POST https://your-backend.onrender.com/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "password123",
    "full_name": "Test User"
  }'
```

---

## Complete Checklist

- [ ] Frontend URL added to CORS_ORIGINS in backend/app/config.py
- [ ] Changes committed and pushed to GitHub
- [ ] Backend redeployed on Render
- [ ] VITE_API_URL is correct in frontend environment variables
- [ ] Backend is live and responding to /health endpoint
- [ ] MongoDB Atlas allows connections from 0.0.0.0/0
- [ ] Browser cache cleared
- [ ] Tested signup again

---

## Still Not Working?

### Share These Details:

1. **Frontend URL:** `https://_____.onrender.com`
2. **Backend URL:** `https://_____.onrender.com`
3. **Browser Console Error:** (screenshot or copy error message)
4. **Backend Logs:** (from Render dashboard)

### Quick Test:

Try this in browser console (F12):
```javascript
fetch('https://your-backend.onrender.com/api/v1/health')
  .then(r => r.json())
  .then(d => console.log(d))
  .catch(e => console.error(e))
```

Replace with your backend URL and see what error you get.

---

## Most Common Solution

**99% of the time, it's CORS!**

Just add your frontend URL to CORS_ORIGINS and redeploy. That's it! ✅
