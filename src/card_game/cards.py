from enum import Enum, IntEnum
from random import randint
from typing import TypeVar, Generic, List

from log import log

CardSuitType = TypeVar('CardSuitType')
CardValueType = TypeVar('CardValueType')


class Card(Generic[CardSuitType, CardValueType]):
    def __init__(self, suit: CardSuitType, value: CardValueType):
        self.suit = suit
        self.value = value


class CardSuit(Enum):
    Blue = "B"
    Orange = "O"
    Green = "G"
    Red = "R"


class CardValue(IntEnum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Ten = 10


def toss_deck() -> List[Card]:
    deck = []

    for suit in CardSuit:
        for value in CardValue:
            deck.append(Card(suit, value))

    tossed_deck = []
    num = len(deck)
    for card in range(0, num):
        pos = randint(0, len(deck) - 1)
        tossed_deck.append(deck.pop(pos))

    return tossed_deck


def card_str(card):
    return str(card.suit.value) + " " + str(card.value.value)


def display_cards(cards):
    log(", ".join(map(card_str, cards)))
