"""
Web scraper for NPB (Nippon Professional Baseball) standings data.
"""
import requests
from typing import Optional
from datetime import datetime


def fetch_npb_standings(year: Optional[int] = None) -> str:
    """
    Fetch NPB Central League standings HTML from the official website.
    
    Args:
        year: Year to fetch data for. If None, fetches current season.
        
    Returns:
        HTML content as string
        
    Raises:
        requests.RequestException: If the request fails
    """
    if year is None:
        year = datetime.now().year
    
    # NPB official standings page URL
    # Note: This is a placeholder URL - actual NPB website structure may vary
    url = f"https://npb.jp/bis/{year}/standing_c.html"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to fetch standings data: {str(e)}")