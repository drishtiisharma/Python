# match a string that has an a followed by exactly three bs (i.e., only abbb is a valid match).
import re
x = input()
if re.fullmatch(r"ab{3}",x):
    print("3 bs matched")
else:
    print("string not matched")