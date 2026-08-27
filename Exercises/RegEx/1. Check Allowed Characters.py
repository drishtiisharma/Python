# string contains only alphanumeric characters (a-z, A-Z, and 0-9).
import re
x = input()
if re.fullmatch(r"[a-zA-Z0-9]+",x):
    print("matched")
else:
    print("something else")