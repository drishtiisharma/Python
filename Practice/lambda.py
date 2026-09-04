# sq = lambda x : x**2
# print(sq(12))

## sorted - ordering/arranging data, creates a copy and leaves original data alone 
## while sort() modifies the original lsit directly in place
## both can be used with lambda function
# people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 28)]
# # sorted by age
# asc = sorted(people, key = lambda person: person[1])
# dsc = sorted(people, key = lambda person : person[1], reverse = True)
# print(asc,'\n',dsc)

## map - when we want to modify every item in a collection
# celsius = [0, 20, 37, 100]
# f = list(map(lambda c: (c*9/5)+32, celsius))
# print(f)

## filter - when we want a subset from a collection
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x : x % 2 == 0, numbers))
# print(even)

## chaining map and filter
# numbers = [-3, -1, 0, 2, 4, -2, 5, 7]
# res = list(
#     map(lambda n : n ** 2,
#         filter(lambda n: n>=0,numbers)
#     )
# )

# print(res)