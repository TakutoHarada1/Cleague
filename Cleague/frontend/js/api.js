/**
 * API client for fetching standings data from the backend.
 */

// API base URL - adjust for production deployment
const API_BASE_URL = 'http://localhost:5000/api';

/**
 * Fetch standings data from the API.
 *
 * @param {Object} params - Query parameters
 * @param {number} params.year - Year (optional)
 * @param {number} params.startMonth - Start month (optional)
 * @param {number} params.endMonth - End month (optional)
 * @returns {Promise<Object>} Standings response with period and data
 * @throws {Error} If the API request fails
 */
async function fetchStandings(params = {}) {
    const queryParams = new URLSearchParams();
    
    if (params.year) queryParams.append('year', params.year);
    if (params.startMonth) queryParams.append('startMonth', params.startMonth);
    if (params.endMonth) queryParams.append('endMonth', params.endMonth);
    
    const url = `${API_BASE_URL}/standings${queryParams.toString() ? '?' + queryParams.toString() : ''}`;
    
    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error?.message || `HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        if (error instanceof TypeError) {
            throw new Error('Network error: Could not connect to API server');
        }
        throw error;
    }
}

/**
 * Fetch team information from the API.
 *
 * @returns {Promise<Array>} Array of team objects
 * @throws {Error} If the API request fails
 */
async function fetchTeams() {
    const url = `${API_BASE_URL}/teams`;
    
    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const teams = await response.json();
        return teams;
    } catch (error) {
        if (error instanceof TypeError) {
            throw new Error('Network error: Could not connect to API server');
        }
        throw error;
    }
}