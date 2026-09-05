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

```
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

### **Race Condition**

A race condition happens when **multiple threads access and modify the same shared data at nearly the same time**, and the final result depends on which thread executes first.

For example, if two threads try to increase the same counter simultaneously, the final value may be incorrect.

### **Locks**

A lock allows **only one thread at a time** to execute a particular section of code.

A thread acquires the lock before accessing shared data and releases it afterward. This prevents other threads from interfering while the operation is being performed.

```python
with lock:
    counter += 1
```

The protected section is called a **critical section**.