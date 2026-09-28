from multiprocessing import Process, Value
import time

def withdraw(balance,amt):
    if balance.value>=amt:
        print("Balance available: ",balance.value)
        time.sleep(3)
        balance.value -=amt
        print("withdrawn: ",amt)
    else:
        print("balance cannot be 0")

if __name__ == '__main__':
    balance = Value('i',1000)

    p1 = Process(target=withdraw,args=(balance,700))
    p2 = Process(target=withdraw,args=(balance,700))
    
    # race condition
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("final balance: ",balance.value) # returns -400
