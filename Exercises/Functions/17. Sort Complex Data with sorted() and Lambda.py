# Exercise 17. Sort Complex Data with sorted() and Lambda
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
s = sorted(students, key = lambda student: student[1]) # indexing in tuple : 0-> name, 1-> marks

print(s)