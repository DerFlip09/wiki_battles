from printings import *
from player import initialize_player
from battle_logic import *


def main():
    print_welcome_message()
    player_1 = initialize_player("Player 1")
    player_2 = initialize_player("Player 2")
    print_instructions(player_1, player_2)
    battle_round = 1
    while is_battle_ongoing(player_1, player_2):
        print(f"\nRound {battle_round} start!")
        conduct_battle_round(player_1, player_2)
        if is_battle_ongoing(player_1, player_2):
            conduct_battle_round(player_2, player_1)
        battle_round += 1
    print_winner(battle_round, player_1, player_2)
    print_good_bye(player_1, player_2)


if __name__ == "__main__":
    main()
