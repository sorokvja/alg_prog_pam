def get_variables():
    while True:
        try:
            nat_int = int(input('Ievadiet naturālo skaitli ==> '))
            if nat_int < 0:
                print("Kļūda #1: ievadītais skaitlis neesot naturāls skaitlis!")
                continue
            return nat_int
        except ValueError:
            print("Kļūda #2: ievadīta vērtība neesot naturāls skaitlis!")

def do_action_1(a):
    return a % 10

def do_action_2(a):
    while a >= 10:
        a -= 10
    return a

def main():
    a = get_variables()
    b_1 = do_action_1(a)
    print(f"1. metode: skaitļa {a} pedējais cipars ir {b_1}")
    b_2 = do_action_2(a)
    print(f"2. metode: skaitļa {a} pedējais cipars ir {b_2}")

main()
