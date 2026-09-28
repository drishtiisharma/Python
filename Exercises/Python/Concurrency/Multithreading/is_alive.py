from threading import Thread 
import time

def task():
    print("task has started")
    time.sleep(5)
    print("task has finished")

t = Thread(target=task)

print(t.is_alive()) # false

t.start() 
print(t.is_alive()) # true

t.join()
time.sleep(5)
print(t.is_alive()) # false (because of .join)