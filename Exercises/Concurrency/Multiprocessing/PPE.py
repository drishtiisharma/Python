from concurrent.futures import ProcessPoolExecutor
import time

def sq(num):
    time.sleep(3)
    return num * num

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as exe:

        f1 = exe.submit (sq,5)
        f2 = exe.submit (sq,2)

        print(f1.result())
        print(f2.result())