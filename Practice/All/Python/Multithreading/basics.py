# sequential execution
# import time

# def eat():
#     time.sleep(3)
#     print("finished eating")

# def drink():
#     time.sleep(1)
#     print("finished drinking")

# def code():
#     time.sleep(5)
#     print("finished coding")  

# start = time.perf_counter()
# eat()
# drink()
# code()
# end = time.perf_counter()

# print("total time taken: ",end-start)
    

# concurrent execution
import threading
import time

def eat():
    time.sleep(3)
    print("finished eating")

def drink():
    time.sleep(1)
    print("finished drinking")

def code():
    time.sleep(5)
    print("finished coding")  

t1 = threading.Thread(target=eat)
t2 = threading.Thread(target=drink)
t3 = threading.Thread(target=code)

start = time.perf_counter()
for a in t1,t2,t3:
    a.start()

for x in t1,t2,t3:
    x.join()
end = time.perf_counter()
print("total time taken: ",end-start)
