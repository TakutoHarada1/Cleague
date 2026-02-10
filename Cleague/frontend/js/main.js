/**
 * Main entry point for the application.
 * Handles page load and initialization.
 */

document.addEventListener('DOMContentLoaded', async () => {
    console.log('Central League Standings Graph - Application loaded');
    
    // Get DOM elements
    const canvas = document.getElementById('standingsChart');
    const loadingEl = document.getElementById('loading');
    const errorEl = document.getElementById('error');
    
    // Initialize chart
    const chart = initChart(canvas);
    
    // Load default graph (current season)
    await loadDefaultGraph(chart, loadingEl, errorEl);
});

/**
 * Load and display the default graph (current season).
 *
 * @param {Chart} chart - Chart.js instance
 * @param {HTMLElement} loadingEl - Loading indicator element
 * @param {HTMLElement} errorEl - Error message element
 */
async function loadDefaultGraph(chart, loadingEl, errorEl) {
    try {
        // Show loading indicator
        loadingEl.classList.remove('hidden');
        errorEl.classList.add('hidden');
        errorEl.textContent = '';
        
        // Get URL parameters
        const urlParams = parseUrlParams();
        
        // Fetch teams data
        const teams = await fetchTeams();
        
        // Fetch standings data
        const standingsData = await fetchStandings({
            year: urlParams.year,
            startMonth: urlParams.startMonth,
            endMonth: urlParams.endMonth
        });
        
        // Transform data for Chart.js
        const chartData = createChartData(standingsData, teams);
        
        // Update chart
        updateChart(chart, chartData);
        
        // Hide loading indicator
        loadingEl.classList.add('hidden');
        
        console.log('Graph loaded successfully');
        
    } catch (error) {
        console.error('Failed to load graph:', error);
        
        // Hide loading indicator
        loadingEl.classList.add('hidden');
        
        // Show error message
        errorEl.textContent = `エラー: ${error.message}`;
        errorEl.classList.remove('hidden');
    }
}