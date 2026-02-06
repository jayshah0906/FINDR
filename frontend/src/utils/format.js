export const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

export const formatTime = (hour) => {
  const period = hour >= 12 ? 'PM' : 'AM'
  const displayHour = hour % 12 || 12
  return `${displayHour}:00 ${period}`
}

export const formatConfidence = (score) => {
  return `${Math.round(score * 100)}%`
}

export const formatOccupancy = (occupancy) => {
  return `${occupancy.toFixed(1)}%`
}
