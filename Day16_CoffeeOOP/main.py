from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the coffee machine")

MenuScreen = Menu()
CoffeeMachine = CoffeeMaker()
CoinMachine = MoneyMachine()

SystemStatus = 'On'
while SystemStatus == 'On':
    Choices = MenuScreen.get_items()
    UserChoice = input(f"What would you like to drink? [{Choices}] ")

    UserChoice.lower()
    if UserChoice == "off":
        SystemStatus = "Off"
    elif UserChoice == "report":
        CoffeeMachine.report()
        CoinMachine.report()
    else:
        drink = MenuScreen.find_drink(UserChoice)
        if CoffeeMachine.is_resource_sufficient(drink) and CoinMachine.make_payment(drink.cost):
            CoffeeMachine.make_coffee(drink)

