/**
 * Utility functions for date calculations and URL parameter parsing.
 */

/**
 * Get the current season's start and end dates.
 * NPB season typically runs from late March to early October.
 * 
 * @returns {Object} Object with startDate and endDate in ISO 8601 format
 */
function getCurrentSeasonDates() {
    const now = new Date();
    const year = now.getFullYear();
    
    // Season starts around March 20
    const startDate = `${year}-03-20`;
    
    // If we're past October, use October 10 as end date
    // Otherwise, use today's date
    const endDate = now.getMonth() >= 9 ? `${year}-10-10` : now.toISOString().split('T')[0];
    
    return { startDate, endDate, year };
}

/**
 * Parse URL query parameters.
 * 
 * @returns {Object} Object with year, startMonth, endMonth parameters
 */
function parseUrlParams() {
    const params = new URLSearchParams(window.location.search);
    
    return {
        year: params.get('year') ? parseInt(params.get('year'), 10) : null,
        startMonth: params.get('startMonth') ? parseInt(params.get('startMonth'), 10) : null,
        endMonth: params.get('endMonth') ? parseInt(params.get('endMonth'), 10) : null
    };
}