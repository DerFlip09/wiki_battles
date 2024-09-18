from article import prep_article_data


LP = 5
COMMAND_DISPATCHER = {1: "Count of words",
                      2: "Count of images",
                      3: "Count of hyperlinks",
                      4: "Length of longest word",
                      5: "Highest number on page",
                      6: "Lowest number on page"}


def initialize_player(player_n):
    player = {"name": input(f"Enter name for {player_n}: ").strip(),
              "LP": LP,
              "article": prep_article_data()[0],
              "stats": prep_article_data()[1],
              "guesses": COMMAND_DISPATCHER.copy()}
    return player



