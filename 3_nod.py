# 3.1. Uzdevuma kods
def get_variables():
    int_a = int(input('Ievadiet veselo skaitli "a" ==> '))
    int_b = int(input('Ievadiet veselo skaitli "b" ==> '))
    int_c = int(input('Ievadiet veselo skaitli "c" ==> '))
    #print(f"Skaitlis a = {int_a}, skaitlis b = {int_b}, skaitlis c = {int_c}")
    return int_a, int_b, int_c

def do_action(a, b, c):
    if a == b and a == c:
        print(3)
    elif a == b or a == c or b == c:
        print(2)
    else:
        print(1)

def main():
    a, b, c = get_variables()
    do_action(a, b, c)

main()

# 3.2. Uzdevuma kods
def get_variables():
    while True:
        try:
            atz_int = int(input('Ievadiet atzīmi, veselo skaitli no 1. līdz 100. ==> '))
            if atz_int < 1 or atz_int > 100:
                print("Kļūda #1: lūdzu ievadiet skaitli no 1. līdz 100.!")
                continue
            return atz_int
        except ValueError:
            print("Kļūda #2: ievadīta vērtība neesot vesels skaitlis!")

def do_action(a):
    if a >= 90:
        print("A")
    elif 80 <= a < 90:
        print("B")
    elif 70 <= a < 80:
        print("C")
    elif 60 <= a < 70:
        print("D")
    elif 50 <= a < 60:
        print("E")
    else:
        print("F")

def main():
    a = get_variables()
    do_action(a)

main()

# 3.3. Uzdevuma kods
def get_variables():
    n = str(input('Ievadiet lietotāja vārdu ==> '))
    p = str(input('Ievadiet paroli ==> '))
    return n, p

def do_action(n, p, users_dict):
    for key in users_dict:
        if key == n:
            if users_dict[key] == p:
                print("Laipni lūdzam, Jūs varat turpināt darbu ar programmu!")
            else:
                print("Parole ir nepareiza!")
        else:
            print("Šāds lietotājs neeksistē!")

def main():
    registered_users = {"admin": "12345", }
    usr_name, usr_passw = get_variables()
    do_action(usr_name, usr_passw, registered_users)

main()

# 3.4. Uzdevuma kods
def get_boolean_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ("y", "yes"):
            return True
        elif user_input in ("n", "no"):
            return False
        else:
            print("Kļūda: var ievadīt y, yes, n, no.")

def get_variables():
    get_param = {}
    while True:
        try:
            get_param["speed"] = int(input('Ievadiet braukšanas ātrumu ==> '))
            if get_param["speed"] < 0:
                print("Kļūda: ātrums nevar būt negatīvs skaitlis!")
                continue
            else:
                get_param["location"] = get_boolean_input("Vai ceļš atrodas apdzīvotā vietā? (Y/N) ==> ")
                get_param["birthday"] = get_boolean_input("Vai  autovadītāja dzimšanas diena? (Y/N) ==> ")
                return get_param
        except ValueError:
            print("Kļūda: ievadiet ātrumu izmantojot ciparus!")

def do_action(speed, sp_limit):
    #print(f"speed: {speed}, sp_limit: {sp_limit}")
    if speed <= sp_limit:
        print(0)
    else:
        if (speed - sp_limit) <= 20:
            print(1)
        else:
            print(2)

def main():
    parameters = get_variables()
    if parameters["location"]:
        speed_limit = 50
    else:
        speed_limit = 90
    if parameters["birthday"]:
        speed_limit += 5
    do_action(parameters["speed"], speed_limit)

main()

