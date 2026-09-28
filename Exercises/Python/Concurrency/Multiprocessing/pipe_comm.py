import multiprocessing

def sender(conn):
    conn.send("helloo")

def receiver(conn):
    message = conn.recv()
    print("received: ",message)

if __name__ == "__main__":
    
    parent_conn, child_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(
        target = sender,
        args =  (parent_conn,)
    )

    p2 = multiprocessing.Process(
        target = receiver,
        args =  (child_conn,)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

