from multiprocessing import Process, Queue
import time
def sender(q):
    q.put("helloooo")
    q.put("how're you?")
    q.put("byeeee")

def receiver(q):
    while not q.empty():
        message = q.get()
        time.sleep(3)
        print("recieved:",message)
        

if __name__ == "__main__":

    q = Queue()

    p1 = Process(target=sender,args=(q,))
    p2 = Process(target=receiver,args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()