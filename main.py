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
profit=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enogh{item}")
            return False
        else:
            return True

def process_coins():
    quar= int(input("How many Quarters:"))
    dime= int(input("How many Dimes:"))
    nick= int(input("How many Nickels:"))
    penn= int(input("How many Pennies:"))

    total_money= (quar*0.25)+(dime*.10)+(nick*0.05)+(penn*0.01)
    return total_money


def is_transaction_succesful(money_recieved, drink_cost):
    if money_recieved>= drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is {change}$ in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(" The Money is not enogh, it is refunded ")
        return False 

def make_coffee(drink_name, other_ingredients):
    for item in other_ingredients:
        resources[item] -= other_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy!!")





is_on= True

while is_on:
    choice=input(" What would you like to have? (espresso/latte/cappuccino)")
    if choice== "off": 
        is_on= False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}")
    
    else:
        drink= MENU[choice]
        if is_resource_enough(drink['ingredients']):
            payment=process_coins()
            if is_transaction_succesful(payment,drink["cost"]):
                make_coffee(choice,drink['ingredients'])
