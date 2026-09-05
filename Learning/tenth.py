## SEQUENTIAL EXECUTION

# import threading

# def eat():
#     print("finished eating")
# def drink():
#     print("finished drinking")
# def code():
#     print("finished coding")

# t1 = threading.Thread(target=eat)
# t2 = threading.Thread(target=drink)
# t3 = threading.Thread(target=code)

# t1.start()
# t2.start()
# t3.start()


## CONCURRENT EXECUTION
# import threading
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

# t1 = threading.Thread(target=eat)
# t2 = threading.Thread(target=drink)
# t3 = threading.Thread(target=code)

# t1.start()
# t2.start()
# t3.start()

# print("main program finished")


## CONCURRENT EXECUTION WITH THREAD SYNCRONIZATION
# import threading
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

# t1 = threading.Thread(target=eat)
# t2 = threading.Thread(target=drink)
# t3 = threading.Thread(target=code)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("main program finished")

## RUN
# import threading
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

# t1 = threading.Thread(target=eat)
# t2 = threading.Thread(target=drink)
# t3 = threading.Thread(target=code)


# # executes the functions in the 'main' thread
# t1.run()
# t2.run()
# t3.run()


import threading
import time

def eat():
    time.sleep(3)
    print("finished eating", threading.current_thread().name)
def drink():
    time.sleep(2)
    print("finished drinking",threading.current_thread().name)
def code():
    time.sleep(5)
    print("finished code",threading.current_thread().name)


t1 = threading.Thread(target=eat)
t2 = threading.Thread(target=drink)
t3 = threading.Thread(target=code)

start = time.perf_counter()

t1.run()
t2.run()
t3.run()

end = time.perf_counter()

print("total time taken",end-start)




