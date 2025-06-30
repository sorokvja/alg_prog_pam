def get_list(filepath):
    with open(filepath, 'r') as file:
        file_contents = eval(file.read())
    return file_contents

def sort_name_down(data_list):
    #print("\npēc preču nosaukumiem dilstošā secībā:")
    return sorted(data_list, key=lambda prece: prece[0], reverse=True)

def sort_name_up(data_list):
    #print(f"\npēc preču nosaukumiem augošā secībā:")
    return sorted(data_list, key=lambda prece: prece[0])

def sort_price_down(data_list):
    #print(f"\npēc preču cenām:")
    return sorted(data_list, key=lambda prece: prece[1], reverse=True)

def print_list(title, data_list):
    print(f"\n{title}")
    for item in data_list:
        print(f"{item[0]:<15} {item[1]:>6.2f} EUR")

def calcualte_total(data_list):
    total_price = 0
    for prece in data_list:
        total_price += prece[1]
    return round(total_price, 2)

def main():
    uzdevums_list = get_list('./7_4_list.txt')
    print_list("Oriģinālais saraksts:", uzdevums_list)
    print_list("Pēc preču nosaukumiem, dilstošā secībā:", sort_name_down(uzdevums_list))
    print_list("Pēc preču nosaukumiem, augošā secībā:", sort_name_up(uzdevums_list))
    print_list("Pēc preču cenām:", sort_price_down(uzdevums_list))
    print(f"\nVisu sarakstā esošo preču summu: {calcualte_total(uzdevums_list)} EUR")

main()
