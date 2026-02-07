import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { API_URL } from '../utils/constants'
import './LandingPage.css'

function LandingPage() {
  const [showAuth, setShowAuth] = useState(false)
  const [isLogin, setIsLogin] = useState(true)
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    full_name: ''
  })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(false)
  const navigate = useNavigate()

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
    setError('')
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    // Validation for signup
    if (!isLogin) {
      if (!formData.full_name || !formData.email || !formData.username || !formData.password) {
        setError('Please fill in all fields')
        setLoading(false)
        return
      }
      if (formData.password.length < 6) {
        setError('Password must be at least 6 characters')
        setLoading(false)
        return
      }
    }

    try {
      const endpoint = isLogin ? '/api/v1/auth/login' : '/api/v1/auth/register'
      const payload = isLogin 
        ? { username: formData.username, password: formData.password }
        : formData

      const response = await fetch(`${API_URL.replace('/api/v1', '')}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      })

      const data = await response.json()

      if (!response.ok) {
        // Handle different error formats
        let errorMessage = 'Authentication failed'
        
        if (typeof data.detail === 'string') {
          errorMessage = data.detail
        } else if (data.detail && Array.isArray(data.detail)) {
          errorMessage = data.detail.map(err => err.msg).join(', ')
        } else if (data.message) {
          errorMessage = data.message
        }
        
        throw new Error(errorMessage)
      }

      // Store token and user info
      localStorage.setItem('token', data.access_token)
      localStorage.setItem('user', JSON.stringify(data.user))

      // Show success message
      setSuccess(true)
      
      // Close modal and navigate to dashboard after a brief delay
      setTimeout(() => {
        setShowAuth(false)
        navigate('/dashboard')
      }, 800)
    } catch (err) {
      console.error('Auth error:', err)
      setError(err.message || 'An error occurred. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const toggleAuthMode = () => {
    setIsLogin(!isLogin)
    setError('')
    setSuccess(false)
    setFormData({
      email: '',
      username: '',
      password: '',
      full_name: ''
    })
  }

  return (
    <div className="landing-page">
      {/* Navigation */}
      <nav className="landing-nav">
        <div className="nav-container">
          <div className="nav-logo">
            <img src="/logo1.png" alt="FINDR Logo" className="logo-image" />
          </div>
          
          <div className="nav-center">
            <div className="nav-links">
              <a href="#features" className="nav-link">Features</a>
              <a href="#zones" className="nav-link">Zones</a>
              <a href="#how-it-works" className="nav-link">How It Works</a>
            </div>
            <div className="nav-divider"></div>
            <div className="nav-stats">
              <span className="nav-stat">10 Zones</span>
              <span className="nav-stat-dot">•</span>
              <span className="nav-stat">24/7</span>
            </div>
          </div>
          
          <button 
            className="nav-btn"
            onClick={() => setShowAuth(true)}
          >
            Sign In
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-container">
          <div className="hero-content">
            <h1 className="hero-title animate-fade-in-up">
              Find Parking
              <span className="hero-gradient"> Smarter</span>
            </h1>
            <p className="hero-subtitle animate-fade-in-up-delay">
              AI-powered predictions help you find available parking spots in Seattle. 
              Save time, reduce stress, and never circle the block again.
            </p>
            <div className="hero-buttons animate-fade-in-up-delay-2">
              <button 
                className="btn-primary"
                onClick={() => setShowAuth(true)}
              >
                Get Started
              </button>
              <button className="btn-secondary">
                Learn More
              </button>
            </div>
            
            {/* Live Stats */}
            <div className="hero-live-stats animate-fade-in-up-delay-3">
              <div className="live-stat">
                <span className="live-dot"></span>
                <span className="live-text">Live predictions updating every minute</span>
              </div>
              <div className="live-stat">
                <span className="stat-highlight">1,247</span>
                <span className="live-text">parking spots tracked today</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="features-section">
        <div className="features-container">
          <h2 className="section-title animate-on-scroll">Why Choose FINDR?</h2>
          <div className="features-grid">
            <div className="feature-card animate-on-scroll" style={{animationDelay: '0.1s'}}>
              <div className="feature-icon"></div>
              <h3>AI-Powered Predictions</h3>
              <p>Machine learning algorithms analyze patterns to predict parking availability accurately</p>
            </div>
            <div className="feature-card animate-on-scroll" style={{animationDelay: '0.2s'}}>
              <div className="feature-icon"></div>
              <h3>Real-Time Data</h3>
              <p>Get instant updates on parking availability across all zones in Seattle</p>
            </div>
            <div className="feature-card animate-on-scroll" style={{animationDelay: '0.3s'}}>
              <div className="feature-icon"></div>
              <h3>Interactive Maps</h3>
              <p>Visual zone selection with color-coded availability indicators</p>
            </div>
            <div className="feature-card animate-on-scroll" style={{animationDelay: '0.4s'}}>
              <div className="feature-icon"></div>
              <h3>Smart Analytics</h3>
              <p>View trends, events, and traffic patterns that affect parking</p>
            </div>
            <div className="feature-card animate-on-scroll" style={{animationDelay: '0.5s'}}>
              <div className="feature-icon"></div>
              <h3>Event Awareness</h3>
              <p>Get alerts about nearby events that impact parking availability</p>
            </div>
            <div className="feature-card animate-on-scroll" style={{animationDelay: '0.6s'}}>
              <div className="feature-icon"></div>
              <h3>Time Predictions</h3>
              <p>Plan ahead with hourly forecasts for your destination</p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section id="how-it-works" className="how-section">
        <div className="how-container">
          <h2 className="section-title">How It Works</h2>
          <div className="steps-grid">
            <div className="step">
              <div className="step-number">1</div>
              <h3>Select Your Zone</h3>
              <p>Choose from 50+ parking zones across Seattle</p>
            </div>
            <div className="step">
              <div className="step-number">2</div>
              <h3>Pick Your Time</h3>
              <p>Select when you need parking</p>
            </div>
            <div className="step">
              <div className="step-number">3</div>
              <h3>Get Predictions</h3>
              <p>View AI-powered availability forecasts</p>
            </div>
            <div className="step">
              <div className="step-number">4</div>
              <h3>Park Smart</h3>
              <p>Head to zones with high availability</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section id="zones" className="cta-section">
        <div className="cta-container">
          <h2>Ready to Find Parking Faster?</h2>
          <p>Join thousands of drivers who save time every day</p>
          <button 
            className="cta-button"
            onClick={() => setShowAuth(true)}
          >
            Start Predicting Now
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="landing-footer">
        <div className="footer-container">
          <div className="footer-content">
            <div className="footer-brand">
              <img src="/logo1.png" alt="FINDR Logo" className="footer-logo-image" />
            </div>
            <div className="footer-info">
              <p className="footer-text">© 2026 FINDR. Built for IITG Hackathon.</p>
              <p className="footer-credits">
                Powered by MongoDB Atlas • OpenStreetMap • Leaflet Maps
              </p>
            </div>
          </div>
        </div>
      </footer>

      {/* Auth Modal */}
      {showAuth && (
        <div className="auth-modal" onClick={() => setShowAuth(false)}>
          <div className="auth-content" onClick={(e) => e.stopPropagation()}>
            <button 
              className="auth-close"
              onClick={() => setShowAuth(false)}
            >
              ×
            </button>
            
            <div className="auth-header">
              <h2>{isLogin ? 'Welcome Back' : 'Create Account'}</h2>
              <p>{isLogin ? 'Sign in to continue' : 'Join FINDR today'}</p>
            </div>

            <form onSubmit={handleSubmit} className="auth-form">
              {error && <div className="auth-error">{error}</div>}
              {success && <div className="auth-success">✓ Success! Redirecting...</div>}
              
              {!isLogin && (
                <>
                  <div className="form-group">
                    <label>Full Name</label>
                    <input
                      type="text"
                      name="full_name"
                      value={formData.full_name}
                      onChange={handleInputChange}
                    />
                  </div>
                  <div className="form-group">
                    <label>Email</label>
                    <input
                      type="email"
                      name="email"
                      value={formData.email}
                      onChange={handleInputChange}
                      required
                    />
                  </div>
                </>
              )}

              <div className="form-group">
                <label>Username</label>
                <input
                  type="text"
                  name="username"
                  value={formData.username}
                  onChange={handleInputChange}
                  required
                />
              </div>

              <div className="form-group">
                <label>Password</label>
                <input
                  type="password"
                  name="password"
                  value={formData.password}
                  onChange={handleInputChange}
                  required
                />
              </div>

              <button 
                type="submit" 
                className="auth-submit"
                disabled={loading}
              >
                {loading ? 'Please wait...' : (isLogin ? 'Sign In' : 'Create Account')}
              </button>
            </form>

            <div className="auth-switch">
              {isLogin ? "Don't have an account? " : "Already have an account? "}
              <button onClick={toggleAuthMode}>
                {isLogin ? 'Sign Up' : 'Sign In'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default LandingPage
