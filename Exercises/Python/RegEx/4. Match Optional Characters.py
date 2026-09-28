# match a string that has an a followed by zero or one b (i.e., exactly a or ab, nothing else).
import re
x = input()
if re.fullmatch(r"ab?",x):
    print("0 or 1 occurence of b")
else:
    print("more than 1 occurence of b or pattern not matched")