import threading
import time

def eat():
    time.sleep(3)
    print("finished eating")
def drink():
    time.sleep(2)
    print("finished drinking")
def code():
    time.sleep(5)
    print("finished coding")

t1 = threading.Thread(target=eat)
t2 = threading.Thread(target=drink)
t3 = threading.Thread(target=code)

start = time.perf_counter()
t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
end = time.perf_counter()

print("total time taken",end-start)
# total time taken 5.001122599991504