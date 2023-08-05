from config import resources


class Report():

    def __init__(self):
        self.total_earning = 0

    def print_report(self):
        user_input_report = input("Type 1 - To Get Sales \nType 2 - To Get resources\n")
        if user_input_report == "1":
            print(f"Your Total Earning for Today is : {self.total_earning}")
        else:
            for i in resources:
                print(str(i) + ":" + str(resources[i]))
