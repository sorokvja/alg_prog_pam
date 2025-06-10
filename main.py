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

def do_action(do_param, sp_a, sp_na):
    print(do_param)
    if do_param["birthday"]:
        sp_a += 5
        sp_na += 5
    print(sp_a, sp_na)

def main():
    parameters = get_variables()
    speed_apdz, speed_neapdz = 50, 90
    do_action(parameters, speed_apdz, speed_neapdz)

main()
