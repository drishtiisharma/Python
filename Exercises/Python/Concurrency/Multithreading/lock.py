from threading import Thread, Lock
import time

lock = Lock()

def print_document(name):
    with lock:
        print(name,'started printing')
        time.sleep(3)
        print(name,'finished printing')

p1 = Thread(target=print_document,args=('Document 1',))
p2 = Thread(target=print_document,args=('Document 2',))

p1.start()
p2.start()

p1.join()
p2.join()

print("all documents finished printing")