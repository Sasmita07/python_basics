import time

def time_it(func):
    def wrapper_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ +" duration:", str((end-start)*1000)+" ms")
        return result
    return wrapper_func

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

arr = range(1, 10000)
out_square = calc_square(arr)
out_cube = calc_cube(arr)

#print(out_square)
#print(out_cube)