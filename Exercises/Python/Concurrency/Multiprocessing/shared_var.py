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
