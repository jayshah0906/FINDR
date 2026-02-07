# Frontend - Parking Availability Predictor

React + Vite frontend for the AI-based parking availability prediction system.

## Environment Variables

### Required for Production

Create a `.env` file or set in your deployment platform:

```bash
VITE_API_URL=https://your-backend-url.onrender.com/api/v1
```

**Important Notes:**
- Variable MUST start with `VITE_` to be exposed to the browser
- Must include `/api/v1` at the end
- No trailing slash

### For Render Deployment

1. Go to Render Dashboard
2. Select your Frontend service
3. Click "Environment" tab
4. Add environment variable:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://your-backend-url.onrender.com/api/v1`
5. Save and redeploy

## Local Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
frontend/
├── src/
│   ├── components/     # Reusable UI components
│   ├── pages/          # Page components
│   ├── services/       # API services
│   ├── utils/          # Utility functions and constants
│   ├── styles/         # Global styles
│   ├── App.jsx         # Main app component
│   └── index.jsx       # Entry point
├── public/             # Static assets
├── index.html          # HTML template
└── vite.config.js      # Vite configuration
```

## Key Features

- **Landing Page**: Marketing page with auth modal
- **Dashboard**: Main prediction interface
- **Interactive Map**: Leaflet-based zone selection
- **Time Picker**: Select prediction time
- **Prediction Cards**: Display availability predictions
- **Zone Details**: Detailed view for each zone

## API Configuration

The frontend uses `VITE_API_URL` environment variable to determine the backend URL:

```javascript
// src/utils/constants.js
export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8001/api/v1'
```

**Development**: Uses localhost with Vite proxy
**Production**: Uses environment variable (MUST be set!)

## Troubleshooting

### "Failed to fetch" error in production

**Cause**: `VITE_API_URL` environment variable not set

**Solution**:
1. Set `VITE_API_URL` in Render dashboard
2. Redeploy the frontend
3. Wait 2-3 minutes for build to complete

### Environment variable not working

**Cause**: Didn't redeploy after setting variable

**Solution**:
1. Go to Render → Frontend service
2. Click "Manual Deploy" → "Deploy latest commit"
3. Wait for build to complete

### CORS errors

**Cause**: Frontend URL not in backend CORS list

**Solution**: Add your frontend URL to `backend/app/config.py` CORS_ORIGINS

## Tech Stack

- **React 18**: UI library
- **Vite**: Build tool and dev server
- **React Router**: Client-side routing
- **Leaflet**: Interactive maps
- **Axios**: HTTP client
- **CSS3**: Styling

## Deployment

### Render

1. Connect GitHub repository
2. Select "Static Site" service type
3. Set build command: `npm run build`
4. Set publish directory: `dist`
5. Add environment variable: `VITE_API_URL`
6. Deploy!

### Vercel

1. Connect GitHub repository
2. Framework preset: Vite
3. Add environment variable: `VITE_API_URL`
4. Deploy!

### Netlify

1. Connect GitHub repository
2. Build command: `npm run build`
3. Publish directory: `dist`
4. Add environment variable: `VITE_API_URL`
5. Deploy!

## License

MIT
