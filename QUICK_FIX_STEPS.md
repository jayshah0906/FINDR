# 🚀 Quick Fix - 3 Steps (2 Minutes)

## The Problem
Your frontend doesn't know where your backend is! It's trying to call `localhost` which doesn't exist in production.

## The Fix

### Step 1: Get Backend URL (30 seconds)
```
1. Open Render Dashboard
2. Click your BACKEND service
3. Copy the URL (example: https://parking-backend-abc123.onrender.com)
```

### Step 2: Set Environment Variable (1 minute)
```
1. Open Render Dashboard
2. Click your FRONTEND service
3. Click "Environment" tab
4. Click "Add Environment Variable"
5. Enter:
   Key:   VITE_API_URL
   Value: https://parking-backend-abc123.onrender.com/api/v1
          ↑ YOUR backend URL + /api/v1
```

### Step 3: Redeploy (30 seconds)
```
1. Click "Save Changes"
2. Wait for automatic redeploy
   OR
   Click "Manual Deploy" → "Deploy latest commit"
```

## Done! ✅

Wait 2-3 minutes for build to complete, then test signup again.

---

## Why This Works

**Before:**
- Frontend calls: `http://localhost:8001/api/v1` ❌
- Result: "Failed to fetch"

**After:**
- Frontend calls: `https://your-backend.onrender.com/api/v1` ✅
- Result: Success!

---

## Still Not Working?

1. **Wait 60 seconds** - Backend might be sleeping (free tier)
2. **Check the URL format** - Must end with `/api/v1`
3. **Verify backend is Live** - Check Render dashboard
4. **Share your backend URL** - I'll help debug

---

**That's it!** This is the only thing preventing your signup from working. 🎯
