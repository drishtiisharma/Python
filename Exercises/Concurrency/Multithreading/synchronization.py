from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
import time

lock = Lock()

def work(name):
    with lock:
        print(name,"started")
        time.sleep(2)
        print(name,"finished")

tasks = ['thread 1','thread 2']

with ThreadPoolExecutor(max_workers=2) as exe:
    for task in tasks:
        exe.submit(work,task)

 