# match a string that starts with a, ends with b, and has any characters in between (e.g., a123b, axyzb).
import re
x = input()
if re.fullmatch(r"a.*b",x):
    print("matched")
else:
    print("not matched")