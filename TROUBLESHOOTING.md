# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### Backend Issues

#### Issue: "ModuleNotFoundError: No module named 'jose'"
**Cause**: Missing authentication dependencies

**Solution**:
```bash
cd backend
pip install python-jose[cryptography] passlib[bcrypt] python-dotenv
# Or
pip install -r requirements.txt
```

#### Issue: "Table 'users' doesn't exist"
**Cause**: Database not initialized with new User table

**Solution**:
```bash
cd backend
python init_db.py
```

#### Issue: "ImportError: cannot import name 'auth_routes'"
**Cause**: Auth routes file not found or syntax error

**Solution**:
1. Check if `backend/app/routes/auth_routes.py` exists
2. Check for syntax errors in the file
3. Restart the backend server

#### Issue: Backend won't start - "Address already in use"
**Cause**: Port 8001 is already in use

**Solution**:
```bash
# Find process using port 8001
lsof -i :8001

# Kill the process
kill -9 <PID>

# Or use a different port in run_server.py
```

#### Issue: "CORS policy: No 'Access-Control-Allow-Origin' header"
**Cause**: Frontend URL not in CORS allowed origins

**Solution**:
Edit `backend/app/middleware/cors.py`:
```python
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    # Add your frontend URL
]
```

### Frontend Issues

#### Issue: "Cannot find module './pages/LandingPage'"
**Cause**: LandingPage component not created

**Solution**:
1. Check if `frontend/src/pages/LandingPage.jsx` exists
2. Check if `frontend/src/pages/LandingPage.css` exists
3. Restart the dev server

#### Issue: Blank page after login
**Cause**: Protected route not working or token not stored

**Solution**:
1. Open browser console (F12)
2. Check for errors
3. Check localStorage:
```javascript
// In browser console
localStorage.getItem('token')
localStorage.getItem('user')
```
4. If null, try logging in again

#### Issue: "Failed to fetch" or network errors
**Cause**: Backend not running or wrong URL

**Solution**:
1. Check if backend is running on port 8001
2. Visit http://localhost:8001 in browser
3. Check `frontend/src/services/api.js` for correct URL:
```javascript
const API_URL = 'http://localhost:8001'
```

#### Issue: Styles not loading
**Cause**: CSS file not imported

**Solution**:
Check imports in component files:
```javascript
import './LandingPage.css'
import './MainPage.css'
```

#### Issue: Map not displaying
**Cause**: Leaflet CSS not loaded or map container has no height

**Solution**:
1. Check if Leaflet CSS is imported:
```javascript
import 'leaflet/dist/leaflet.css'
```
2. Check CSS for map container:
```css
.uber-map {
  height: 500px; /* Must have explicit height */
}
```

### Authentication Issues

#### Issue: "Could not validate credentials"
**Cause**: Invalid or expired token

**Solution**:
```javascript
// Clear localStorage and login again
localStorage.clear()
// Then login again
```

#### Issue: "Email already registered"
**Cause**: Email already exists in database

**Solution**:
- Use a different email
- Or login with existing credentials
- Or delete the user from database:
```bash
sqlite3 backend/parking_prediction.db
DELETE FROM users WHERE email = 'your@email.com';
.quit
```

#### Issue: "Username already taken"
**Cause**: Username already exists

**Solution**:
- Choose a different username
- Or login with existing credentials

#### Issue: "Password too short"
**Cause**: Password less than 6 characters

**Solution**:
Use a password with at least 6 characters

#### Issue: Token expires too quickly
**Cause**: Default expiration is 7 days

**Solution**:
Edit `backend/app/services/auth_service.py`:
```python
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30  # 30 days
```

### Database Issues

#### Issue: "Database is locked"
**Cause**: Multiple processes accessing SQLite

**Solution**:
1. Close all connections to database
2. Restart backend server
3. For production, use PostgreSQL instead of SQLite

#### Issue: "No such table: users"
**Cause**: Database not initialized

**Solution**:
```bash
cd backend
python init_db.py
```

#### Issue: Want to reset database
**Solution**:
```bash
cd backend
rm parking_prediction.db
python init_db.py
python scripts/seed_zones.py
```

### UI/UX Issues

#### Issue: Modal won't close
**Cause**: Click event not propagating correctly

**Solution**:
Click the X button or press ESC (if implemented)

#### Issue: Form validation not working
**Cause**: HTML5 validation or JavaScript validation issue

**Solution**:
Check browser console for errors

#### Issue: Animations not smooth
**Cause**: Browser performance or CSS issues

**Solution**:
1. Close other browser tabs
2. Check if GPU acceleration is enabled
3. Reduce animation complexity

#### Issue: Responsive design broken on mobile
**Cause**: CSS media queries not working

**Solution**:
1. Check viewport meta tag in `index.html`:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
2. Test in browser dev tools mobile view

### Deployment Issues

#### Issue: "SECRET_KEY not set" in production
**Cause**: Environment variable not configured

**Solution**:
```bash
# Set environment variable
export SECRET_KEY="your-super-secret-key-here"

# Or use .env file
echo "SECRET_KEY=your-super-secret-key-here" > .env
```

