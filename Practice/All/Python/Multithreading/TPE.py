from concurrent.futures import ThreadPoolExecutor
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

start = time.perf_counter()

tasks = [eat,drink,code]

with ThreadPoolExecutor(max_workers=3) as exe:
    for task in tasks:
        exe.submit(task)
end = time.perf_counter()
print("total time taken: ",end-start)