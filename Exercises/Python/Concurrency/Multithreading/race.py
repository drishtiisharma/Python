from threading import Thread 
import time

x = 0

def inc():
    global x

    temp = x
    time.sleep(3)
    x = temp + 1

t1 = Thread(target=inc)
t2 = Thread(target=inc)

# this would result in a race condition
t1.start()
t2.start()

t1.join()
t2.join()

print("final value of x : ",x) # output: x = 1

# # this would NOT result in a race condition
# t1.start()
# t1.join()
# t2.start()
# t2.join()

# print("final value of x : ",x) # output: x = 2


