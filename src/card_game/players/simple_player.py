from players.base_player import IPlayer


class SimplePlayer(IPlayer):
    cards = []

    def make_move(self):
        self.cards.sort(key=lambda c: c.value, reverse=True)

        return [self.cards.pop()]

    def respond(self, cards):
        response = [None] * len(cards)

        for i in range(0, len(cards)):
            card_to_beat = cards[i]

            options = list(
                filter(lambda c: c.suit == card_to_beat.suit and c.value > card_to_beat.value and not (c in response),
                       self.cards))
            if len(options) == 0:
                return []

            pos = self.cards.index(options[0])
            response[i] = self.cards.pop(pos)

        return response
