# find sequences of lowercase letters joined with an underscore (e.g., hello_world).
import re
x = input()
if re.fullmatch(r"[a-z]+_[a-z]+",x):
    print("lowercase and underscore matched")
else:
    print("not matched")