# match a string that has an a followed by two to three bs (i.e., abb or abbb).
import re
x = input()
if re.fullmatch(r"ab{2,3}",x):
    print("2-3 occurences of b matched")
else:
    print("not matched")