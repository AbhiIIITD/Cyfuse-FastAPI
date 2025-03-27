import logging
import subprocess
import requests

PLAYER_NAME = "Player1"
PLAYER_API_URL = "http://127.0.0.1:8001"
DEALER_API_URL = "http://127.0.0.1:8000"

def register_with_dealer():
    data = {
        "name": PLAYER_NAME,
        "host_url": "host url"
    }
    register_endpoint = f"{DEALER_API_URL}/register"
    
    try:
        response = requests.post(register_endpoint, json=data)
        response.raise_for_status()
        logging.info("Successfully registered with dealer: %s", response.json())
    except Exception as e:
        logging.error("Error registering with dealer: %s", e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    register_with_dealer()

    logging.info("Starting Player API...")

    port = 8001
    process = subprocess.Popen([
        "uvicorn", "playapi:app",
        "--host", "127.0.0.1",
        "--port", str(port)
    ])

    process.wait()
