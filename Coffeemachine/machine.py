from config import resources
class coffee_machine(object):

    def __init__(self):
        self.machine_is_on = True

    def recharge_machine(self):
        # 2recharge_resources
        for i in resources:
            print(i)
        user_resources = input("Select the resource to above list\n")
        user_quantity = input("Please provide quantity in 100's\n")

        resources[user_resources] += int(user_quantity) * 100

    def switch_off_machine(self):
        self.machine_is_on = False
        return self.machine_is_on

    def machine_is_on(self):
        return self.machine_is_on
