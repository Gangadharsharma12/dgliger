import sys
resources = {"milk": 200, "water": 500, "coffee_beans": 100, "profit": 0}
menu = {
        "latte": {
          "ingredients": {
              "water": 200,
              "milk": 150,
              "coffee_beans": 24
          }, "cost": 150},
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee_beans": 24,
            }, "cost": 200},

        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee_beans": 18
            }, "cost": 100
        }
        }
def report():
    print(f"water : {resources['water']} ml")
    print(f"milk : {resources['milk']} ml")
    print(f"coffee_beans : {resources['coffee_beans']}g")
    print(f"profit : {resources['profit']} RS")

def add_resource():
    add_milk = int(input("how much milk you want to add:"))
    add_water = int(input("how much water you want to add:"))
    add_coffee_beans= int(input("how much coffee_beams you want to add:"))
    resources["milk"] += add_milk
    resources["water"] += add_water
    resources["coffee_beans"] += add_coffee_beans
def check_resources(order_int):
    for item in order_int:
        if order_int[item] > resources[item]:
            print(f"sorry!! not enough {item}")
            return False
    return True

def process_coins():
    total = 0
    print("please insert coins")
    five_coins = int(input("how many 5 RS coins?"))
    ten_coins = int(input("how many 10 RS coins?"))
    twenty_coins = int(input("how many 20 RS coins?"))
    total += five_coins*5 + ten_coins*10 + twenty_coins*20
    return  total

def is_payment_successful(money_received, cost_of_coffee):
    if money_received >= cost_of_coffee:
        resources['profit'] += cost_of_coffee
        change = money_received - cost_of_coffee
        print(f"please collect your change of RS {change}")
        return True
    else:
        print(f"sorry!!. The cost of coffee is {coffee_type['cost']} and you have provided only {money_received}")
        print("please collect your cash and try again. Thank you")
        return False
def make_coffee(coffee_name, ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]



def quit():
    print("Thank you for using our services")
    sys.exit()

if __name__ == "__main__":
    while True:
        choice = input("what would you like to have? (latte/espresso/cappuccino): ").lower()
        if choice == 'report':
            report()

        elif choice == "off":
            quit()
        else:
            coffee_type = menu[choice]
            print(coffee_type)
            if check_resources(coffee_type["ingredients"]):
                profit = process_coins()
                if is_payment_successful(profit, coffee_type["cost"]):
                    make_coffee(choice, coffee_type["ingredients"])
            else:
                option = input("would you like to add extra resources to the meachine? [yes/no]").lower()
                if option == "no":
                    quit()
                else:
                    add_resource()


