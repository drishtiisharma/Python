from multiprocessing import Process, Value, Lock
import time

def withdraw(balance,amt,lock):
    with lock:
        if balance.value >= amt:
            print("current balance: ",balance.value)
            time.sleep(3)

            balance.value -= amt
            print("withdrawn: ",amt)
        else:
            print("balance cannot be 0")

if __name__ == '__main__':
    
    balance = Value('i',1000)
    lock = Lock()

    p1 = Process(target=withdraw,args=(balance,700,lock))
    p2 = Process(target=withdraw,args=(balance,700,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("final balance: ",balance.value)