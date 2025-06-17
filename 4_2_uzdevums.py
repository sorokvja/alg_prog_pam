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

def two_player_game():
    rolls_to_make = 6
    players_scores = {"A": 0, "B": 0}
    for player in players_scores:
        print(f"Spēlētājs {player} met kauliņu:")
        roll_list = random.choices(range(1, 7), k=rolls_to_make)
        for count, item in enumerate(roll_list, start=1):
            print(f"{count}. metiens: {item}")
        players_scores[player] = sum(roll_list)
        print(f"Kopā punkti spēlētājam {player}: {players_scores[player]}\n")
    return players_scores

def hundred_points_game():
    print("Spēles mērķis: pirmajam sasniegt vismaz 100 punktus.\n")
    players_scores = {"User": 0, "PC": 0}
    winner = []
    while players_scores["User"] < 100 and players_scores["PC"] < 100:
        user_rolls = random.choices(range(1, 7), k=2)
        players_scores["User"] += sum(user_rolls)
        print(f'Lietotājs | {user_rolls[0]}  {user_rolls[1]} | {players_scores["User"]}')
        pc_rolls = random.choices(range(1, 7), k=2)
        players_scores["PC"] += sum(pc_rolls)
        print(f'Dators    | {pc_rolls[0]}  {pc_rolls[1]} | {players_scores["PC"]}\n')
    print("Spēle beigusies!")
    return players_scores
    max_score = max(players_scores.values())
    for player, score in players_scores.items():
        if score == max_score:
            winner.append(player)
    if len(winner) > 1:
        print("Vairākiem spēlētājiem ir vienāds rezultāts, mēģiniet vēlreiz!")
    else:
        print(f'{winner[0]} uzvarēja!\nIegūtie punkti:')
        print(f'')

def the_winner(players_scores):
    winner = []
    max_score = max(players_scores.values())
    for player, score in players_scores.items():
        if score == max_score:
            winner.append(player)
    if len(winner) > 1:
        print("Vairākiem spēlētājiem ir vienāds rezultāts, mēģiniet vēlreiz!")
    else:
        print(f'{winner[0]} uzvarēja!\nIegūtie punkti:')
        i = 0
        for player, score in players_scores.items():
            print(f'{player}: {score}')

def main():
    user_input = get_input()
    if user_input == "Q":
        print("Lietotājs izvēlējas pabeigt spēli.\n")
    elif user_input == "1":
        players_and_scores = two_player_game()
        the_winner(players_and_scores)
    else:
        players_and_scores = hundred_points_game()
        the_winner(players_and_scores)

main()
