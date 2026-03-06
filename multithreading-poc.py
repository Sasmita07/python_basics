import time 
import threading

def calc_square(numbers):
    print("Calculate Squares")
    for number in numbers:
        time.sleep(0.2)
        print("square:",number*number)

def calc_cube(numbers):
    print("Calculate Cubes")
    for number in numbers:
        time.sleep(0.2)
        print("cube:",number*number*number)

arr = [7,4,5,6]
t = time.time()
t1 = threading.Thread(target = calc_square, args=(arr,))
t2 = threading.Thread(target = calc_cube, args=(arr,))

t1.start()
t2.start()

# wait until t1, t2 is done
t1.join()
t2.join()

print("completed in:", time.time() - t)