"""
api.py

Handles all API requests to Alpha Vantage.
Sets up request caching to avoid rate limits.
"""

import requests
import requests_cache

# Set up a cache for all requests. Calls to the same URL will be cached for 1 hour.
requests_cache.install_cache('alpha_vantage_cache', backend='sqlite', expire_after=3600)

# Define the base URL for the Alpha Vantage API
ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query"

def fetch_alpha_vantage_data(function: str, symbol: str, api_key: str) -> dict:
    """
    Fetches data from the Alpha Vantage API for a specific function and symbol.
    Includes error checking for common API-level messages.
    """
    # Prepare the query parameters
    params = {"function": function, "symbol": symbol, "apikey": api_key}
    
    # Send an HTTP GET request to the API URL with the specified parameters
    response = requests.get(ALPHA_VANTAGE_API_URL, params=params)
    
    # Check if the request was successful (e.g., 404, 500)
    response.raise_for_status()
    
    # Parse the JSON response text into a Python dictionary
    json_data = response.json()
    
    # Check for API-level errors in the JSON response
    if "Error Message" in json_data:
        raise Exception(f"API Error for {function} {symbol}: {json_data['Error Message']}")
    if "Information" in json_data:
        raise Exception(f"API Info for {function} {symbol}: {json_data['Information']} (This often means you've hit a rate limit)")
    if not json_data: # Handle empty JSON response {}
        raise Exception(f"API Error for {function} {symbol}: Received empty response.")

    # Return the dictionary
    return json_data