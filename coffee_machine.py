from doctest import register_optionflag
from operator import truediv
from warnings import catch_warnings

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# TODO 1. print report of all of the coffee machine resources
# TODO 2. check resources sufficient to make drink order
# TODO 3. take coins

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def make_coffee(coffee_type):

    coffee_ingredients = MENU[coffee_type]["ingredients"]

    MENU["espresso"]["ingredients"]["milk"] = 0

    if coffee_ingredients["water"] > resources["water"]:
        print("Sorry there is not enough water.")
    elif coffee_ingredients["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif coffee_ingredients["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
    else:
        print("Please insert coins.")
        # penny 0.01, nickel 0.05, dime 0.10, quarter 0.25
        num_quarters = int(input("how many quarters?: "))
        num_dimes = int(input("how many dimes?: "))
        num_nickels = int(input("how many nickles?: "))
        num_pennies = int(input("how many pennies?: "))

        total_coins = round((0.25 * num_quarters + 0.1 * num_dimes + 0.05 * num_nickels + 0.01 * num_pennies), 2)

        if total_coins > MENU[coffee_type]["cost"]:
            change = round(total_coins - MENU[coffee_type]["cost"], 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_type} ☕️")
            resources["money"] += float(total_coins - change)
            for ingredient in "water", "milk", "coffee":
                resources[ingredient] -= coffee_ingredients[ingredient]
        else:
            print("Sorry that's not enough money. Money refunded.")

        # print(f"You have entered: {total_coins}, total price of coffee is {MENU.get(coffee_type).get("cost")}")

    return None

# 1: Prompt user (insert in while loop)
power_on = True

while power_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
# 2: Turn off Coffee machine by entering "off" to the prompt
    if user_choice.lower() == "off":
        power_on = False
# 3: Print report
    elif user_choice.lower() == "report":
        report()
    elif user_choice.lower() == "espresso" or user_choice.lower() == "latte" or user_choice.lower() == "cappuccino":
        make_coffee(user_choice.lower())
    else:
        print("Invalid choice, please try again")