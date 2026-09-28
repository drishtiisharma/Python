# match a specific word only if it appears at the very beginning of a string.
import re
x = input()
if re.search(r"^the\b",x):
    print("matched string")
else:
    print("not matched")
