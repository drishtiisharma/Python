from multiprocessing import Process, current_process, cpu_count
import time

def eat(name):
    print("running process : ",current_process().name)
    print('started eating',name)
    time.sleep(3)
    print('finished eating',name)
 
def drink(name):
    print("running process : ",current_process().name)
    print('started drinking',name)
    time.sleep(3)
    print('finished drinking',name)


if __name__ == "__main__":
    p1 = Process(target=eat,args=('snacks',),name='eating')
    p2 = Process(target=drink,args=('cola',),name='drinking')

    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print("total number of logical cpus : " ,cpu_count()) # returns the number of logical CPUs
