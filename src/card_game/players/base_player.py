from typing import List
import sys
sys.path.append("..")
from cards import Card, display_cards


class IPlayer:
    cards: List[Card] = []

    def __init__(self, name="Player 1"):
        self.name = name

    # @property
    # def speed(self):
    #     raise NotImplementedError

    def make_move(self) -> List[Card]:
        raise NotImplementedError

    def respond(self, cards: List[Card]) -> List[Card]:
        raise NotImplementedError

    def get_cards(self):
        return self.cards

    def take_cards(self, cards):
        self.cards.extend(cards)

    def clear(self):
        self.cards = []

