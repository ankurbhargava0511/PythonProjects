
from report import Report
from machine import coffee_machine
from coffee import coffee
report = Report()
mac = coffee_machine()
my_coffee= coffee()

while mac.machine_is_on:

    user_input=input("Type 1 - To Select a coffee from menu \nType 2 - To switch off the machine \nType 3 - To add resources.\nType 4 - Get Report\n")
    if user_input == "1":
       earning=my_coffee.make_coffee()
       report.total_earning +=earning
    elif user_input =="2":
        mac.switch_off_machine()
    elif user_input =="3":
       mac.recharge_machine()
    elif user_input =="4":
        report.print_report()
    else:
        print("invalid Selection")


