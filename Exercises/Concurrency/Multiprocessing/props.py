from multiprocessing import Process
import time
import os

def worker1():
  pid = os.getpid()
  print("process",pid,"started")
  time.sleep(3)
  print("process",pid,"finished")

def worker2():
  pid = os.getpid()
  print("process",pid,"started")
  time.sleep(3)
  print("process",pid,"finished")

if __name__ == '__main__':  
    w1 = Process(target=worker1)
    w2 = Process(target=worker2)

    print("...program starts...")

    w1.start()
    w2.start()
    print(w1.is_alive())
    print(w2.is_alive())

    w1.join()
    w2.join()
    print(w1.is_alive())
    print(w2.is_alive())

    print("...program ended...")