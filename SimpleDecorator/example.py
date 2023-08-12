import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper():
        current_time1=time.time()
        function()
        current_time2=time.time()
        run_time=current_time2-current_time1
        print(f"function {function.__name__} runtime is {run_time}")


    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()