def get_variables():
    int_eur = int(input('Eiro ==> '))
    int_cent = int(input('Centi ==> '))
    int_cookies = int(input('Kūku skaits ==> '))
    return int_eur, int_cent, int_cookies

def do_action(a, b, n):
    eur = a * n
    cents = b * n
    #print(f"eur_a: {eur}, cents_b: {cents}")
    eur += cents // 100
    cents %= 100
    print(f"Par {n} kūkam ir jāmaksā {eur} Eiro un {cents} centi")

def main():
    print("Ievadiet vienas kūkas cenu un kūku skaitu:")
    a, b, n = get_variables()
    do_action(a, b, n)

main()
