import { useState, useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import './MainPage.css'
import api from '../services/api'

// Zone data with coordinates
const ZONES = [
  { id: 1, name: 'Downtown Pike St', lat: 47.6105, lng: -122.3380 },
  { id: 2, name: 'Downtown 1st Ave', lat: 47.6050, lng: -122.3350 },
  { id: 3, name: 'Downtown 3rd Ave', lat: 47.6080, lng: -122.3310 },
  { id: 4, name: 'Capitol Hill - Broadway', lat: 47.6240, lng: -122.3210 },
  { id: 5, name: 'University District - University Way', lat: 47.6650, lng: -122.3130 },
  { id: 6, name: 'Stadium District - Occidental', lat: 47.5920, lng: -122.3330 },
  { id: 7, name: 'Stadium District - 1st Ave S', lat: 47.5970, lng: -122.3280 },
  { id: 8, name: 'Capitol Hill - Pike St', lat: 47.6180, lng: -122.3150 },
  { id: 9, name: 'University District - 45th St', lat: 47.6590, lng: -122.3080 },
  { id: 10, name: 'Fremont - Fremont Ave', lat: 47.6505, lng: -122.3493 }
]

// Modern color scheme
const COLORS = {
  High: '#10b981',    // Green
  Medium: '#f59e0b',  // Amber
  Low: '#ef4444'      // Red
}

function MainPage() {
  const navigate = useNavigate()
  const [selectedDate, setSelectedDate] = useState('')
  const [selectedHour, setSelectedHour] = useState('')
  const [showResults, setShowResults] = useState(false)
  const [selectedZone, setSelectedZone] = useState('')
  const [predictions, setPredictions] = useState([])
  const [loading, setLoading] = useState(false)
  const [zoneColors, setZoneColors] = useState({})
  const [eventAlert, setEventAlert] = useState(null)
  const [dayEvents, setDayEvents] = useState(null)
  const [loadingEvents, setLoadingEvents] = useState(false)
  const [alternativeZones, setAlternativeZones] = useState([])
  const [loadingAlternatives, setLoadingAlternatives] = useState(false)
  
  const mapRef = useRef(null)
  const mapInstanceRef = useRef(null)
  const markersRef = useRef({})
  const resultsSectionRef = useRef(null)

  // Generate hour options (0-23)
  const hourOptions = Array.from({ length: 24 }, (_, i) => i)

  // Auto-show results when date and hour are selected
  useEffect(() => {
    if (selectedDate && selectedHour !== '' && !showResults) {
      setShowResults(true)
      setTimeout(() => {
        resultsSectionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
        setTimeout(() => {
          initializeMap()
        }, 600)
      }, 100)
    }
  }, [selectedDate, selectedHour])

  // Fetch events for selected date
  useEffect(() => {
    const fetchDayEvents = async () => {
      if (!selectedDate) {
        setDayEvents(null)
        return
      }

      setLoadingEvents(true)
      try {
        const response = await api.get(`/events/date/${selectedDate}`)
        if (response.data && response.data.events) {
          // Count unique events by name
          const uniqueEventNames = new Set(response.data.events.map(e => e.name))
          const uniqueEventCount = uniqueEventNames.size
          
          setDayEvents({
            ...response.data,
            unique_event_count: uniqueEventCount
          })
        } else {
          setDayEvents(null)
        }
      } catch (error) {
        console.error('Error fetching day events:', error)
        // Set empty events instead of null to prevent UI issues
        setDayEvents({ total_events: 0, unique_event_count: 0, zones_affected: [], events: [] })
      } finally {
        setLoadingEvents(false)
      }
    }

    fetchDayEvents()
  }, [selectedDate])

  // Initialize Leaflet map
  const initializeMap = async () => {
    if (mapInstanceRef.current) return
    
    try {
      const map = L.map(mapRef.current, {
        zoomControl: false,
        zoomAnimation: true,
        fadeAnimation: true,
        markerZoomAnimation: true,
        preferCanvas: false // Use SVG for better quality
      }).setView([47.6205, -122.3321], 12)

      // Uber-style map tiles (light, minimal)
      L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 19,
        updateWhenZooming: false, // Improve zoom performance
        keepBuffer: 2
      }).addTo(map)

      // Add zoom control to bottom right
      L.control.zoom({
        position: 'bottomright'
      }).addTo(map)

      mapInstanceRef.current = map

      await fetchZoneColors()

      ZONES.forEach(zone => {
        addZoneMarker(zone)
      })
    } catch (error) {
      console.error('Error initializing map:', error)
      // Map initialization failed, but don't crash the page
    }
  }

  // Fetch zone colors
  const fetchZoneColors = async () => {
    if (!selectedDate || selectedHour === '') return

    try {
      const hour = parseInt(selectedHour)
      const date = new Date(selectedDate)
      const dayOfWeek = date.getDay() === 0 ? 6 : date.getDay() - 1

      const colors = {}
      
      for (const zone of ZONES) {
        try {
          const response = await api.post('/predict', {
            zone_id: zone.id,
            date: selectedDate,
            hour: hour,
            day_of_week: dayOfWeek
          })
          
          colors[zone.id] = COLORS[response.data.availability_level] || '#666666'
        } catch (error) {
          console.error(`Error fetching color for zone ${zone.id}:`, error)
          colors[zone.id] = '#666666'
        }
      }

      setZoneColors(colors)
    } catch (error) {
      console.error('Error fetching zone colors:', error)
    }
  }

  // Add zone marker
  const addZoneMarker = (zone) => {
    if (!mapInstanceRef.current) return

    const color = zoneColors[zone.id] || '#666666'

    const marker = L.circleMarker([zone.lat, zone.lng], {
      radius: 12,
      fillColor: color,
      color: '#ffffff',
      weight: 3,
      opacity: 1,
      fillOpacity: 0.85,
      className: 'zone-marker',
      pane: 'markerPane' // Ensure proper rendering layer
    }).addTo(mapInstanceRef.current)

    // Enhanced popup with styling
    const popupContent = `
      <div style="text-align: center; padding: 0.5rem;">
        <strong style="font-size: 1rem; color: #0F172A;">${zone.name}</strong>
        <div style="margin-top: 0.5rem; font-size: 0.85rem; color: #64748B;">
          Click to view predictions
        </div>
      </div>
    `
    marker.bindPopup(popupContent, {
      className: 'custom-popup',
      closeButton: false,
      offset: [0, -5]
    })

    // Hover effects - using Leaflet's setStyle for smooth performance
    marker.on('mouseover', function(e) {
      if (!mapInstanceRef.current.dragging.moving() && !mapInstanceRef.current._animatingZoom) {
        this.setStyle({
          radius: 16,
          weight: 4,
          fillOpacity: 1
          // Keep original color - don't change fillColor
        })
        this.openPopup()
      }
    })

    marker.on('mouseout', function(e) {
      if (!mapInstanceRef.current.dragging.moving() && !mapInstanceRef.current._animatingZoom) {
        this.setStyle({
          radius: 12,
          weight: 3,
          fillOpacity: 0.85
          // Keep original color - don't change fillColor
        })
        this.closePopup()
      }
    })

    marker.on('click', () => {
      // Add pulse animation on click
      marker.setStyle({
        radius: 18,
        weight: 5
      })
      setTimeout(() => {
        marker.setStyle({
          radius: 12,
          weight: 3
        })
      }, 200)
      
      handleZoneSelect(zone.id.toString())
    })

    markersRef.current[zone.id] = marker
  }

  // Update marker colors
  useEffect(() => {
    if (Object.keys(zoneColors).length > 0) {
      Object.entries(markersRef.current).forEach(([zoneId, marker]) => {
        const color = zoneColors[parseInt(zoneId)] || '#666666'
        marker.setStyle({ 
          fillColor: color,
          fillOpacity: 0.85
        })
        
        // Add subtle pulse animation when color updates
        marker.setStyle({ fillOpacity: 1 })
        setTimeout(() => {
          marker.setStyle({ fillOpacity: 0.85 })
        }, 300)
      })
    }
  }, [zoneColors])

  // Auto-refresh predictions when date/time changes and zone is selected
  useEffect(() => {
    // Clear selected zone and predictions when date/time changes
    if (selectedZone) {
      setSelectedZone('')
      setPredictions([])
      setEventAlert(null)
    }
    
    // Refresh zone colors on map
    if (selectedDate && selectedHour !== '' && mapInstanceRef.current) {
      fetchZoneColors()
    }
  }, [selectedDate, selectedHour])

  // Handle zone selection
  const handleZoneSelect = async (zoneId) => {
    setSelectedZone(zoneId)
    setLoading(true)
    setPredictions([])
    setEventAlert(null)

    try {
      const hour = parseInt(selectedHour)
      const date = new Date(selectedDate)
      const dayOfWeek = date.getDay() === 0 ? 6 : date.getDay() - 1

      // Fetch events
      let eventsHappening = []
      try {
        const eventsResponse = await api.get(`/events?zone_id=${zoneId}&date=${selectedDate}`)
        const events = eventsResponse.data
        
        eventsHappening = events.filter(event => {
          const eventStart = parseInt(event.start_time.split(':')[0])
          const eventEnd = parseInt(event.end_time.split(':')[0])
          return hour >= eventStart && hour <= eventEnd
        })
        
        if (eventsHappening.length > 0) {
          // Generate reasoning based on events
          const eventTypes = [...new Set(eventsHappening.map(e => e.event_type))]
          const venues = [...new Set(eventsHappening.map(e => e.venue))]
          const totalAttendance = eventsHappening.reduce((sum, e) => {
            const attendance = typeof e.expected_attendance === 'number' 
              ? e.expected_attendance 
              : parseInt(String(e.expected_attendance || '0').replace(/[^0-9]/g, ''))
            return sum + attendance
          }, 0)
          
          let reasoning = ''
          if (eventsHappening.length === 1) {
            const event = eventsHappening[0]
            const attendance = typeof event.expected_attendance === 'number'
              ? event.expected_attendance.toLocaleString()
              : event.expected_attendance
            reasoning = `${event.name} at ${event.venue} is expected to draw ${attendance}+ attendees, significantly increasing parking demand in this zone.`
          } else {
            reasoning = `${eventsHappening.length} events happening simultaneously at ${venues.join(' and ')}, with combined attendance of ${totalAttendance.toLocaleString()}+ people, creating high parking demand.`
          }
          
          setEventAlert({
            eventNames: eventsHappening.map(e => e.name),
            impact: eventsHappening[0].expected_impact,
            reasoning: reasoning
          })
        }
      } catch (error) {
        console.error('Error fetching events:', error)
      }

      const predictionResults = []

      // Fetch predictions for next 4 hours
      for (let i = 0; i < 4; i++) {
        const targetHour = (hour + i) % 24
        
        const response = await api.post('/predict', {
          zone_id: parseInt(zoneId),
          date: selectedDate,
          hour: targetHour,
          day_of_week: dayOfWeek
        })

        const availability = 100 - response.data.predicted_occupancy
        const confidence = response.data.confidence_score * 100
        const predictionScore = response.data.predicted_occupancy
        const availableSpaces = response.data.available_spaces
        const totalSpaces = response.data.total_spaces

        predictionResults.push({
          hour: targetHour,
          availability: availability,
          confidence: confidence,
          predictionScore: predictionScore,
          availabilityLevel: response.data.availability_level,
          availableSpaces: availableSpaces,
          totalSpaces: totalSpaces
        })
      }

      setPredictions(predictionResults)
      
      // Fetch alternative zones if availability is Low or Medium
      const currentAvailability = predictionResults[0].availabilityLevel
      if (currentAvailability === 'Low' || currentAvailability === 'Medium') {
        fetchAlternativeZones(zoneId, currentAvailability, dayOfWeek)
      } else {
        setAlternativeZones([])
      }
    } catch (error) {
      console.error('Error fetching predictions:', error)
      alert('Error loading predictions. Please try again.')
    } finally {
      setLoading(false)
    }
  }
  
  // Fetch alternative zone recommendations
  const fetchAlternativeZones = async (zoneId, availabilityLevel, dayOfWeek) => {
    setLoadingAlternatives(true)
    try {
      const hour = parseInt(selectedHour)
      const response = await api.get('/recommendations', {
        params: {
          zone_id: parseInt(zoneId),
          date: selectedDate,
          hour: hour,
          day_of_week: dayOfWeek,
          availability_level: availabilityLevel,
          max_recommendations: 3,
          max_distance_km: 3.0
        }
      })
      
      setAlternativeZones(response.data || [])
    } catch (error) {
      console.error('Error fetching alternative zones:', error)
      setAlternativeZones([])
    } finally {
      setLoadingAlternatives(false)
    }
  }

  // Format hour
  const formatHour = (hour) => {
    const ampm = hour >= 12 ? 'PM' : 'AM'
    const h = hour % 12 || 12
    return `${h}:00 ${ampm}`
  }

  const selectedZoneName = ZONES.find(z => z.id === parseInt(selectedZone))?.name

  const handleLogout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    navigate('/')
  }

  const user = JSON.parse(localStorage.getItem('user') || '{}')

  return (
    <div className="uber-page">
      {/* Top Navigation */}
      <nav className="top-nav">
        <div className="nav-brand">
          <img src="/logo1.png" alt="FINDR Logo" className="nav-logo-image" />
        </div>
        <div className="nav-user">
          <div className="user-info">
            <div className="user-name">{user.full_name || user.username}</div>
            <div className="user-email">{user.email}</div>
          </div>
          <button className="logout-btn" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="uber-hero">
        <div className="uber-container">
          <div className="hero-header">
            <div className="hero-text">
              <h1 className="uber-title animate-fade-in">Find Your Spot in Seattle</h1>
              <p className="uber-subtitle animate-fade-in-delay">AI-powered predictions for smarter parking decisions</p>
            </div>
            <div className="hero-stats">
              <div className="stat-card animate-slide-up" style={{animationDelay: '0.1s'}}>
                <div className="stat-icon"></div>
                <div className="stat-number">10</div>
                <div className="stat-label">Zones</div>
              </div>
              <div className="stat-card animate-slide-up" style={{animationDelay: '0.2s'}}>
                <div className="stat-icon"></div>
                <div className="stat-number">24/7</div>
                <div className="stat-label">Live Data</div>
              </div>
            </div>
          </div>
          
          {/* Input Card */}
          <div className="uber-input-card animate-scale-in">
            <div className="input-header">
              <span className="input-icon animate-bounce"></span>
              <h3>When do you need parking?</h3>
            </div>
            <div className="uber-input-group">
              <div className="input-wrapper">
                <label className="uber-label">Date</label>
                <input
                  type="date"
                  className="uber-input"
                  value={selectedDate}
                  onChange={(e) => setSelectedDate(e.target.value)}
                  placeholder="Select date"
                />
              </div>
              <div className="input-wrapper">
                <label className="uber-label">Time</label>
                <select
                  className="uber-input"
                  value={selectedHour}
                  onChange={(e) => setSelectedHour(e.target.value)}
                >
                  <option value="">Select time</option>
                  {hourOptions.map(hour => (
                    <option key={hour} value={hour}>
                      {formatHour(hour)}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            {selectedDate && selectedHour !== '' && (
              <div className="search-info animate-slide-in">
                <span className="info-icon animate-pulse"></span>
                <span>Searching for parking on {new Date(selectedDate).toLocaleDateString()} at {formatHour(parseInt(selectedHour))}</span>
              </div>
            )}
            
            {/* Quick Tips */}
            {!selectedDate || selectedHour === '' ? (
              <div className="quick-tips animate-fade-in-slow">
                <div className="tip-icon"></div>
                <div className="tip-content">
                  <h4>Pro Tips</h4>
                  <ul>
                    <li>Early morning (6-8 AM) usually has best availability</li>
                    <li>Check for events that might affect parking</li>
                    <li>Green zones indicate high availability</li>
                  </ul>
                </div>
              </div>
            ) : null}
          </div>
        </div>
      </section>

      {/* Results Section */}
      {showResults && (
        <section className="uber-results" ref={resultsSectionRef}>
          <div className="uber-container-full">
            <div className="uber-split">
              {/* Map Side */}
              <div className="uber-map-side">
                <div className="uber-map-header">
                  <h2>Available zones</h2>
                  <div className="uber-legend">
                    <span className="uber-legend-item">
                      <span className="uber-dot" style={{background: '#05A357'}}></span>
                      High
                    </span>
                    <span className="uber-legend-item">
                      <span className="uber-dot" style={{background: '#FFC043'}}></span>
                      Medium
                    </span>
                    <span className="uber-legend-item">
                      <span className="uber-dot" style={{background: '#CD0000'}}></span>
                      Low
                    </span>
                  </div>
                </div>
                <div ref={mapRef} className="uber-map"></div>
              </div>

              {/* Details Side */}
              <div className="uber-details-side">
                {/* Events for Selected Date - Always show when date/time selected */}
                {selectedDate && selectedHour !== '' && dayEvents && dayEvents.total_events > 0 && (
                  <div className="day-events-card animate-bounce-in">
                    <div className="events-header">
                      <div className="events-title">
                        <span className="events-icon"></span>
                        <h4>{dayEvents.unique_event_count || dayEvents.total_events} Event{(dayEvents.unique_event_count || dayEvents.total_events) > 1 ? 's' : ''} Today</h4>
                      </div>
                      <span className="events-badge">{dayEvents.zones_affected.length} zones affected</span>
                    </div>
                    
                    {/* Group events by venue/area */}
                    {(() => {
                      const eventsByVenue = {}
                      dayEvents.events.forEach(event => {
                        if (!eventsByVenue[event.venue]) {
                          eventsByVenue[event.venue] = []
                        }
                        eventsByVenue[event.venue].push(event)
                      })
                      
                      return Object.entries(eventsByVenue).map(([venue, events], venueIndex) => {
                        const highestImpact = events.reduce((max, e) => {
                          const impacts = { 'very high': 4, 'high': 3, 'medium': 2, 'low': 1 }
                          const current = impacts[e.expected_impact.toLowerCase()] || 0
                          const maxVal = impacts[max.toLowerCase()] || 0
                          return current > maxVal ? e.expected_impact : max
                        }, 'low')
                        
                        const affectedZoneIds = [...new Set(events.map(e => e.zone_id))].sort()
                        const affectedZoneNames = affectedZoneIds.map(id => {
                          const zone = ZONES.find(z => z.id === id)
                          return zone ? zone.name : `Zone ${id}`
                        })
                        
                        // Deduplicate events by event name (same event shown for multiple zones)
                        const uniqueEvents = []
                        const seenEventNames = new Set()
                        events.forEach(event => {
                          if (!seenEventNames.has(event.name)) {
                            seenEventNames.add(event.name)
                            uniqueEvents.push(event)
                          }
                        })
                        
                        // Generate reasoning for this venue
                        const totalAttendance = uniqueEvents.reduce((sum, e) => {
                          const attendance = typeof e.expected_attendance === 'number'
                            ? e.expected_attendance
                            : parseInt(String(e.expected_attendance || '0').replace(/[^0-9]/g, ''))
                          return sum + attendance
                        }, 0)
                        
                        let reasoning = ''
                        if (uniqueEvents.length === 1) {
                          const event = uniqueEvents[0]
                          const attendance = typeof event.expected_attendance === 'number'
                            ? event.expected_attendance.toLocaleString()
                            : event.expected_attendance
                          reasoning = `${event.name} is expected to draw ${attendance}+ attendees, significantly increasing parking demand in nearby zones.`
                        } else {
                          reasoning = `${uniqueEvents.length} events at this venue with combined attendance of ${totalAttendance.toLocaleString()}+ people will create high parking demand.`
                        }
                        
                        return (
                          <div key={venueIndex} className="venue-event-group-compact animate-slide-in-left" style={{animationDelay: `${venueIndex * 0.1}s`}}>
                            {/* Compact Venue Header */}
                            <div className="venue-header-compact">
                              <div className="venue-info-compact">
                                <span className="venue-icon-small"></span>
                                <span className="venue-name-compact">{venue}</span>
                                <span className="venue-zones-compact" title={affectedZoneNames.join(', ')}>
                                  {affectedZoneNames.length === 1 
                                    ? affectedZoneNames[0]
                                    : `${affectedZoneNames.length} zones affected`}
                                </span>
                              </div>
                              <div className={`venue-impact-compact impact-${highestImpact.toLowerCase().replace(' ', '-')}`}>
                                {highestImpact}
                              </div>
                            </div>
                            
                            {/* Compact Events List */}
                            <div className="venue-events-compact">
                              {uniqueEvents.map((event, eventIndex) => (
                                <div key={eventIndex} className="event-row-compact">
                                  <span className="event-type-icon-small">
                                    {event.event_type === 'sports' && ''}
                                    {event.event_type === 'concert' && ''}
                                    {event.event_type === 'festival' && ''}
                                    {event.event_type === 'conference' && ''}
                                    {event.event_type === 'celebration' && ''}
                                  </span>
                                  <span className="event-name-compact">{event.name}</span>
                                  <span className="event-time-compact">{event.start_time}</span>
                                </div>
                              ))}
                            </div>
                            
                            {/* Compact Alert */}
                            <div className="venue-alert-compact">
                              <span className="alert-icon-small"></span>
                              <span className="alert-text-compact">
                                {highestImpact.toLowerCase() === 'very high' && 'Arrive 2+ hours early'}
                                {highestImpact.toLowerCase() === 'high' && 'Arrive 1+ hour early'}
                                {highestImpact.toLowerCase() === 'medium' && 'Arrive 30-45 min early'}
                                {highestImpact.toLowerCase() === 'low' && 'Normal arrival time OK'}
                              </span>
                            </div>
                            
                            {/* Compact Forecast */}
                            <div className="venue-forecast-compact">
                              <span className="forecast-label-compact">Occupancy:</span>
                              <span className="forecast-value-compact">
                                {highestImpact.toLowerCase() === 'very high' && '90-100%'}
                                {highestImpact.toLowerCase() === 'high' && '75-90%'}
                                {highestImpact.toLowerCase() === 'medium' && '60-75%'}
                                {highestImpact.toLowerCase() === 'low' && '50-60%'}
                              </span>
                            </div>
                            
                            {/* Reasoning - shown once per venue */}
                            <div className="venue-reasoning-compact">
                              <span className="reasoning-icon-small"></span>
                              <div className="reasoning-content-compact">
                                <div className="reasoning-zones">
                                  <strong>Affected zones:</strong> {affectedZoneNames.join(', ')}
                                </div>
                                <div className="reasoning-text-compact">{reasoning}</div>
                              </div>
                            </div>
                          </div>
                        )
                      })
                    })()}
                  </div>
                )}
                
                {!selectedZone && (
                  <div className="uber-empty-state">
                    <div className="uber-empty-icon animate-bounce-slow"></div>
                    <h3>Select a zone</h3>
                    <p>Click on a zone marker or choose from the list below</p>
                    
                    <div className="uber-zone-list">
                      {ZONES.map((zone, index) => (
                        <button
                          key={zone.id}
                          className="uber-zone-button animate-slide-in-left"
                          style={{animationDelay: `${index * 0.05}s`}}
                          onClick={() => handleZoneSelect(zone.id.toString())}
                        >
                          <span className="uber-zone-name">{zone.name}</span>
                          <span 
                            className="uber-zone-indicator animate-pulse-slow"
                            style={{background: zoneColors[zone.id] || '#666666'}}
                          ></span>
                        </button>
                      ))}
                    </div>
                  </div>
                )}

                {loading && (
                  <div className="uber-loading">
                    <div className="uber-spinner"></div>
                    <p>Loading predictions...</p>
                  </div>
                )}

                {!loading && eventAlert && (
                  <div className="uber-alert animate-bounce-in">
                    <div className="uber-alert-icon"></div>
                    <div className="uber-alert-content">
                      <h4>Event Nearby!</h4>
                      <p className="event-name">{eventAlert.eventNames.join(', ')}</p>
                      <p className="event-impact">
                        <span className="impact-badge">
                          {eventAlert.impact === 'very high' && 'Very High Impact'}
                          {eventAlert.impact === 'high' && 'High Impact'}
                          {eventAlert.impact === 'medium' && 'Medium Impact'}
                          {eventAlert.impact === 'low' && 'Low Impact'}
                        </span>
                        <span className="impact-text">
                          {eventAlert.impact === 'very high' && 'Parking will be extremely limited due to major event'}
                          {eventAlert.impact === 'high' && 'Parking will be very limited due to event'}
                          {eventAlert.impact === 'medium' && 'Parking may be challenging due to event'}
                          {eventAlert.impact === 'low' && 'Slight parking reduction due to event'}
                        </span>
                      </p>
                      {eventAlert.reasoning && (
                        <div className="event-reasoning">
                          <span className="reasoning-icon"></span>
                          <span className="reasoning-text">{eventAlert.reasoning}</span>
                        </div>
                      )}
                    </div>
                  </div>
                )}

                {!loading && predictions.length > 0 && (
                  <div className="uber-predictions">
                    <div className="uber-predictions-header">
                      <div className="predictions-header-content">
                        <h2>{selectedZoneName}</h2>
                        <button 
                          className="change-zone-btn"
                          onClick={() => {
                            setSelectedZone('')
                            setPredictions([])
                            setAlternativeZones([])
                            setEventAlert(null)
                          }}
                        >
                          ← Change Zone
                        </button>
                      </div>
                    </div>

                    <div className="uber-predictions-grid">
                      {predictions.map((pred, index) => {
                        const levelColor = COLORS[pred.availabilityLevel]
                        
                        return (
                          <div key={index} className="uber-prediction-card">
                            <div className="uber-card-header">
                              <span className="uber-card-time">{formatHour(pred.hour)}</span>
                              <span 
                                className="uber-card-badge"
                                style={{background: levelColor}}
                              >
                                {pred.availabilityLevel}
                              </span>
                            </div>
                            <div className="uber-card-body">
                              <div className="uber-card-main">
                                <span className="uber-card-number">{pred.availableSpaces}</span>
                                <span className="uber-card-label">/ {pred.totalSpaces} spaces</span>
                              </div>
                              <div className="uber-card-sub">
                                {pred.predictionScore.toFixed(0)}% occupied
                              </div>
                            </div>
                          </div>
                        )
                      })}
                    </div>
                    
                    {/* Alternative Zone Recommendations */}
                    {!loadingAlternatives && alternativeZones.length > 0 && (
                      <div className="alternative-zones-card animate-slide-in-up">
                        <div className="alternatives-header">
                          <div className="alternatives-title">
                            <span className="alternatives-icon">💡</span>
                            <h4>Better Options Nearby</h4>
                          </div>
                          <span className="alternatives-subtitle">ML-powered recommendations</span>
                        </div>
                        
                        <div className="alternatives-list">
                          {alternativeZones.map((zone, index) => (
                            <div 
                              key={zone.zone_id} 
                              className="alternative-zone-row animate-fade-in"
                              style={{animationDelay: `${index * 0.1}s`}}
                            >
                              <div className="alt-zone-main">
                                <div className="alt-zone-info">
                                  <span className="alt-zone-name">{zone.zone_name}</span>
                                  <span className="alt-zone-reason">{zone.reason}</span>
                                </div>
                                <div className="alt-zone-metrics">
                                  <span className="alt-zone-distance">
                                    <span className="distance-icon">📍</span>
                                    {zone.distance_display}
                                  </span>
                                  <span 
                                    className="alt-availability-badge"
                                    style={{background: COLORS[zone.availability_level]}}
                                  >
                                    {zone.availability_level}
                                  </span>
                                </div>
                              </div>
                              <button 
                                className="alt-zone-button"
                                onClick={() => handleZoneSelect(zone.zone_id.toString())}
                              >
                                View
                              </button>
                            </div>
                          ))}
                        </div>
                        
                        <div className="alternatives-footer">
                          <span className="alternatives-note">
                            Recommendations based on real-time ML predictions and proximity
                          </span>
                        </div>
                      </div>
                    )}
                    
                    {loadingAlternatives && (
                      <div className="alternatives-loading">
                        <div className="uber-spinner-small"></div>
                        <span>Finding better options...</span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          </div>
        </section>
      )}
    </div>
  )
}

export default MainPage
