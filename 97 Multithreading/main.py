import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicate some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    # Normal Code
    # func(4)
    # func(2)
    # func(1)

    # Same code with thread
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


def poolingDemo():
    with ThreadPoolExecutor() as executer:
        # future1 = executer.submit(func, 3)
        # future2 = executer.submit(func, 2)
        # future3 = executer.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3, 4, 5, 7]
        results = executer.map(func, l)
        for result in results:
            print(result)

    
poolingDemo()