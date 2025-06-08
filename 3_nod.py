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

