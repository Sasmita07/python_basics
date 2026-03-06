import time
import multiprocessing

square_result = []
def calc_square(numbers):
    for number in numbers:
        #time.sleep(5)
        print("square:",number*number)
        square_result.append(number*number)
        print("square_result is:",square_result)

def calc_cube(numbers):
    for number in numbers:
        #time.sleep(5)
        print("cube:",number*number*number)

if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target= calc_square, args=(arr,))
    p2 = multiprocessing.Process(target= calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done", square_result)