# Prime No. : number greater than 1 and divisible ONLY by 1 and the number itself
n = int(input())
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count+=1
if count == 2:
    print("Prime")
else:
    print("Not Prime")