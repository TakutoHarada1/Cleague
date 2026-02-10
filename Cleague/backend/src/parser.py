"""
HTML parser for NPB standings data.
"""
from typing import List
from bs4 import BeautifulSoup
from models import StandingsData, TEAMS


def parse_standings_html(html: str, date: str) -> List[StandingsData]:
    """
    Parse NPB standings HTML and extract standings data.
    
    Args:
        html: HTML content from NPB website
        date: Date of the standings data (ISO 8601 format)
        
    Returns:
        List of StandingsData objects for all teams
        
    Raises:
        ValueError: If HTML structure is unexpected
    """
    soup = BeautifulSoup(html, 'html.parser')
    standings_list = []
    
    # Find the standings table
    # Note: Actual NPB website structure may vary - this is a generic implementation
    table = soup.find('table', class_='standing_table')
    if not table:
        # Try alternative selectors
        table = soup.find('table', id='standingTable')
    
    if not table:
        raise ValueError("Could not find standings table in HTML")
    
    # Parse table rows
    rows = table.find_all('tr')[1:]  # Skip header row
    
    for rank, row in enumerate(rows, start=1):
        cols = row.find_all('td')
        if len(cols) < 5:
            continue
        
        try:
            # Extract team name and match to our TEAMS list
            team_name = cols[0].get_text(strip=True)
            team_id = _match_team_name(team_name)
            
            # Extract statistics
            wins = int(cols[1].get_text(strip=True))
            losses = int(cols[2].get_text(strip=True))
            draws = int(cols[3].get_text(strip=True))
            win_rate = float(cols[4].get_text(strip=True))
            
            # Calculate games behind (if available, otherwise calculate)
            games_behind = 0.0
            if len(cols) > 5:
                gb_text = cols[5].get_text(strip=True)
                if gb_text and gb_text != '-':
                    games_behind = float(gb_text)
            
            standings_data = StandingsData(
                date=date,
                team_id=team_id,
                rank=rank,
                wins=wins,
                losses=losses,
                draws=draws,
                win_rate=win_rate,
                games_behind=games_behind
            )
            standings_list.append(standings_data)
            
        except (ValueError, IndexError) as e:
            raise ValueError(f"Failed to parse row {rank}: {str(e)}")
    
    if len(standings_list) != 6:
        raise ValueError(f"Expected 6 teams, found {len(standings_list)}")
    
    return standings_list


def _match_team_name(team_name: str) -> str:
    """
    Match a team name from HTML to our team ID.
    
    Args:
        team_name: Team name from HTML
        
    Returns:
        Team ID
        
    Raises:
        ValueError: If team name cannot be matched
    """
    # Normalize team name
    team_name = team_name.strip()
    
    # Try to match by short name or full name
    for team in TEAMS:
        if team.short_name in team_name or team_name in team.name:
            return team.id
    
    # Fallback: try partial matches
    name_mapping = {
        '巨人': 'giants',
        'ジャイアンツ': 'giants',
        '阪神': 'tigers',
        'タイガース': 'tigers',
        '中日': 'dragons',
        'ドラゴンズ': 'dragons',
        '広島': 'carp',
        'カープ': 'carp',
        'DeNA': 'baystars',
        'ベイスターズ': 'baystars',
        'ヤクルト': 'swallows',
        'スワローズ': 'swallows'
    }
    
    for key, team_id in name_mapping.items():
        if key in team_name:
            return team_id
    
    raise ValueError(f"Could not match team name: {team_name}")