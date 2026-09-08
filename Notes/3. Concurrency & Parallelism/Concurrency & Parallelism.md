
## List of Topics:

[[1. Multithreading]]
[[2. Multiprocessing]]
[[3. Async Programming]]

## Some Common Terms

### **`start()`**

This method starts the thread and tells Python to execute its `run()` method in a separate thread. After calling `start()`, the thread can begin executing whenever the scheduler gives it CPU time.

### **`join()`**

This method makes the calling thread (usually the main thread) **wait until the target thread finishes**. It is used when we need to make sure a thread has completed its work before the program continues.


### **`is_alive()`**

This method returns `True` if the thread is still running and `False` if it has finished. It allows us to check the thread's status **without waiting for it**.

```python
from threading import Thread 
import time

def task():
    print("task has started")
    time.sleep(5)
    print("task has finished")

t = Thread(target=task)

print(t.is_alive()) # false

t.start() 
print(t.is_alive()) # true

t.join()
time.sleep(5)
print(t.is_alive()) # false (because of .join)
```


### **Daemon**

By default, threads are non-daemon.

A daemon thread is a **background thread** that does not prevent the program from ending. If the main program finishes and only daemon threads are left, Python stops those threads automatically.

They are generally used for background tasks that are **not essential** to complete, such as monitoring or logging.

**Non-daemon (By Default):**

```
from threading import Thread 
import time

def task():
    print("thread started")
    time.sleep(5)
    print("thread finished")

t = Thread(target=task)

t.start()

print("main thread...")
```

Output :
```
thread started
main thread...
thread finished
```

**Explanation:**

Python says:

> "There's a non-daemon thread still running. I have to wait."

So the **program does NOT terminate** until `t` finishes.

**Daemon:**

```
from threading import Thread 
import time

def task():
    print("thread started")
    time.sleep(5)
    print("thread finished")

t = Thread(target=task, daemon=True)

t.start()

print("main thread...")
```

Output:
```
thread started
main thread...
```

**Explanation:**
Python says:

> "The main thread is finished, and the only remaining thread is a daemon. I don't need to wait."

So **the entire program terminates**.


### **Arguments**

Arguments allow us to **pass data to the function running inside a thread**.

We use:

- `args` → for positional arguments (tuple)
- `kwargs` → for keyword arguments (dictionary)


```python
Thread(target=work, args=(10,))
Thread(target=work, kwargs={"name": "D"})
```

This allows the same function to be used with different values in different threads.

### **Synchronization**

Synchronization means **coordinating multiple threads** so that they work together safely.

It is mainly needed when threads share data or resources. Python provides mechanisms such as **locks, events, and semaphores** for synchronization.

```python
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
```

**Explanation:** Here, two threads are trying to use the same resource. The `Lock` makes them work **one at a time** instead of both entering the section together. `with lock:` means a thread gets the lock, does its work, and then releases the lock. This coordination between threads is called **synchronization**.
### **Race Condition**

A race condition happens when **multiple threads access and modify the same shared data at nearly the same time**, and the final result depends on which thread executes first.

For example, if two threads try to increase the same counter simultaneously, the final value may be incorrect.

```python
from threading import Thread 
import time

x = 0

def inc():
    global x

    temp = x
    time.sleep(3)
    x = temp + 1

t1 = Thread(target=inc)
t2 = Thread(target=inc)

# this would result in a race condition
t1.start()
t2.start()

t1.join()
t2.join()

print("final value of x : ",x) # output: x = 1

# # this would NOT result in a race condition
# t1.start()
# t1.join()
# t2.start()
# t2.join()

# print("final value of x : ",x) # output: x = 2

```

**Explanation**: Both threads are changing the same `counter`. A thread first reads the value into `temp`, waits for a moment, and then increases it. During this time, the other thread can also read and change `counter`. Because both threads are accessing the same data at the same time, some increments can be lost. This situation, where the final result depends on **which thread runs first**, is called a **race condition**.
### **Locks**

A lock allows **only one thread at a time** to execute a particular section of code.

A thread acquires the lock before accessing shared data and releases it afterward. This prevents other threads from interfering while the operation is being performed.

```python
from threading import Thread, Lock
import time

lock = Lock()

def print_document(name):
    with lock:
        print(name,'started printing')
        time.sleep(3)
        print(name,'finished printing')

p1 = Thread(target=print_document,args=('Document 1',))
p2 = Thread(target=print_document,args=('Document 2',))

p1.start()
p2.start()

p1.join()
p2.join()

print("all documents finished printing")
```

The protected section is called a **critical section**.

**Explanation**: This program creates **two threads**, `p1` and `p2`, that both want to print a document. The `Lock()` ensures that **only one thread can print at a time**. When `p1.start()` and `p2.start()` are called, both threads begin, but the thread that gets the lock first enters the `with lock:` block, prints that its document has started, waits for 3 seconds, and then prints that it has finished. The other thread has to **wait for the lock to be released**, then it prints its document. `p1.join()` and `p2.join()` make the main thread wait until both printing threads are completely finished. Finally, `"all documents finished printing"` is printed. So this program demonstrates **synchronization using a lock**—the two threads can run concurrently, but access to the printing section happens **one at a time**.

**Lock with TPE:**

```python
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
```

One way to remember the relation between Locks, Synchronization and Race Condition

> [!NOTE]
> A **lock** is a method of **synchronization** used to prevent **race conditions** when multiple threads access shared data or resources.

