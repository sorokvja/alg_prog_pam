# 7.1. Uzdevuma kods
def get_input():
    entered_text = input('Ievadiet tekstu ==> ')
    return entered_text

def do_action(the_text):
    reversed_text = the_text[::-1]
    if the_text[0].isupper():
        reversed_text = reversed_text.capitalize()
    print(f"Apgriezts teksts (ja vārds sākas ar lielo burtu, arī apgrieztais vārds sākas ar lielo burtu): {reversed_text}")

def do_action_alt(the_text):
    ol_reversed_text = the_text[::-1] # original letters
    #print(f"ol_reversed_text: {ol_reversed_text}")
    reversed_text = ""
    for i in range (len(the_text)):
        if the_text[i].isupper():
            reversed_text += ol_reversed_text[i].upper()
        else:
            reversed_text += ol_reversed_text[i].lower()
    print(f"Apgriezts teksts (alternatīvs risinājums): {reversed_text}")

def main():
    teksts = get_input()
    do_action(teksts)
    do_action_alt(teksts)

main()

# 7.2. Uzdevuma kods
