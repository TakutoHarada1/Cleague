"""
Flask API server for Central League standings data.
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, date
from typing import Optional
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from models import TEAMS, StandingsData
from scraper import fetch_npb_standings
from parser import parse_standings_html

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access


@app.route('/api/standings', methods=['GET'])
def get_standings():
    """Get standings data - MOCK VERSION for testing"""
    try:
        year = request.args.get('year', type=int)
        if year is None:
            year = datetime.now().year
        
        # モックデータを返す
        from datetime import timedelta
        
        mock_data = []
        base_date = date(year, 3, 20)
        
        # 10日分のモックデータを生成
        for day in range(10):
            current_date = base_date + timedelta(days=day)
            date_str = current_date.isoformat()
            
            # 各球団のモックデータ
            teams_data = [
                {"teamId": "giants", "rank": 1, "wins": 5+day, "losses": 3, "draws": 0, "winRate": 0.625, "gamesBehind": 0.0},
                {"teamId": "tigers", "rank": 2, "wins": 4+day, "losses": 4, "draws": 0, "winRate": 0.500, "gamesBehind": 1.0},
                {"teamId": "carp", "rank": 3, "wins": 4+day, "losses": 5, "draws": 0, "winRate": 0.444, "gamesBehind": 1.5},
                {"teamId": "baystars", "rank": 4, "wins": 3+day, "losses": 5, "draws": 0, "winRate": 0.375, "gamesBehind": 2.0},
                {"teamId": "dragons", "rank": 5, "wins": 3+day, "losses": 6, "draws": 0, "winRate": 0.333, "gamesBehind": 2.5},
                {"teamId": "swallows", "rank": 6, "wins": 2+day, "losses": 6, "draws": 0, "winRate": 0.250, "gamesBehind": 3.0},
            ]
            
            for team_data in teams_data:
                team_data["date"] = date_str
                mock_data.append(team_data)
        
        response = {
            'period': {
                'year': year,
                'startDate': f"{year}-03-20",
                'endDate': f"{year}-03-29",
                'startMonth': None,
                'endMonth': None
            },
            'data': mock_data
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'error': {
                'code': 'INTERNAL_ERROR',
                'message': 'An unexpected error occurred',
                'details': str(e)
            }
        }), 500


@app.route('/api/teams', methods=['GET'])
def get_teams():
    """Get all Central League teams."""
    teams_list = []
    for team in TEAMS:
        teams_list.append({
            'id': team.id,
            'name': team.name,
            'shortName': team.short_name,
            'color': team.color,
            'league': team.league
        })
    return jsonify(teams_list)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)