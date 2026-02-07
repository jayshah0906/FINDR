# 🔍 Debug "Failed to Fetch" Error

## Step-by-Step Debugging

### Step 1: Check Browser Console

1. Open your frontend: `https://ai-based-parking-availability-predictor-3.onrender.com`
2. Press **F12** to open Developer Tools
3. Go to **Console** tab
4. Type this and press Enter:
   ```javascript
   console.log('API_URL:', import.meta.env.VITE_API_URL)
   ```
5. **What does it show?**
   - If it shows your backend URL → Good ✅
   - If it shows `undefined` → Environment variable not set ❌
   - If it shows `localhost` → Environment variable not set ❌

### Step 2: Check Network Request

1. In Developer Tools, go to **Network** tab
2. Try to signup
3. Look for a request (might be red/failed)
4. Click on it
5. **Check the Request URL:**
   - Should be: `https://YOUR-BACKEND.onrender.com/api/v1/auth/register`
   - If it's `localhost` → Environment variable not set
   - If it's correct but failed → Backend issue

### Step 3: Test Backend Directly

Open a new tab and try these URLs:

**Health Check:**
```
https://YOUR-BACKEND-URL.onrender.com/api/v1/health
```
Should return: `{"status":"healthy",...}`

**If backend URL doesn't work:**
- Backend might be sleeping (Render free tier)
- Wait 60 seconds and try again
- Check Render dashboard - is backend "Live"?

### Step 4: Check Render Environment Variables

**Frontend:**
1. Go to Render dashboard
2. Click on your **frontend** service
3. Go to **Environment** tab
4. Look for `VITE_API_URL`
5. **Is it there?** 
   - Yes → What's the value?
   - No → That's the problem! Add it now

**Backend:**
1. Click on your **backend** service
2. Check if it says **"Live"** or **"Sleeping"**
3. If sleeping, click on it to wake it up

---

## Common Causes & Solutions

### Cause 1: VITE_API_URL Not Set in Render ⚠️

**Symptoms:**
- Console shows `undefined` or `localhost`
- Network tab shows request to `localhost`

**Solution:**
1. Render dashboard → Frontend service → Environment
2. Add variable:
   ```
   Key: VITE_API_URL
   Value: https://YOUR-BACKEND.onrender.com/api/v1
   ```
3. Save and wait for redeploy (2-3 min)

### Cause 2: Backend is Sleeping 😴

**Symptoms:**
- Request times out
- Takes 30-60 seconds
- First request fails, second works

**Solution:**
- This is normal for Render free tier
- Just wait 60 seconds and try again
- Or upgrade to paid plan ($7/month)

### Cause 3: CORS Not Configured ❌

**Symptoms:**
- Console shows: `CORS policy: No 'Access-Control-Allow-Origin'`
- Request reaches backend but is blocked

**Solution:**
- Already fixed in your code ✅
- Make sure backend redeployed after CORS fix

### Cause 4: Wrong Backend URL 🔗

**Symptoms:**
- 404 error
- "Not found"

**Solution:**
- Check VITE_API_URL value
- Should end with `/api/v1`
- Should NOT end with `/` after `/api/v1`

### Cause 5: Frontend Not Redeployed 🔄

**Symptoms:**
- Environment variable is set but still using localhost

**Solution:**
- After adding VITE_API_URL, frontend must redeploy
- Check Render dashboard for deployment status
- Wait for "Your site is live 🎉"

---

## Quick Diagnostic Commands

### In Browser Console (F12):

```javascript
// Check API URL
console.log('API_URL:', import.meta.env.VITE_API_URL)

// Check if it's using fallback
console.log('Using fallback?', !import.meta.env.VITE_API_URL)

// Try to fetch health endpoint
fetch('https://YOUR-BACKEND.onrender.com/api/v1/health')
  .then(r => r.json())
  .then(d => console.log('Backend response:', d))
  .catch(e => console.error('Backend error:', e))
```

### In Terminal:

```bash
# Test backend health
curl https://YOUR-BACKEND.onrender.com/api/v1/health

# Test backend registration
curl -X POST https://YOUR-BACKEND.onrender.com/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "password123",
    "full_name": "Test User"
  }'
```

---

## What to Share for Help

Please share these details:

1. **Frontend URL:** `https://ai-based-parking-availability-predictor-3.onrender.com`

2. **Backend URL:** `https://_____.onrender.com` (what is it?)

3. **Browser Console Output:**
   ```javascript
   console.log('API_URL:', import.meta.env.VITE_API_URL)
   // What does this show?
   ```

4. **Network Tab:**
   - What URL is the request going to?
   - What's the error message?
   - Screenshot if possible

5. **Render Environment:**
   - Is `VITE_API_URL` set in frontend environment?
   - What's the exact value?
   - Is backend showing "Live" or "Sleeping"?

---

## Most Likely Issues

Based on your symptoms, it's probably one of these:

### 1. VITE_API_URL Not Set (90% chance)
- Go to Render → Frontend → Environment
- Add `VITE_API_URL` with your backend URL
- Wait for redeploy

### 2. Backend Sleeping (5% chance)
- Wait 60 seconds
- Try again
- Should work on second attempt

### 3. Wrong URL Format (3% chance)
- Check VITE_API_URL ends with `/api/v1`
- No trailing slash after `/api/v1`

### 4. Frontend Not Redeployed (2% chance)
- Check Render deployment status
- Wait for "Live"
- Clear browser cache

---

## Next Steps

1. **Check browser console** - What does `import.meta.env.VITE_API_URL` show?
2. **Check Network tab** - What URL is it trying to reach?
3. **Share your backend URL** - So I can test it
4. **Check Render environment** - Is VITE_API_URL set?

**Share these 4 things and I can pinpoint the exact issue!**
