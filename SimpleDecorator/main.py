import time


def delay_decorator(function):
    def wrapper_function():
        print("Sleeping start....")
        time.sleep(2)
        print("Sleeping end....")
        print("func execution start....")
        function()
        print("func execution end....")
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

say_hello()