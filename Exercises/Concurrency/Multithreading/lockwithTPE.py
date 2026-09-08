from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
import time

lock = Lock()

def print_docs(name):
  with lock:
    print(name,"started printing")
    time.sleep(3)
    print(name,"finished printing")

docs = ['Document 1','Document 2']

with ThreadPoolExecutor(max_workers=2) as exe:
  for doc in docs:
    exe.submit(print_docs,doc)

time.sleep(3)
print("all docs finished printing")