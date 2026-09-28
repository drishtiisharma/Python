from multiprocessing import Process

count = 0

def change():
    global count
    count = 10
    print("child: ",count)

if __name__ == '__main__':
    print("before: ",count)
    
    p = Process(target=change)
    p.start()
    p.join()

    print("after:",count)