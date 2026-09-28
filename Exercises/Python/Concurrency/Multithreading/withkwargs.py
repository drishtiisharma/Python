from threading import Thread 
import time

def intro(name,age):
    print("thread started")
    time.sleep(3)
    print("hello, i'm",age,"years old and my name is",name)
    time.sleep(2)
    print("thread finished")

i = Thread(target=intro,
kwargs= {"age":"22","name":'drishti'})
i.start()
i.join()
print("main thread finished...")