# simple way
# l = [10,10,20,4,20,10]
# print(l)
# n=int(input("num:"))
# print(l.count(n))

#using loops
l = [10,10,20,4,20,10]
print(l)
n=int(input("num:"))

count = 0
for x in l:
    if x == n:
        count+=1
print(count)