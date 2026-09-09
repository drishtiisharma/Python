# Sharing Data with Processes

Multiprocessing module provides shared-memory objects and managers for sharing data between processes.

## Sharing Data using Array & Value

Array and Value provide shared memory that can be accessed by multiple processes.

```python
from multiprocessing import Process, Array, Value

def update_cart(cart,total):
    cart[0] = 20
    cart[1] = 30
    cart[2] = 10

    total.value = sum(cart)

if __name__ == "__main__":
    cart = Array('i',[0,0,0])
    total = Value('i',0)

    p = Process(target=update_cart,args=(cart,total))

    p.start()
    p.join()

    print("items: ",cart[:])
    print("total items:",total.value)
```

**Explanation**: This code creates a **shared array** called `cart` containing three values and a **shared single value** called `total`. A separate process `p` runs the `update_cart()` function, where it changes the shared array to `[20, 30, 10]` and then calculates their sum, storing `60` in the shared `total`. After `p.join()` ensures that the child process has finished, the main process prints the same updated values. The important point is that **`Array` lets multiple processes share multiple values, while `Value` lets them share one value**, so the changes made by the child process are visible to the main process.


## Sharing Python Objects Using Manager

multiprocessing.Manager() can create shared objects such as lists and dictionaries that can be accessed by multiple processes.

```python
from multiprocessing import Process, Manager

def add_items(items):
    items.append("milk")

def remove_items(items):
    items.pop(1)

if __name__ == '__main__':
    with Manager() as manager:

        items = manager.list(['bread','eggs'])
        p = Process(target=add_items,args=(items,))
        q = Process(target=remove_items,args=(items,))

        p.start()
        p.join()
        print('shopping list: ',list(items))
        q.start()
        q.join()
        print('shopping list: ',list(items))
```

