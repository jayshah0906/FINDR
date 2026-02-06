import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { getZone, getEvents } from '../services/predictionApi'
import PredictionCard from '../components/PredictionCard'
import TimePicker from '../components/TimePicker'
import { usePrediction } from '../hooks/usePrediction'
import './ZoneDetail.css'

const ZoneDetail = () => {
  const { zoneId } = useParams()
  const [zone, setZone] = useState(null)
  const [events, setEvents] = useState([])
  const [date, setDate] = useState(new Date().toISOString().split('T')[0])
  const [hour, setHour] = useState(new Date().getHours())
  const [dayOfWeek, setDayOfWeek] = useState(new Date().getDay() === 0 ? 6 : new Date().getDay() - 1)
  
  const { makePrediction, loading, error, prediction } = usePrediction()

  useEffect(() => {
    loadZoneData()
  }, [zoneId])

  useEffect(() => {
    if (zoneId && date && hour !== null && dayOfWeek !== null) {
      makePrediction(Number(zoneId), date, hour, dayOfWeek)
      loadEvents()
    }
  }, [zoneId, date, hour, dayOfWeek])

  const loadZoneData = async () => {
    try {
      const zoneData = await getZone(zoneId)
      setZone(zoneData)
    } catch (err) {
      console.error('Failed to load zone:', err)
    }
  }

  const loadEvents = async () => {
    try {
      const eventsData = await getEvents(Number(zoneId), date)
      setEvents(eventsData)
    } catch (err) {
      console.error('Failed to load events:', err)
    }
  }

  const handleDateChange = (newDate) => {
    setDate(newDate)
    const selectedDate = new Date(newDate)
    const day = selectedDate.getDay() === 0 ? 6 : selectedDate.getDay() - 1
    setDayOfWeek(day)
  }

  if (!zone) {
    return <div className="zone-detail loading">Loading zone details...</div>
  }

  return (
    <div className="zone-detail">
      <div className="zone-detail-container">
        <div className="zone-header">
          <h1>{zone.name}</h1>
          <p>Location: {zone.lat.toFixed(4)}, {zone.lng.toFixed(4)}</p>
        </div>

        <div className="zone-content">
          <div className="zone-left">
            <div className="time-selection">
              <h2>Select Time</h2>
              <TimePicker
                date={date}
                hour={hour}
                dayOfWeek={dayOfWeek}
                onDateChange={handleDateChange}
                onHourChange={setHour}
                onDayChange={setDayOfWeek}
              />
            </div>

            {events.length > 0 && (
              <div className="events-section">
                <h2>Upcoming Events</h2>
                <div className="events-list">
                  {events.map((event) => (
                    <div key={event.id} className="event-card">
                      <h3>{event.name}</h3>
                      <p>
                        {event.start_time} - {event.end_time}
                      </p>
                      <span className={`event-impact impact-${event.expected_impact.toLowerCase()}`}>
                        {event.expected_impact} Impact
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          <div className="zone-right">
            <PredictionCard
              prediction={prediction}
              loading={loading}
              error={error}
            />
          </div>
        </div>
      </div>
    </div>
  )
}

export default ZoneDetail
