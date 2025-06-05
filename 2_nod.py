# 2.1. Uzdevuma kods
def get_variables():
    int_a = int(input('Ievadiet veselo skaitli "a" ==> '))
    int_b = int(input('Ievadiet veselo skaitli "b" ==> '))
    print(f"Skaitlis a = {int_a}, skaitlis b = {int_b}")
    return int_a, int_b

def do_action(a, b):
    # actions to print: +, -, *, /, //, %, **
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    try:
        print(f"a / b = {a / b}")
        print(f"a // b = {a // b}")
        print(f"a % b = {a % b}")
        print(f"a ** b = {a ** b}")
    except ZeroDivisionError as e:
        print(f"Kļūda: {e}")

def main():
    print("Hello!")
    a, b = get_variables()
    do_action(a, b)

main()

# 2.2 Uzdevuma kods
def get_variables():
    int_x = int(input('Ievadiet veselo skaitli "x" ==> '))
    int_y = int(input('Ievadiet veselo skaitli "y" ==> '))
    #print(f"x = {int_x}, y = {int_y}")
    return int_x, int_y

def do_action_1(x, y):
    try:
        print(f"1) rezultāts = {(2 + x)/(x * y)}")
    except ZeroDivisionError as e:
        print(f"1) Kļūda: {e}")

def do_action_2(x, y):
    print(f"2) rezultāts = {5 * (x ** 3) - (x ** 2) + (7 * x) - 6}")

def do_action_3(x, y):
    print(f"3) rezultāts = {(x * y) ** 0.5}")

def do_action_4(x, y):
    try:
        print(f"4) rezultāts = {(2 ** (x * y)) / (5 * y)}")
    except ZeroDivisionError as e:
        print(f"4) Kļūda: {e}")

def main():
    x, y = get_variables()
    do_action_1(x, y)
    do_action_2(x, y)
    do_action_3(x, y)
    do_action_4(x, y)

main()

#2.3 Uzdevuma kods
def main():
    price_book = 24.95
    discount = 0.4
    price_basic_delivery = 3
    price_extra_delivery = 0.75

    units_bought = 60
    costs_books = price_book * units_bought
    costs_books_discounted = costs_books * (1 - discount)

    costs_delivery = price_basic_delivery + price_extra_delivery * (units_bought - 1)

    costs_total = costs_books_discounted + costs_delivery
    print(f"Kopējas izmaksas: {costs_total: .2f} EUR")

main()

#2.4 Uzdevuma kods
def get_variables():
    int_eur = int(input('Eiro ==> '))
    int_cent = int(input('Centi ==> '))
    int_cookies = int(input('Kūku skaits ==> '))
    return int_eur, int_cent, int_cookies

def do_action(a, b, n):
    eur = a * n
    cents = b * n
    eur += cents // 100
    cents %= 100
    print(f"Par {n} kūkam ir jāmaksā {eur} Eiro un {cents} centi")

def main():
    print("Ievadiet vienas kūkas cenu un kūku skaitu:")
    a, b, n = get_variables()
    do_action(a, b, n)

main()

#2.5 Uzdevuma kods
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

#2.6 Uzdevuma kods
def get_variables():
    # https://lv.wikipedia.org/wiki/Re%C4%81ls_skaitlis
    while True:
        try:
            n_float = float(input('Ievadiet reālo skaitli ==> '))
            return n_float
        except ValueError:
            print("Kļūda: ievadīta vērtība neesot reāls skaitlis!")

def do_action(skaitlis):
    n = skaitlis
    #n = abs(skaitlis)
    if n < 0:
        n *= -1
    a, b = int(n), n
    b -= a
    a %= 10
    b *= 10
    c = int(b)
    print(f"Cipari: {a} un {c}")

def main():
    n = get_variables()
    do_action(n)

main()

