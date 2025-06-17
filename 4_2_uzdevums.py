# 4.2. Uzdevuma kods
import random

def get_input():
    allowed_input = ("1", "2", "Q")
    print("Divu spēlētāju spēle (1)\n100. punktu spēle (2)\nIziet (Q)")
    while True:
        user_input = input("Ievadiet savu izvēli ==> ").upper()
        if user_input in allowed_input:
            return user_input
        print("\nKļūda: mēģieniet ievadīt 1, 2, Q vai q.")
'''
def dice_roll(dice_min_val, dice_max_val, rolls):
    rolls_performed = {}

    return random.randint(min_val, max_val)
'''
def two_player_game():
    rolls_to_make = 6
    players_scores = {"A": 0, "B": 0}
    winner = []
    for player in players_scores:
        print(f"Spēlētājs {player} met kauliņu:")
        roll_list = random.choices(range(1, 7), k=rolls_to_make)
        for count, item in enumerate(roll_list, start=1):
            print(f"{count}. metiens: {item}")
        players_scores[player] = sum(roll_list)
        print(f"Kopā punkti spēlētājam {player}: {players_scores[player]}\n")
    max_score = max(players_scores.values())
    for player, score in players_scores.items():
        if score == max_score:
            winner.append(player)
    if len(winner) > 1:
        print("Vairākiem spēlētājiem ir vienāds rezultāts, mēģiniet vēlreiz!")
    else:
        print(f"Uzvar spēlētājs {winner[0]}")

def hundred_points_game():
    pass

def main():
    user_input = get_input()
    if user_input == "Q":
        print("Lietotājs izvēlējas pabeigt spēli.\n")
    elif user_input == "1":
        two_player_game()
    else:
        hundred_points_game()

main()
