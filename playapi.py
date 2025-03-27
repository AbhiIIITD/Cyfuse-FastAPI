# playapi.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Model for the game state received from the dealer
class GameState(BaseModel):
    cards: List[str]  # e.g., ["2D", "AD", "10H"]
    pot: int          # e.g., 0

# Model for the action response from the player
class Action(BaseModel):
    action: str             # "bet", "fold", or "show"
    amount: Optional[int] = None  # Only used when betting

# List of suits and values for reference (if needed for more advanced logic)
suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def extract_rank(card: str) -> str:
    """
    Extracts the rank from a card string.
    Assumes cards are formatted like "10H", "AD", "2C", etc.
    """
    if card.startswith("10"):
        return "10"
    else:
        return card[0]

@app.post("/play", response_model=Action)
def play_game(state: GameState):
    """
    Decides the player's move based on the current game state.
    
    Strategy:
    - If the pot is high (>= 100), choose to show the cards.
    - Else, if any card is an Ace, bet a fixed amount (e.g., 10).
    - Otherwise, fold.
    """
    # If the pot is very high, decide to show cards.
    if state.pot >= 100:
        return Action(action="show")
    
    # Check if the player's cards include an Ace.
    has_ace = any(extract_rank(card) == "A" for card in state.cards)
    if has_ace:
        return Action(action="bet", amount=10)
    
    # In all other cases, fold.
    return Action(action="fold")
