# from concurrent.futures import ThreadPoolExecutor
# import time

# def eat():
#     time.sleep(3)
#     print("finished eating")
# def drink():
#     time.sleep(2)
#     print("finished drinking")
# def code():
#     time.sleep(5)
#     print("finished coding")

# start = time.perf_counter()

# with ThreadPoolExecutor(max_workers=3) as exe:
#     exe.submit(eat)
#     exe.submit(drink)
#     exe.submit(code)

# end = time.perf_counter()

# print("total time taken: ",end-start)
# total time taken:  5.00136019999627

## ANOTHER APPROACH

from concurrent.futures import ThreadPoolExecutor
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

tasks = [eat,drink,code]

with ThreadPoolExecutor(max_workers=3) as exe:
    for task in tasks:
        exe.submit(task)

end = time.perf_counter()

print("total time taken: ",end-start)
# total time taken:  5.001382399990689