# Create Coffee Machine Program

'''
Apa aja featurenya :
1. Print report sisa ingredients yang ada di mesin
2. Memeriksa sumberdaya yang ada saat orderan hendak dibuat
3. Saat sudah dipilih hendak yang mana, process coin yang masuk
4. Cek apakah transaksinya sukses (uangnya cukup atau enggak).
   Kalau uangnya cukup, hitung apakah ada kembaliannya dan uang
   dimasukan kedalam wallet. Jika tidak cukup, maka full refund
   dan uang yang ada di wallet tidak bertambah
5. Membuat kopi jika transaksi berhasil. Maka uang akan masuk
   walet, resources akan berkurang dan sajikan kopi
'''

from data import resources, MENU

state_coffee_machine = True
money = 0
total_change = 0


def print_report():
    '''Print the remain resource of Coffe Machine'''
    print(f"Water : {resources['water']}")
    print(f"Milk  : {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money : ${float(money)}")


def mapping_menu(order):
    '''Return mapping of ingredients and cost from choosen menu'''
    ingredients = MENU[order]['ingredients']
    cost = MENU[order]['cost']
    return ingredients, cost

def check_resource(ingredients):
    '''Checking are the ingredients items still less than remain resource or not'''
    for key,value in resources.items():
        for key1,value1, in ingredients.items():
            if key == key1:
                if value < value1:
                    return key


while state_coffee_machine:
    pointer = input('What you like ? (espresso/latte/cappuccino): ').lower()
    if pointer == 'off':
        state_coffee_machine = False

    # TODO: Print the report of current resources
    elif pointer == 'report':
        print_report()

    elif pointer == 'espresso' or pointer == 'latte' or pointer == 'cappuccino':
        ingredients, cost = mapping_menu(pointer)

        cek_sisa_resource = check_resource(ingredients)
        if cek_sisa_resource:
            print(f"Sorry there is not enough {cek_sisa_resource}")
            continue

        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        total_receives = (0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
        total_change = total_receives-cost
        if total_change < 0:
            print("Sorry that's not enough money. Money refunded")
        elif total_change >= 0:
            for key, value in ingredients.items():
                # print(key, value)
                for key1, value1 in resources.items():
                    # print(key1, value1)
                    if key == key1:
                        # resources[value1] -= ingredients[value]
                        resources[key1] -= ingredients[key]
                    else:
                        continue
            money += cost
            print("Enjoy the coffee ☕")

        print(ingredients, cost, total_receives,resources)
