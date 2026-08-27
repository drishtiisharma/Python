# Exercise 6: Finally Block
# Problem Statement: Write a function read_file(filename) that opens a file manually (without a with statement), reads its contents, and uses a finally block to ensure the file handle is always closed, whether the read succeeds or an exception is raised.
def read_file(filename):
    f = None
    try:
        f = open(filename, "r")
        content = f.read()
        print("----------------------------------------------")
        print(f"{filename:>20} opened")
        print("----------------------------------------------")
        print(content)
        print("----------------------------------------------")

    except FileNotFoundError:
        print("----------------------------------------------")
        print(f"{filename:>20} not found")

    finally:
        if f:
            f.close()
        print("----------------------------------------------")
        print(f"{filename:>20} closed")
        print("----------------------------------------------")


# read_file("root.txt")
read_file("lemon.txt")
