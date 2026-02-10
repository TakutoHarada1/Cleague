"""
Data models for Central League standings application.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Team:
    """Represents a baseball team in the Central League."""
    id: str
    name: str
    short_name: str
    color: str
    league: str = "central"


@dataclass
class StandingsData:
    """Represents standings data for a team on a specific date."""
    date: str  # ISO 8601 format (YYYY-MM-DD)
    team_id: str
    rank: int
    wins: int
    losses: int
    draws: int
    win_rate: float
    games_behind: float


# Predefined Central League teams
TEAMS = [
    Team(
        id="giants",
        name="読売ジャイアンツ",
        short_name="巨人",
        color="#FF6600",
        league="central"
    ),
    Team(
        id="tigers",
        name="阪神タイガース",
        short_name="阪神",
        color="#FFE600",
        league="central"
    ),
    Team(
        id="dragons",
        name="中日ドラゴンズ",
        short_name="中日",
        color="#0057B8",
        league="central"
    ),
    Team(
        id="carp",
        name="広島東洋カープ",
        short_name="広島",
        color="#FF0000",
        league="central"
    ),
    Team(
        id="baystars",
        name="横浜DeNAベイスターズ",
        short_name="DeNA",
        color="#6A4C9C",
        league="central"
    ),
    Team(
        id="swallows",
        name="東京ヤクルトスワローズ",
        short_name="ヤクルト",
        color="#00A650",
        league="central"
    ),
]