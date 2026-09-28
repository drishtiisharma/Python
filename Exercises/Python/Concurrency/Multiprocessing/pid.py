from multiprocessing import Process, current_process
import time
import os

def work1(name):
    time.sleep(3)
    pname = current_process().name
    print("running process: ", pname,'\n',pname+"'s process id: ",os.getpid())
def work2(name):
    time.sleep(3)
    pname = current_process().name
    print("running process: ",pname,'\n',pname+"'s process id: ",os.getpid())

if __name__ == '__main__':
    p1 = Process(target=work1,args=('process 1',))
    p2 = Process(target=work2,args=('process 2',))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()

    

    