#### Issue: HTTPS required in production
**Cause**: Browsers require HTTPS for secure cookies

**Solution**:
1. Set up SSL certificate (Let's Encrypt)
2. Configure reverse proxy (Nginx)
3. Update CORS settings

#### Issue: Database connection fails in production
**Cause**: SQLite not suitable for production

**Solution**:
Switch to PostgreSQL:
```python
# In config.py
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/dbname")
```

## Debug Commands

### Check Backend Status
```bash
# Test if backend is running
curl http://localhost:8001/

# Test health endpoint
curl http://localhost:8001/health

# Test zones endpoint
curl http://localhost:8001/zones
```

### Check Frontend Status
```bash
# Test if frontend is running
curl http://localhost:5173/
```

### Test Authentication
```bash
# Register user
curl -X POST http://localhost:8001/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "test123",
    "full_name": "Test User"
  }'

# Login
curl -X POST http://localhost:8001/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "test123"
  }'

# Get user info (replace TOKEN with actual token)
curl http://localhost:8001/auth/me \
  -H "Authorization: Bearer TOKEN"
```

### Check Database
```bash
# Open database
sqlite3 backend/parking_prediction.db

# List tables
.tables

# View users
SELECT * FROM users;

# View zones
SELECT * FROM zones;

# Count users
SELECT COUNT(*) FROM users;

# Exit
.quit
```

### Check Logs

#### Backend Logs
```bash
# Run with verbose logging
cd backend
python run_server.py --log-level debug
```

#### Frontend Logs
```bash
# Check browser console (F12)
# Look for errors in Console tab
# Check Network tab for failed requests
```

## Browser-Specific Issues

### Chrome/Edge
- Clear cache: Ctrl+Shift+Delete
- Hard reload: Ctrl+Shift+R
- Check console: F12

### Firefox
- Clear cache: Ctrl+Shift+Delete
- Hard reload: Ctrl+F5
- Check console: F12

### Safari
- Clear cache: Cmd+Option+E
- Hard reload: Cmd+Shift+R
- Check console: Cmd+Option+C

## Performance Issues

### Slow Backend Response
**Solutions**:
1. Add database indexing
2. Implement caching
3. Optimize queries
4. Use connection pooling

### Slow Frontend Loading
**Solutions**:
1. Optimize images
2. Lazy load components
3. Minimize bundle size
4. Use CDN for assets

### High Memory Usage
**Solutions**:
1. Check for memory leaks
2. Optimize state management
3. Clean up event listeners
4. Use React.memo for expensive components

## Security Issues

### Token Stolen
**Solution**:
1. Logout immediately
2. Change password
3. Implement token refresh
4. Add IP validation

### Brute Force Attacks
**Solution**:
1. Implement rate limiting
2. Add CAPTCHA
3. Lock account after failed attempts
4. Monitor login attempts

### SQL Injection Concerns
**Solution**:
SQLAlchemy ORM prevents SQL injection by default
Use parameterized queries always

## Getting Help

### Check Documentation
1. SETUP_INSTRUCTIONS.md
2. AUTH_SYSTEM_README.md
3. QUICK_REFERENCE.md
4. This file (TROUBLESHOOTING.md)

### Check API Documentation
Visit: http://localhost:8001/docs

### Debug Checklist
- [ ] Backend is running
- [ ] Frontend is running
- [ ] Database is initialized
- [ ] Dependencies are installed
- [ ] No errors in console
- [ ] Network requests succeed
- [ ] Token is stored
- [ ] CORS is configured

### Still Having Issues?

1. **Check browser console** (F12) for errors
2. **Check backend logs** for error messages
3. **Verify all files exist** as per file structure
4. **Restart both servers** (backend and frontend)
5. **Clear browser cache** and localStorage
6. **Try a different browser**
7. **Check firewall settings**
8. **Verify port availability**

### Emergency Reset

If nothing works, try a complete reset:

```bash
# Backend
cd backend
rm parking_prediction.db
pip install -r requirements.txt
python init_db.py
python scripts/seed_zones.py

# Frontend
cd frontend
rm -rf node_modules
npm install

# Clear browser
# Open browser console (F12)
localStorage.clear()
# Hard reload: Ctrl+Shift+R
```

## Prevention Tips

### Development
- Always check console for errors
- Test in multiple browsers
- Use version control (git)
- Keep dependencies updated
- Write tests

### Production
- Use environment variables
- Enable HTTPS
- Set up monitoring
- Configure logging
- Regular backups
- Security audits

## Quick Fixes

### "It was working yesterday"
```bash
# Check git history
git log --oneline
git diff HEAD~1

# Revert if needed
git checkout HEAD~1 -- <file>
```

### "Works on my machine"
- Check Node.js version
- Check Python version
- Check environment variables
- Check file permissions

### "Random errors"
- Restart servers
- Clear cache
- Check memory usage
- Check disk space

## Contact Support

If you've tried everything and still have issues:

1. Document the error message
2. Note steps to reproduce
3. Check system requirements
4. Review all documentation
5. Search for similar issues

Remember: Most issues are configuration or environment related!
