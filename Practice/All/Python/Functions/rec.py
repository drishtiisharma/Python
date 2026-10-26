# 1 to 10
def count(n):
    if n > 10:
        return
    print(n)
    count(n+1)

count(1)

# 10 to 1
def count(n):
    if n < 1:
        return
    print(n)
    count(n-1)

count(10)


