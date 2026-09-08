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