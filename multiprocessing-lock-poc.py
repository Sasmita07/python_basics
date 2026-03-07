import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.1)
        # critical section
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdrawn(balance, lock):
    for i in range(100):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == "__main__":
    balance  = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target= deposit, args=(balance,lock))
    w = multiprocessing.Process(target= withdrawn, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print("final balance:", balance.value)