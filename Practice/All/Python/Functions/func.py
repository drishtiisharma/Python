def count(x,y):
    for i in range(x,y+1):
        print(i)

a = int(input("starting num: ")) 
b = int(input("ending num: "))
count(a,b)

def largest(m,n,o):
    max = m
    if n>m and n>o:
        max = n
    elif o>m and o>n:
        max = o
    else:
        max = m
    print(max)

largest(29,49,56)