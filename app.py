import requests

def fetch_external_data(url):
    """
    Fetches data from an external API.

    Parameters:
        url (str): The API endpoint to fetch data from.

    Returns:
        dict or None: Parsed JSON data, or None if the request fails.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API call failed: {e}")
        return None
