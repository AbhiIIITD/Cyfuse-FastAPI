# Teen Patti API Project

This project implements a simple API for a Teen Patti (3 Cards) game player using FastAPI. The project demonstrates how to build an API that makes decisions based on the game state, register the player with a dealer's API, and test the endpoints.

---

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

---

## Overview

The Teen Patti API project consists of two main components:
1. **Player API (`playapi.py`):** A FastAPI application that processes game state data and returns a player's action (bet, fold, or show).
2. **Initialization Script (`init.py`):** A script that registers the player with a dealer's API and starts the player API server.

Additionally, a test script (`test_api.py`) is provided to automatically verify the API endpoints.

---

## Features

- **Automatic Data Validation:**  
  Utilizes Pydantic models to validate request payloads and ensure correct data types.
  
- **Asynchronous Endpoints:**  
  FastAPI endpoints support asynchronous operations, allowing for efficient, concurrent processing of I/O-bound operations.
  
- **Game Decision Logic:**  
  Implements simple logic to decide whether to bet, fold, or show cards based on the game state (e.g., the player's cards and the current pot).
  
- **Dealer Integration:**  
  The initialization script registers the player's API with the dealer's API by sending a JSON payload.
  
- **Automated Testing:**  
  A test script ensures the API behaves as expected.

---

## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://docs.python-requests.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AbhiIIITD/Cyfuse-FastAPI
   cd Cyfuse-FastAPI
