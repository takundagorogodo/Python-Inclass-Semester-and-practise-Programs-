profit = 0

Menu = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 150
    },
    "espresso": {
        "ingredients": {
            "water": 200,
            "coffee": 18
        },
        "cost": 100
    },
    "cappuccino": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 18
        },
        "cost": 200
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins:")
    total = 0
    coins_five = int(input("How many 5rs coins?: "))
    coins_ten = int(input("How many 10rs coins?: "))
    coins_twenty = int(input("How many 20rs coins?: "))
    total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20
    return total


def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your Rs{change} in change.")
        return True
    else:
        print("There is not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name}. Enjoy your drink!")


is_on = True

while is_on:
    choice = input("What would you like? (latte/espresso/cappuccino): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money = Rs{profit}")

    else:
        coffee_type = Menu.get(choice)

        if coffee_type is None:
            print("Invalid choice. Try again.")
        else:
            if check_resources(coffee_type["ingredients"]):
                payment = process_coins()
                if is_payment_successful(payment, coffee_type["cost"]):
                    make_coffee(choice, coffee_type["ingredients"])
