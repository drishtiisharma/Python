# Exercise 2: Lambda with Sorting
# Problem Statement: Given a list of (name, age) tuples, sort them in ascending order by age using sorted() with a lambda as the key argument. Then sort the same list in descending order by age.
l = [("alice",24),("john",15),("steve",56),("crystal",9)]
a = sorted(l, key = lambda l : l[1])
d = sorted(l, key = lambda l : l[1], reverse = True) 
print("Ascending Order:")
print(a)
print("Descending Order:")
print(d)