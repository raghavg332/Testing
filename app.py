import requests

def fetch_external_data(url, retries=3, backoff=2):
    """
    Fetches data from an external API with retry logic.
    
    Parameters:
        url (str): The API endpoint to fetch data from.
        retries (int): Number of retries before giving up.
        backoff (int): Time multiplier for exponential backoff.
        
    Returns:
        dict or None: Parsed JSON data, or None if all retries fail.
    """
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"[Retry {attempt+1}] Error: {e}")
            time.sleep(backoff ** attempt)
            attempt += 1
    return None
