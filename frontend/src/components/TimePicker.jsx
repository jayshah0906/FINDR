import React from 'react'
import { DAYS_OF_WEEK } from '../utils/constants'
import './TimePicker.css'

const TimePicker = ({ date, hour, dayOfWeek, onDateChange, onHourChange, onDayChange }) => {
  const hours = Array.from({ length: 24 }, (_, i) => i)

  return (
    <div className="time-picker">
      <div className="time-picker-group">
        <label htmlFor="date-input" className="time-picker-label">
          Date:
        </label>
        <input
          id="date-input"
          type="date"
          className="time-picker-input"
          value={date}
          onChange={(e) => onDateChange(e.target.value)}
          min={new Date().toISOString().split('T')[0]}
        />
      </div>

      <div className="time-picker-group">
        <label htmlFor="day-select" className="time-picker-label">
          Day of Week:
        </label>
        <select
          id="day-select"
          className="time-picker-select"
          value={dayOfWeek}
          onChange={(e) => onDayChange(Number(e.target.value))}
        >
          {DAYS_OF_WEEK.map((day, index) => (
            <option key={index} value={index}>
              {day}
            </option>
          ))}
        </select>
      </div>

      <div className="time-picker-group">
        <label htmlFor="hour-select" className="time-picker-label">
          Hour:
        </label>
        <select
          id="hour-select"
          className="time-picker-select"
          value={hour}
          onChange={(e) => onHourChange(Number(e.target.value))}
        >
          {hours.map((h) => (
            <option key={h} value={h}>
              {h.toString().padStart(2, '0')}:00
            </option>
          ))}
        </select>
      </div>
    </div>
  )
}

export default TimePicker
