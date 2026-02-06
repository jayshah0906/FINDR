import React from 'react'
import './ZoneSelector.css'

const ZoneSelector = ({ zones, selectedZone, onZoneChange }) => {
  return (
    <div className="zone-selector">
      <label htmlFor="zone-select" className="zone-selector-label">
        Select Zone:
      </label>
      <select
        id="zone-select"
        className="zone-selector-select"
        value={selectedZone || ''}
        onChange={(e) => onZoneChange(Number(e.target.value))}
      >
        <option value="">Choose a zone...</option>
        {zones.map((zone) => (
          <option key={zone.id} value={zone.id}>
            {zone.name}
          </option>
        ))}
      </select>
    </div>
  )
}

export default ZoneSelector
