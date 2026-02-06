import React from 'react'
import { AVAILABILITY_COLORS, AVAILABILITY_LABELS } from '../utils/constants'
import './AvailabilityBadge.css'

const AvailabilityBadge = ({ level }) => {
  const color = AVAILABILITY_COLORS[level] || '#6b7280'
  const label = AVAILABILITY_LABELS[level] || level

  return (
    <span className="availability-badge" style={{ backgroundColor: color }}>
      {label}
    </span>
  )
}

export default AvailabilityBadge
