# 🔧 Fix "Failed to Fetch" on Render - Complete Guide

## Problem Identified
Your signup is failing because the **VITE_API_URL environment variable is not set in Render**. Without it, the frontend defaults to `http://localhost:8001/api/v1`, which doesn't exist in production.

## ✅ Solution: Set Environment Variable in Render

### Step 1: Get Your Backend URL
1. Go to Render Dashboard
2. Click on your **Backend** service
3. Copy the URL at the top (looks like: `https://your-backend-name.onrender.com`)

### Step 2: Set Frontend Environment Variable
1. Go to Render Dashboard
2. Click on your **Frontend** service (the one with React/Vite)
3. Click **"Environment"** in the left sidebar
4. Click **"Add Environment Variable"**
5. Add this variable:
   ```
   Key: VITE_API_URL
   Value: https://your-backend-name.onrender.com/api/v1
   ```
   ⚠️ **IMPORTANT**: Replace `your-backend-name` with your actual backend URL
   ⚠️ **IMPORTANT**: Must end with `/api/v1`

### Step 3: Trigger Redeploy
1. After adding the environment variable, Render will ask if you want to redeploy
2. Click **"Save Changes"** or **"Manual Deploy"** → **"Deploy latest commit"**
3. Wait for the build to complete (2-3 minutes)

### Step 4: Test
1. Open your frontend: `https://ai-based-parking-availability-predictor-3.onrender.com`
2. Click "Sign Up"
3. Fill in the form
4. Click "Create Account"
5. Should work now! ✅

---

## 🔍 How to Verify It's Working

### Option 1: Use the Test Page (Easiest)
1. Open the test page I created: `test_frontend_api.html`
2. Open it in your browser (double-click the file)
3. Enter your backend URL
4. Click all the test buttons
5. It will show you exactly what's wrong

### Option 2: Check Browser Console
1. Open your frontend in browser
2. Press F12 to open Developer Tools
3. Go to "Console" tab
4. Type: `import.meta.env.VITE_API_URL`
5. Press Enter
6. Should show your backend URL (not `undefined`)

### Option 3: Check Network Tab
1. Open your frontend in browser
2. Press F12 to open Developer Tools
3. Go to "Network" tab
4. Try to sign up
5. Look at the request URL - should be your backend URL, not localhost

---

## 🚨 Common Issues & Solutions

### Issue 1: "Failed to fetch" still happening
**Cause**: Backend is sleeping (Render free tier)
**Solution**: 
- Wait 60 seconds for backend to wake up
- Try signup again
- First request always takes longer

### Issue 2: CORS error in console
**Cause**: Frontend URL not in backend CORS list
**Solution**: Already fixed! Your frontend URL is in `backend/app/config.py`

### Issue 3: Environment variable not working
**Cause**: Didn't redeploy after setting variable
**Solution**: 
- Go to Render → Frontend service
- Click "Manual Deploy" → "Deploy latest commit"
- Wait for build to complete

### Issue 4: Wrong backend URL format
**Cause**: Missing `/api/v1` at the end
**Solution**: 
- Correct: `https://your-backend.onrender.com/api/v1`
- Wrong: `https://your-backend.onrender.com`
- Wrong: `https://your-backend.onrender.com/api/v1/`

---

## 📋 Quick Checklist

- [ ] Backend is deployed and showing "Live" in Render
- [ ] Frontend is deployed and showing "Live" in Render
- [ ] `VITE_API_URL` is set in Frontend environment variables
- [ ] `VITE_API_URL` ends with `/api/v1` (no trailing slash)
- [ ] Frontend was redeployed after setting environment variable
- [ ] Backend CORS includes frontend URL (already done ✅)
- [ ] Waited 60 seconds for backend to wake up on first request

---

## 🎯 What Should Happen

### Before Fix:
```
Frontend tries to call: http://localhost:8001/api/v1/auth/register
Result: ❌ Failed to fetch (localhost doesn't exist in production)
```

### After Fix:
```
Frontend tries to call: https://your-backend.onrender.com/api/v1/auth/register
Result: ✅ Success! User created
```

---

## 🔧 Technical Explanation

### Why This Happens
1. Vite environment variables must start with `VITE_` to be exposed to the browser
2. In development, the proxy in `vite.config.js` forwards `/api` to `localhost:8001`
3. In production (Render), there's no proxy, so frontend needs the full backend URL
4. Without `VITE_API_URL`, the code defaults to `http://localhost:8001/api/v1`
5. Localhost doesn't exist in production → "Failed to fetch"

### How the Code Works
```javascript
// frontend/src/utils/constants.js
export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001/api/v1'
```

- `import.meta.env.VITE_API_URL` reads from Render environment variable
- If not set, falls back to localhost (for development)
- In production, MUST be set to backend URL

---

## 📞 Still Not Working?

If you've followed all steps and it's still not working:

1. **Share your backend URL** - I'll verify the format
2. **Check browser console** - Press F12, share any error messages
3. **Check Network tab** - Press F12 → Network, try signup, share the request URL
4. **Verify environment variable** - Screenshot of Render environment variables page

---

## ✅ Success Indicators

You'll know it's working when:
- ✅ Signup form submits without "Failed to fetch"
- ✅ You see "Success! Redirecting..." message
- ✅ You're redirected to the dashboard
- ✅ Browser console shows no errors
- ✅ Network tab shows request to your backend URL (not localhost)

---

**Next Step**: Set the `VITE_API_URL` environment variable in Render and redeploy! 🚀
