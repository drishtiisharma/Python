# Exercise 2. Variable Length of Arguments ( *args )
def func(*args):
    return "helloooo" + " " + " ".join(args)
print((func("drishti","khushi")))