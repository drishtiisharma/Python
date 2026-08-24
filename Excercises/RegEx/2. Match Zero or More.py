# match a string that has an a followed by zero or more bs (e.g., a, ab, abb).
import re
x = input()
if re.fullmatch(r"ab*",x):
    print("ab squence matched")
else:
    print("not matched")
