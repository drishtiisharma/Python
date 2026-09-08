from multiprocessing import Process, Semaphore
import time

def work(num,semaphore):
    with semaphore:
        print('Process',num,'started')
        time.sleep(3)
        print('Process',num,'finished')

if __name__ == '__main__':
    semaphore = Semaphore(4) # all 4 processes start together and end together

    processes = []

    for i in range(4):
        p = Process(target=work,args=(i,semaphore))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

# output:
# Process 0 started
# Process 1 started
# Process 2 started
# Process 3 started
# Process 0 finished
# Process 1 finished
# Process 2 finished
# Process 3 finished