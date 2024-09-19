from printings import print_stat_list
from time import sleep


def attack_phase(attacking_player):
    print_stat_list(attacking_player)
    stat = int(input(f"{attacking_player["name"]} choose your stat (1-6): ").strip())
    attacker_guess = int(input("Enter your guess: ").strip())
    return stat, attacker_guess


def defense_phase(attacking_player, defense_player, stat, attacker_guess):
    print(f"{attacking_player["name"]} attacks you with {attacker_guess} "
          f"for the stat {attacking_player["guesses"][stat]}")
    defender_guess = int(input(f"{defense_player["name"]} enter your guess to defend: ").strip())
    return defender_guess


def battle_phase(attacking_player, defense_player):
    stat, attacker_guess = attack_phase(attacking_player)
    defender_guess = defense_phase(attacking_player, defense_player, stat, attacker_guess)
    return stat, attacker_guess, defender_guess


def conduct_battle_round(attacker, defender):
    """Handle a single round of battle between attacker and defender."""
    stat, attacker_guess, defender_guess = battle_phase(attacker, defender)
    if compare_phase(stat, attacker_guess, defender_guess, defender, attacker):
        defender["LP"] -= 1
        print(f"{attacker["name"]} successfully attacks you {defender["name"]}!\n"
              f"You will lose 1 LP! Current LP: {defender["LP"]}")
    else:
        attacker["LP"] -= 1
        print(f"{defender["name"]} has successfully defended you {attacker["name"]}!\n"
              f"You will lose 1 LP! Current LP: {attacker["LP"]}")
    del attacker["guesses"][stat]
    sleep(1)


def compare_phase(stat, attacker_guess, defender_guess, defending_player, attacking_player):
    actual_stat = defending_player["stats"][attacking_player["guesses"][stat]]
    attacker_diff = abs(actual_stat - attacker_guess)
    defender_diff = abs(actual_stat - defender_guess)
    return attacker_diff < defender_diff


def is_battle_ongoing(player_1, player_2):
    """Check if the battle is still ongoing based on life points and available stats."""
    return player_1["LP"] > 0 and player_2["LP"] > 0 and len(player_1["guesses"]) > 0 and len(player_2["guesses"]) > 0

