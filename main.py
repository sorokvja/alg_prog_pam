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

def do_action(do_param, sp):
    #print(f"do_param: {do_param}, sp: {sp}")
    if do_param["speed"] <= sp:
        print(0)
    else:
        if (sp - do_param["speed"]) <= 20:
            print(1)
        else:
            print(2)

def main():
    parameters = get_variables()
    if parameters["location"]:
        speed = 50
    else:
        speed = 90
    if parameters["birthday"]:
        speed += 5
    do_action(parameters, speed)

main()
