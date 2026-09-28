from threading import Thread 
import time

def task():
    print("thread started")
    time.sleep(5)
    print("thread finished")

t = Thread(target=task)

t.start()

print("main thread...")