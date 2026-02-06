import api from './api'

export const getZones = async () => {
  const response = await api.get('/zones')
  return response.data
}

export const getZone = async (zoneId) => {
  const response = await api.get(`/zones/${zoneId}`)
  return response.data
}

export const getEvents = async (zoneId = null, date = null) => {
  const params = {}
  if (zoneId) params.zone_id = zoneId
  if (date) params.date = date
  
  const response = await api.get('/events', { params })
  return response.data
}

export const predictAvailability = async (predictionData) => {
  const response = await api.post('/predict', predictionData)
  return response.data
}
