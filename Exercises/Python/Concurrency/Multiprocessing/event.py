from multiprocessing import Process, Event
import time

def worker1(event):
    print("worker 1 : doing some work...")
    time.sleep(3)
    print("worker 1 : work finished!")
    
def worker2(event):
    event.wait() # waits for signal
    print("worker 2 : doing some work...")
    print("worker 2 : work finished!")

if __name__ == "__main__":
    
    event = Event()

    p1 = Process(target=worker1,args=(event,))
    p2 = Process(target=worker2,args=(event,))

    p1.start()
    p2.start()
    p1.join()
    print("lets check")
    time.sleep(5)
    event.set() # sends the signal to continue
    p2.join()
