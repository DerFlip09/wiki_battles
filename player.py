from article import *


LP = 5


def initialize_player(player_n):
    player = {"name": input(f"Enter name for {player_n}: ").strip(),
              "LP": LP,
              "article": prep_article_data()[0],
              "stats": prep_article_data()[1],
              "guesses": COMMAND_DISPATCHER.copy()}
    return player



