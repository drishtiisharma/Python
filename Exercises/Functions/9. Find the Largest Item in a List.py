# Exercise 9. Find the Largest Item in a List
def maxx(l):
    f = l[0]
    for i in l:
      if i > f:
        f = i
    return f


x = [4, 6, 8, 24, 12, 2]
print(maxx(x))