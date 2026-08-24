# find sequences of one uppercase letter followed by lowercase letters (e.g., Hello, World, Python).
import re
x = input()
if re.fullmatch(r"[A-Z][a-z]+",x):
    print("PascalCase")
else:
    print("not PascalCase")