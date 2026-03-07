from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(n):
        sum += x * x
    return sum

if __name__ == "__main__":
    #arr = [1,2,3,4,5]
    t1 = time.time()
    p = Pool()
    #result = p.map(f, arr)
    result = p.map(f, range(10000))
    p.close()
    p.join()
    print("Pool duration:", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))
    print("Serial processing duration:", time.time() - t2)


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    t1 = time.time()
    p = Pool(processes= 3)
    result = p.map(f, arr)
    p.close()
    p.join()
    print("Pool duration:", time.time() - t1)
