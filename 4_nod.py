# 4.1. Uzdevuma kods
import random

def get_input():
    allowed_input = ("C", "G", "Q")
    while True:
        try:
            user_input = input("Ievadiet savu izvēli - C (cipars), G (ģerbonis) vai Q (exit) ==> ").upper()
            if user_input not in allowed_input:
                raise Exception("Kļūda: mēģieniet ievadīt burtus c, C, g, G, q, Q.")
            elif user_input == "Q":
                return None
            else:
                return user_input
        except Exception as e:
            print(e)

def random_value():
    choice_from = "CG"
    r_value = random.choice(choice_from)
    print(f"Monētas mešanas simulācija: {r_value}")
    return r_value

def compare_inputs(user, machine):
    if user == machine:
        print("Uzminēji")
        return True
    else:
        print("Nepaveicās")
        return False

def end_game_data(games, user_w):
    print("\n***********")
    print(f"Spēles: {games}")
    print(f"Lietotājs vinnēja: {user_w}")
    print(f"Dators vinnēja: {games - user_w}")

def main():
    games_played = 0
    user_wins = 0
    while True:
        user_input = get_input()
        if user_input == None:
            print("Lietotājs izvēlējas pabeigt spēli.")
            end_game_data(games_played, user_wins)
            break
        computer_input = random_value()
        outcome = compare_inputs(user_input, computer_input)
        games_played += 1
        if outcome:
            user_wins += 1

main()

# 4.2. Uzdevuma kods
