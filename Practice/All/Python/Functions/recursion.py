'''
recursion
---------

technique where a function calls itself to solve smaller version of the same problem

base case: condition that stops trhe iteration
recursive case: part where the function keeps calling itself with smaller or more simpler output

'''

def countdown(n):
    if n == 0:
        print("doneee")
        return

    print(n)
    countdown(n-1)

countdown(5)


# factorial
def fact(n):
    if n == 0 or n == 1:
        return 1

    return n * fact(n-1)

print(fact(5))

# sum of numberss

def addn(n):
    if n == 0:
        return 0
    return n + addn(n-1)
print(addn(10))