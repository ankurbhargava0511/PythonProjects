#task
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

notes_in_inr = [50, 100, 200, 500]
total_earning=0

def check_resources(coffee):
    resource_available= True
    ingredients =MENU[coffee]["ingredients"]
    if "water" in ingredients and ingredients["water"]>resources["water"]:
        resource_available = False
    if "milk" in ingredients and ingredients["milk"]>resources["milk"]:
        resource_available = False
    if "coffee" in ingredients and ingredients["coffee"] > resources["coffee"]:
        resource_available = False
    return resource_available

def check_payment(coffee):
    ##3c take Payment
    price =MENU[coffee]["cost"]
    print (f"Cost of Coffee is {price}")
    print("Insert No of Notes")
    input_50 =input("50:")
    input_100 = input("100:")
    input_200 = input("200:")
    input_500 = input("500:")

    total_money_provided= int(input_50)*50 + int(input_100)*100 +int(input_200)*200+int(input_500)*500
    if total_money_provided < int(price):
        print("Insufficient Amount.")
        return -1

    else:
        #global total_earning
        price_of_coffee = int(price)
        return_amount= total_money_provided-price_of_coffee
        print (f"Amount Refunded:{return_amount}")
        return price_of_coffee



machine_on=True

while machine_on:

    user_input=input("Type 1 - To Select a coffee from menu \nType 2 - To switch off the machine \nType 3 - To add resources.\nType 4 - Get Report\n")
    if user_input == "1":
        # 3make_coffee
        ##3a ask for type of coffee
        for i in MENU:
            print (i + "\n")
        selected_coffee=input("Please select coffee from above list.\n")

        resources_available=check_resources(selected_coffee)
        if not resources_available:
            ##3b Check resources
            print("Insufficient Resources. Please Try Later or add Resources.")
        else:
            amount_earn=check_payment(selected_coffee)
            if amount_earn >0:
                ##3d make_coffee
                total_earning = + amount_earn
                print("Making Your Coffee......")
                print("Enjoy your " + selected_coffee)






    elif user_input =="2":
        # 1Switch off the machine
        machine_on = False
    elif user_input =="3":
        # 2recharge_resources
        for i in resources:
            print(i)
        user_resources = input("Select the resource to above list\n")
        user_quantity = input("Please provide quantity in 100's\n")

        resources[user_resources] += int(user_quantity) * 100
    elif user_input =="4":
        user_input_report=input("Type 1 - To Get Sales \nType 2 - To Get resources\n")
        if user_input_report=="1":
            print(f"Your Total Earning for Today is : {total_earning}")
        else:
            for i in resources:
                print(str(i) + ":" + str(resources[i]))
    else:
        print("invalid Selection")




#3make_coffee
##3a ask for type of coffee
##3b Check resources
##3c take Payment
##3d make_coffee