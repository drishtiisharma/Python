# Exercise 12. Modifying Global Variables
def change(global_var):
    global x
    x = 20
    return x

global_var = 10
print(change(global_var))