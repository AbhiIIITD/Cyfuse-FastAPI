# Teen Patti API Project

This project implements a simple API for a Teen Patti (3 Cards) game player using FastAPI. The project demonstrates how to build an API that makes decisions based on the game state, registers the player with a dealer's API, and tests the endpoints.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Registering with the Dealer](#registering-with-the-dealer)
- [API Endpoints](#api-endpoints)
  - [Play Endpoint](#play-endpoint)
- [Testing](#testing)
- [How It Works](#how-it-works)
- [Additional Information](#additional-information)

## Overview

The Teen Patti API project consists of two main components:

1. **Player API (`playapi.py`):**  
   A FastAPI application that processes game state data and returns a player's action (bet, fold, or show).

2. **Initialization Script (`init.py`):**  
   A script that registers the player with a dealer's API and starts the player API server.

Additionally, a test script (`test_api.py`) is provided to automatically verify the API endpoints.

## Features

- **Automatic Data Validation:**  
  Utilizes Pydantic models to validate request payloads and ensure correct data types.
  
- **Asynchronous Endpoints:**  
  FastAPI endpoints support asynchronous operations, allowing efficient, concurrent processing of I/O-bound tasks.
  
- **Game Decision Logic:**  
  Implements simple decision-making logic based on the game state (cards and pot).
  
- **Dealer Integration:**  
  The initialization script registers the player with a dealer's API by sending a JSON payload containing the player's name and API URL.
  
- **Automated Testing:**  
  A test script ensures the API behaves as expected.

## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://docs.python-requests.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create and Activate a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Unix or MacOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn requests
   ```

## Project Structure
```
├── init.py         # Script to register with the dealer and start the API server
├── playapi.py      # FastAPI application that implements the player's game logic
├── test_api.py     # Test script to verify API endpoints
└── README.md       # This file
```

## Usage

### Running the API

You can start the player API in one of two ways:

1. Directly with Uvicorn:
   ```bash
   uvicorn playapi:app --host 127.0.0.1 --port 8001
   ```

2. Via the Initialization Script:
   ```bash
   python init.py
   ```

The `init.py` script will:
- Register the player with the dealer's API.
- Launch the player API as a separate Uvicorn process on port 8001.

### Registering with the Dealer

The initialization process sends a JSON payload to the dealer's API (assumed to be running at http://127.0.0.1:8000/register). The payload contains:

- Player Name: Defined as PLAYER_NAME (e.g., "Player1").
- Player API URL: Defined as PLAYER_API_URL (e.g., "http://127.0.0.1:8001").

Example payload:
```json
{
  "name": "Player1",
  "host_url": "http://127.0.0.1:8001"
}
```

Make sure the dealer's API is running before executing `init.py`.

## API Endpoints

### Play Endpoint

**Endpoint:** `/play`
**Method:** POST

**Description:**
The `/play` endpoint receives the game state in JSON format and returns the player's decision based on simple logic. The decision is made using the following criteria:

- **Bet:** If an Ace is present in the player's cards and the pot is low.
- **Fold:** If no Ace is present and the pot is low.
- **Show:** If the pot is high (e.g., pot >= 100).

**Request Payload Example:**
```json
{
  "cards": ["2D", "AD", "10H"],
  "pot": 50
}
```

**Response Payloads:**

- Bet:
  ```json
  { "action": "bet", "amount": 10 }
  ```
- Fold:
  ```json
  { "action": "fold" }
  ```
- Show:
  ```json
  { "action": "show" }
  ```

## Testing

A test script (`test_api.py`) is provided to verify the API functionality. The script uses Python's requests library to send requests to the `/play` endpoint and asserts that the responses are as expected.

**How to Run Tests:**

1. Ensure the player API is running (using either uvicorn or `init.py`).
2. Run the test script:
   ```bash
   python test_api.py
   ```

The test script includes:
- Test for Betting: Verifies that the API returns a bet action with an amount when an Ace is present.
- Test for Folding: Verifies that the API returns a fold action when no Ace is present.
- Test for Showing: Verifies that the API returns a show action when the pot is high.

If all tests pass, a confirmation message will be displayed.

## How It Works

**FastAPI & Pydantic:**
FastAPI utilizes Pydantic models to validate incoming JSON payloads, ensuring the data structure meets the expected format before processing.

**Game Logic:**
The decision-making in the `/play` endpoint is based on:
- The cards the player holds.
- The current pot value. The logic is simple and serves as a starting point, allowing further customization for more complex strategies.

**Dealer Integration:**
The `init.py` script registers the player with the dealer's API by sending the player's name and API URL as JSON data, ensuring that the dealer can communicate with the player during the game.

**Asynchronous Operation:**
FastAPI's asynchronous support enables the API to handle multiple requests concurrently, which is particularly useful during I/O-bound operations.

**Automated Testing:**
The provided test script verifies that the API endpoints behave as expected, helping to catch issues early during development.

## Additional Information

**Logging:**
Logging is incorporated in the `init.py` script to track the registration process and monitor the startup of the API server.

**Extensibility:**
The game logic in `playapi.py` is intentionally basic. Developers can extend or modify it to incorporate more advanced decision-making strategies based on additional game state parameters.

**Further Reading:**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

Happy coding and enjoy building your Teen Patti API!
