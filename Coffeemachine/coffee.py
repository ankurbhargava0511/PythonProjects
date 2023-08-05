from config import MENU, resources

class coffee():


    def check_resources(self,coffee):
        resource_available = True
        ingredients = MENU[coffee]["ingredients"]
        if "water" in ingredients and ingredients["water"] > resources["water"]:
            resource_available = False
        if "milk" in ingredients and ingredients["milk"] > resources["milk"]:
            resource_available = False
        if "coffee" in ingredients and ingredients["coffee"] > resources["coffee"]:
            resource_available = False
        return resource_available

    def check_payment(self,coffee):
        ##3c take Payment
        price = MENU[coffee]["cost"]
        print(f"Cost of Coffee is {price}")
        print("Insert No of Notes")
        input_50 = input("50:")
        input_100 = input("100:")
        input_200 = input("200:")
        input_500 = input("500:")

        total_money_provided = int(input_50) * 50 + int(input_100) * 100 + int(input_200) * 200 + int(input_500) * 500
        if total_money_provided < int(price):
            print("Insufficient Amount.")
            return -1

        else:
            # global total_earning
            price_of_coffee = int(price)
            return_amount = total_money_provided - price_of_coffee
            print(f"Amount Refunded:{return_amount}")
            return price_of_coffee

    def reduce_resorces(self, coffee):
        ingredients = MENU[coffee]["ingredients"]
        for rec in resources:
            if rec in ingredients:
                used=ingredients[rec]
                resources[rec] -= used

    def make_coffee(self):
        for i in MENU:
            print(i + "\n")
        selected_coffee = input("Please select coffee from above list.\n")
        amount_earn=-1
        resources_available = self.check_resources(selected_coffee)
        if not resources_available:
            ##3b Check resources
            print("Insufficient Resources. Please Try Later or add Resources.")
        else:
            amount_earn = self.check_payment(selected_coffee)
            if amount_earn > 0:
                self.reduce_resorces(selected_coffee)
                print("Making Your Coffee......")
                print("Enjoy your " + selected_coffee)

        return amount_earn