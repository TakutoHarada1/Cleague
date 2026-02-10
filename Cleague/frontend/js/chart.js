/**
 * Chart.js configuration and rendering functions.
 */

let chartInstance = null;

/**
 * Transform API response data to Chart.js format.
 *
 * @param {Object} apiResponse - Response from /api/standings
 * @param {Array} teams - Array of team objects from /api/teams
 * @returns {Object} Chart.js data object
 */
function createChartData(apiResponse, teams) {
    // Group data by date
    const dateMap = new Map();
    
    apiResponse.data.forEach(item => {
        if (!dateMap.has(item.date)) {
            dateMap.set(item.date, {});
        }
        dateMap.get(item.date)[item.teamId] = item.rank;
    });
    
    // Sort dates
    const dates = Array.from(dateMap.keys()).sort();
    
    // Create datasets for each team
    const datasets = teams.map(team => {
        const data = dates.map(date => {
            const dayData = dateMap.get(date);
            return dayData[team.id] || null;
        });
        
        return {
            label: team.shortName,
            data: data,
            borderColor: team.color,
            backgroundColor: hexToRgba(team.color, 0.1),
            tension: 0.1,
            pointRadius: 3,
            pointHoverRadius: 5,
            borderWidth: 2
        };
    });
    
    return {
        labels: dates,
        datasets: datasets
    };
}

/**
 * Convert hex color to rgba.
 *
 * @param {string} hex - Hex color code
 * @param {number} alpha - Alpha value (0-1)
 * @returns {string} RGBA color string
 */
function hexToRgba(hex, alpha) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

/**
 * Initialize the Chart.js instance with proper configuration.
 *
 * @param {HTMLCanvasElement} canvas - Canvas element for the chart
 * @returns {Chart} Chart.js instance
 */
function initChart(canvas) {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: []
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    reverse: true,  // Rank 1 at top
                    min: 1,
                    max: 6,
                    ticks: {
                        stepSize: 1,
                        callback: function(value) {
                            return value + '位';
                        }
                    },
                    title: {
                        display: true,
                        text: '順位'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: '日付'
                    },
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45
                    }
                }
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    onClick: setupLegendClickHandler()
                },
                tooltip: setupTooltipConfig()
            },
            interaction: {
                mode: 'index',
                intersect: false
            }
        }
    };
    
    chartInstance = new Chart(canvas, config);
    return chartInstance;
}

/**
 * Setup legend click handler to toggle team visibility.
 *
 * @returns {Function} Legend click handler
 */
function setupLegendClickHandler() {
    return function(e, legendItem, legend) {
        const index = legendItem.datasetIndex;
        const chart = legend.chart;
        const meta = chart.getDatasetMeta(index);
        
        // Toggle visibility
        meta.hidden = meta.hidden === null ? !chart.data.datasets[index].hidden : null;
        chart.update();
    };
}

/**
 * Setup tooltip configuration.
 *
 * @returns {Object} Tooltip configuration
 */
function setupTooltipConfig() {
    return {
        callbacks: {
            title: function(context) {
                return '日付: ' + context[0].label;
            },
            label: function(context) {
                const teamName = context.dataset.label;
                const rank = context.parsed.y;
                return `${teamName}: ${rank}位`;
            },
            afterLabel: function(context) {
                // Could add wins/losses here if available in data
                return '';
            }
        }
    };
}

/**
 * Update the chart with new data.
 *
 * @param {Chart} chart - Chart.js instance
 * @param {Object} data - Chart data in Chart.js format
 */
function updateChart(chart, data) {
    chart.data.labels = data.labels;
    chart.data.datasets = data.datasets;
    chart.update();
}