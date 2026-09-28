# Exercise 9: Sorted with Multiple Keys
# Problem Statement: Given a list of employee dictionaries, each with a "name" and a "salary" key, sort the list by salary in descending order. Where two employees share the same salary, sort those entries by name in ascending alphabetical order. Use a single lambda as the key argument.
employees = [{"name": "Alice", "salary": 70000}, {"name": "Bob", "salary": 90000}, {"name": "Charlie", "salary": 70000}, {"name": "Diana", "salary": 90000}]
s = sorted(
    employees,
    key = lambda e: (-e['salary'],e['name'])
)

for x in s:
    print(f"{x['name']:<8} : ${x['salary']}")