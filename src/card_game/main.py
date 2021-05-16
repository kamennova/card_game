from game import CardGame
from log import set_logging
from players.simple_player import SimplePlayer


def print_stats(stats):
    total_moves = 0
    loser0 = 0
    loser1 = 0

    for stat in stats:
        total_moves += stat["move_num"]
        if stat["loser"] == 1:
            loser1 += 1
        elif stat["loser"] == 0:
            loser0 += 1

    avg_moves = round(total_moves / len(stats))
    player1_defeat = loser1 * 100 / (loser0 + loser1) if loser0 + loser1 > 0 else 0
    player2_defeat = loser0 * 100 / (loser0 + loser1) if loser0 + loser1 > 0 else 0

    print("Average moves:", avg_moves,
          ", Player1 lost", player1_defeat,
          "%, Player 0 lost", player2_defeat, "%")


def run_rounds(game):
    set_logging(False)
    stats = []
    for i in range(0, 1000):
        stats.append(game.round())
    print_stats(stats)


def debug_round(game):
    set_logging(True)
    stats = []
    for i in range(0, 1):
        stats.append(game.round())
    print_stats(stats)
    set_logging(False)


player1 = SimplePlayer("Player 1")
player2 = SimplePlayer("Player2")
g = CardGame([player1, player2])
# run_rounds(g)
debug_round(g)
