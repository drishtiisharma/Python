from threading import Thread 
import time

def greet(name):
    print("thread started")
    time.sleep(3)
    print("hello "+name)
    print("thread finished")

g = Thread(target=greet,args=('drishti',))
g.start()
g.join()
print("main thread finished...")