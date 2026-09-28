# Exercise 11. Create a Function with Keyword Arguments
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_info(name = "drishti",age =19)