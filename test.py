import requests

PLAYER_API_URL = "http://127.0.0.1:8001/play"

def test_play_bet():
    """
    Test case where the player should bet because one card is an Ace.
    Expected response: {"action": "bet", "amount": 10}
    """
    payload = {
        "cards": ["2D", "AD", "10H"],  # Contains an Ace ("AD")
        "pot": 50
    }
    response = requests.post(PLAYER_API_URL, json=payload)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    data = response.json()
    assert data.get("action") == "bet", f"Expected action 'bet' but got {data.get('action')}"
    assert data.get("amount") == 10, f"Expected amount 10 but got {data.get('amount')}"
    print("Test play_bet passed.")

def test_play_fold():
    """
    Test case where the player should fold because there's no Ace and the pot is low.
    Expected response: {"action": "fold"}
    """
    payload = {
        "cards": ["2D", "3H", "10C"],  # No Ace present
        "pot": 50
    }
    response = requests.post(PLAYER_API_URL, json=payload)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    data = response.json()
    assert data.get("action") == "fold", f"Expected action 'fold' but got {data.get('action')}"
    print("Test play_fold passed.")

def test_play_show():
    """
    Test case where the pot is high so the player should show.
    Expected response: {"action": "show"}
    """
    payload = {
        "cards": ["2D", "3H", "10C"],  # Cards do not matter if pot is high
        "pot": 150  # High pot triggers show action
    }
    response = requests.post(PLAYER_API_URL, json=payload)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    data = response.json()
    assert data.get("action") == "show", f"Expected action 'show' but got {data.get('action')}"
    print("Test play_show passed.")

def run_tests():
    test_play_bet()
    test_play_fold()
    test_play_show()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
