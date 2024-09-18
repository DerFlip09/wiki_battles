def print_welcome_message():
    print(39*"#" + "\n" + 5*"#"+ " Welcome to the Wiki Battles " + 5*"#" + "\n" + 39*"#")


def print_instructions(player_1, player_2):
    print(f"\n{13 * "#"} INSTRUCTIONS {13 * "#"}\n"
          f"\nHello {player_1["name"]} and {player_2["name"]}!\n"
          f"Before we start the Battle a quick overview how to play:\n"
          f"This Game is played with 2 Player.\n"
          f"Each Player gets a random article from Wikipedia.\n"
          f"One Round is defined with an attack and a defense from each Player.\n"
          f"The attacker chooses one stat out of a list and guessed it for the article of the defender.\n"
          f"The Defender will than counter guess to defend himself.\n"
          f"The guess which is nearer to the actual stat wins.\n"
          f"The loser will lose 1 LP.\n"
          f"After that the roles of attacker and defender will switch.\n"
          f"This repeats until someone hits 0 LP or every stat is guessed.\n"
          f"Special Win Condition:\n"
          f"if you can guess the article of the other player, you win instantly\n"
          f"And with all that said, have a good fight and happy guessing!\n")
    input("Please press Enter to continue")


def print_stat_list(player):
    print("\nStats to choose: ")
    for command_number, command_info in player["guesses"].items():
        print(f"{command_number}. {command_info}")


def print_winner(battle_rounds, player_1, player_2):
    print(f"{39 * "#"}\nAfter {battle_rounds} rounds, the winner is decided!")
    if player_1["LP"] > player_2["LP"]:
        print(f"{player_1["name"]}! Congrats to win the Wiki Battle!")
    else:
        print(f"{player_2["name"]}! Congrats to win the Wiki Battle!")


def print_good_bye(player_1, player_2):
    print(f"{player_1["name"]} and {player_2["name"]} thanks for playing this little game!\n"
          f"We hope you had fun!\n"
          f"We would love to hear your feedback and also suggestions for improvement!\n"
          f"See you in the next battle!")