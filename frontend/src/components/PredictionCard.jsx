import React from 'react'
import AvailabilityBadge from './AvailabilityBadge'
import { formatConfidence, formatOccupancy, formatTime } from '../utils/format'
import './PredictionCard.css'

const PredictionCard = ({ prediction, loading, error }) => {
  if (loading) {
    return (
      <div className="prediction-card loading">
        <div className="loading-spinner"></div>
        <p>Predicting availability...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="prediction-card error">
        <h3>Error</h3>
        <p>{error}</p>
      </div>
    )
  }

  if (!prediction) {
    return (
      <div className="prediction-card empty">
        <p>Select a zone and time to get predictions</p>
      </div>
    )
  }

  return (
    <div className="prediction-card">
      <div className="prediction-header">
        <h2>{prediction.zone_name}</h2>
        <AvailabilityBadge level={prediction.availability_level} />
      </div>

      <div className="prediction-stats">
        <div className="stat">
          <span className="stat-label">Predicted Occupancy</span>
          <span className="stat-value">{formatOccupancy(prediction.predicted_occupancy)}</span>
        </div>
        <div className="stat">
          <span className="stat-label">Confidence Score</span>
          <span className="stat-value">{formatConfidence(prediction.confidence_score)}</span>
        </div>
      </div>

      <div className="prediction-factors">
        <h3>Factors</h3>
        <div className="factors-grid">
          <div className="factor">
            <span className="factor-label">Time of Day:</span>
            <span className="factor-value">{prediction.factors.time_of_day || 'N/A'}</span>
          </div>
          <div className="factor">
            <span className="factor-label">Weekend:</span>
            <span className="factor-value">{prediction.factors.is_weekend ? 'Yes' : 'No'}</span>
          </div>
          <div className="factor">
            <span className="factor-label">Traffic Level:</span>
            <span className="factor-value">{prediction.factors.traffic_level || 'N/A'}</span>
          </div>
          <div className="factor">
            <span className="factor-label">Events Nearby:</span>
            <span className="factor-value">{prediction.factors.events_nearby || 0}</span>
          </div>
        </div>
      </div>

      <div className="prediction-timestamp">
        <small>Prediction for: {new Date(prediction.timestamp).toLocaleString()}</small>
      </div>
    </div>
  )
}

export default PredictionCard
