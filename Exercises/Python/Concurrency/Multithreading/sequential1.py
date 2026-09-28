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

start = time.perf_counter()
eat()
drink()
code()
end = time.perf_counter()

print("total time taken",end-start)
# total time taken 10.001038400019752

