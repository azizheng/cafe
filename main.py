from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
still_running = True

my_coffee_maker.report()
my_money_machine.report()

while still_running:
    drink = input(f"What would you like? {my_menu.get_items()}")
    if drink == "off":
        still_running = False
    elif drink == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        my_drink = my_menu.find_drink(drink)
        if my_coffee_maker.is_resource_sufficient(my_drink) and my_money_machine.make_payment(my_drink.cost):
            my_coffee_maker.make_coffee(my_drink)
