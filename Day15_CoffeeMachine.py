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
    "money" : 0
}

def ResourceChecker(drink):
    for values in MENU[drink]['ingredients']
    return True

    return False

def Payment(drink):
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    TotalPayment = (quarters*25 + dimes*10 + nickels*5 + pennies*1)/100
    CustomerChange = 0
    if drink == "latte":
        if TotalPayment - MENU["latte"]["cost"] < 0:
            print("Sorry that's not enough money. Money refunded. ")
        else:
            CustomerChange = TotalPayment - MENU["latte"]["cost"]
            resources['money'] += MENU["latte"]["cost"]
            if ResourceChecker("latte") == True:
                print(f"Here is your change: ${CustomerChange}")
            else:
                print(f"Not enough ingredients for {drink}")
    elif drink == "cappuccino":
        if TotalPayment - MENU["cappuccino"]["cost"] < 0:
            print("Sorry that's not enough money. Money refunded. ")
        else:
            CustomerChange = TotalPayment - MENU["cappuccino"]["cost"]
            resources['money'] += MENU["cappuccino"]["cost"]
            if ResourceChecker("cappuccino") == True:
                print(f"Here is your change: ${CustomerChange}")
            else:
                print(f"Not enough ingredients for {drink}")
    elif drink == "espresso":
        if TotalPayment - MENU["espresso"]["cost"] < 0:
            print("Sorry that's not enough money. Money refunded. ")
        else:
            CustomerChange = TotalPayment - MENU["espresso"]["cost"]
            resources['money'] += MENU["espresso"]["cost"]
            if ResourceChecker("espresso") == True:
                print(f"Here is your change: ${CustomerChange}")
            else:
                print(f"Not enough ingredients for {drink}")

UnitOn = 1
while UnitOn == 1:
    UserSelect = input("What would you like? (espresso/latte/cappuccino)")
    UserSelect = UserSelect.lower()
    if UserSelect == "off":
        print("Machine Turning Off")
        UnitOn = 0
    elif UserSelect == "report":
        for key,value in resources.items():
            print(key,' : ',value)
    elif UserSelect == "latte":
        Payment('latte')
    elif UserSelect == "cappuccino":
        Payment('cappuccino')
    elif UserSelect == "espresso":
        Payment('espresso')
    else:
        print("That is not a selectable drink")