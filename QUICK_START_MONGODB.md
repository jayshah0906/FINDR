# 🚀 Quick Start - MongoDB Migration

## Complete this in 20 minutes!

---

## Part 1: MongoDB Atlas Setup (10 minutes)

### 1. Create Account
- Go to: https://www.mongodb.com/cloud/atlas/register
- Sign up (free)

### 2. Create Cluster
- Click "Build a Database"
- Choose **M0 FREE** tier
- Select AWS + closest region
- Click "Create"
- Wait 3-5 minutes

### 3. Create User
- Username: `parking_admin`
- Click "Autogenerate Secure Password"
- **COPY AND SAVE THE PASSWORD!** Example: `xK9mP2nQ7vL4wR8t`
- Click "Create User"

### 4. Network Access
- Click "Add IP Address"
- Choose "Allow Access from Anywhere" (`0.0.0.0/0`)
- Click "Confirm"

### 5. Get Connection String
- Click "Connect" on your cluster
- Choose "Connect your application"
- Copy the connection string
- It looks like:
  ```
  mongodb+srv://parking_admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
  ```

### 6. Prepare Your Connection String
Replace `<password>` with your actual password and add `/parking_db`:
```
mongodb+srv://parking_admin:xK9mP2nQ7vL4wR8t@cluster0.xxxxx.mongodb.net/parking_db?retryWrites=true&w=majority
```

**SAVE THIS STRING - YOU'LL NEED IT NEXT!**

---

## Part 2: Install & Configure (5 minutes)

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Create .env File
Create `backend/.env` with your connection string:
```env
DATABASE_URL=mongodb+srv://parking_admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/parking_db?retryWrites=true&w=majority
```

**Replace with YOUR actual connection string from Part 1, Step 6!**

### 3. Initialize Database
```bash
python init_mongodb.py
```

Expected output:
```
✅ Successfully connected to MongoDB!
✅ Created 'users' collection
✅ Created 'zones' collection
✅ Seeded 10 zones
```

---

## Part 3: Test (5 minutes)

### 1. Start Backend
```bash
cd backend
python run_server.py
```

### 2. Start Frontend (new terminal)
```bash
cd frontend
npm run dev
```

### 3. Test in Browser
1. Open http://localhost:5174
2. Click "Sign In" → "Sign Up"
3. Register a new user
4. Login
5. Select date and time
6. Click on a zone
7. See predictions!

---

## ✅ Success Checklist

- [ ] MongoDB Atlas cluster created
- [ ] Database user created with password saved
- [ ] IP whitelist set to 0.0.0.0/0
- [ ] Connection string copied and modified
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with connection string
- [ ] `init_mongodb.py` ran successfully
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Can register a new user
- [ ] Can login
- [ ] Can get predictions

---

## 🐛 Quick Troubleshooting

### "Connection refused"
→ Check your connection string in `.env` file

### "Authentication failed"
→ Verify password is correct (no typos!)

### "IP not whitelisted"
→ Add `0.0.0.0/0` in MongoDB Atlas Network Access

### "Module 'motor' not found"
→ Run `pip install -r requirements.txt` again

---

## 📱 Verify in MongoDB Atlas

1. Go to MongoDB Atlas dashboard
2. Click "Browse Collections"
3. See `parking_db` database
4. See `users` and `zones` collections
5. After registering, see your user in `users` collection!

---

## 🎉 Done!

Your app now uses MongoDB Atlas and is ready for Vercel deployment!

**Next:** Deploy to Vercel (your backend will work from anywhere!)
