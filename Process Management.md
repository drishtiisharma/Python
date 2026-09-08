# Process Management

## Creating Processes

## Checking Process ID & Status

## Memory Isolation between Processes

Each process has its own memory space. A normal global variable changed inside a child process does not change the corresponding variable in the main process.

```python
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
```

