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
    players = ("A", "B")
    scores = {}
    for player in players:
        print(f"Spēlētājs {player} met kauliņu:")
        roll_list = random.choices(range(1, 7), k=rolls_to_make)
        player_score = sum(roll_list)
        scores[player] = player_score
        for count, item in enumerate(roll_list, start=1):
            print(f"{count}. metiens: {item}")
        print(f"Kopā punkti spēlētājam {player}: {player_score}\n")
    if scores[players[0]] == scores[players[1]]:
        print(f"Abiem spēlētājiem ir vienāds rezultāts, mēģiniet vēlreiz!")
    elif scores[players[0]] > scores[players[1]]:
        print(f"Uzvar spēlētājs {players[0]}")
    else:
        print(f"Uzvar spēlētājs {players[1]}")

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
