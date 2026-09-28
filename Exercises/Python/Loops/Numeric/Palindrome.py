# Palindrome : is a number that remains exactly the same even when its digits are reversed
n = int(input())
og = n
rev = 0
while n>0:
    digit = n % 10 # gives us the last digit of a number
    rev = rev * 10 + digit # builds the rev num
    n = n // 10 # removes last digit from n
if og == rev:
    print("Palindrome")
else:
    print("Not Palindrome")