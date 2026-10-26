from multiprocessing import Process, current_process
import time

def eat(name):
    print("running process:",current_process().name)
    print("started eating",name)
    time.sleep(3)
    print("finished eating",name)

def drink(name):
    print("running process:",current_process().name)
    print("started drink",name)
    time.sleep(3)
    print("finished drink",name)


if __name__ == "__main__":
    p1 = Process(
        target=eat,
        args=("snacks",),
        name='eating'
    )
    p2 = Process(
            target=drink,
            args=("soda",),
            name='drinking'
    )

    for x in p1,p2:
        x.start()
    for y in p1,p2:
        y.join()

