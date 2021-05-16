from random import randint
from typing import List, Callable

from cards import toss_deck, card_str, Card
from helpers import pop_n
from log import log
from players.base_player import IPlayer

PLAYER_CARDS_NUM = 6


class CardGame:
    players: List[IPlayer] = []
    turn = 0
    deck: List[Card] = []
    toss_func: Callable[[None], List[Card]]

    def __init__(self, players, toss_func=toss_deck):
        self.players = players
        self.toss_func = toss_func

    def refill_cards(self, queue: List[int]):
        for index in queue:
            player = self.players[index]
            cards_num = PLAYER_CARDS_NUM - len(player.get_cards())

            if cards_num < 0 or len(self.deck) == 0:
                continue

            refill = pop_n(self.deck, cards_num)
            player.take_cards(refill)

    def next_turn(self):
        return 1 if self.turn == 0 else 0

    def move(self):
        mover = self.players[self.turn]
        beating = self.players[self.next_turn()]

        move_cards = mover.make_move()
        log(mover.name, " makes move: ", card_str(move_cards[0]))
        response = beating.respond(move_cards)

        if len(response) == 0:
            beating.take_cards(move_cards)
        else:
            log(beating.name, " responds with ", card_str(response[0]))

        self.refill_cards([self.turn, self.next_turn()])

        if len(response) > 0:
            self.turn = self.next_turn()

    def prepare_game(self):
        self.deck = self.toss_func()

        for player in self.players:
            # todo why?
            player.clear()

        self.refill_cards([0, 1])
        self.turn = randint(0, 1)

    def is_game_over(self) -> bool:
        return len(self.deck) == 0 and (len(self.players[0].get_cards()) == 0 or len(self.players[1].get_cards()) == 0)

    def get_loser(self):
        if len(self.players[0].get_cards()) == 0 and len(self.players[1].get_cards()) == 0:
            return None

        return 1 if len(self.players[0].get_cards()) == 0 else 0

    def round(self):
        self.prepare_game()

        move_num = 0
        while not self.is_game_over() and move_num < 15:
            self.move()
            move_num += 1

        loser = self.get_loser()
        log("Game over. Loser: ", loser)

        return {"loser": loser, "move_num": move_num}
