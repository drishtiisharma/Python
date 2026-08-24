#  match a string that has an a followed by one or more bs (e.g., ab, abb, but not a).
import re
x = input()
if re.fullmatch(r"ab+",x):
    print("atleast 1 b in the end")
else:
    print("not matched")