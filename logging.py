import logging

# Set up basic config (can be extended later)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("service.log"),
        logging.StreamHandler()
    ]
)

def log_retry(attempt, error):
    """
    Logs retry attempts in a consistent format.

    Parameters:
        attempt (int): The current retry attempt number.
        error (Exception): The exception raised during the attempt.
    """
    logging.warning(f"[Retry {attempt}] API call failed: {error}")
