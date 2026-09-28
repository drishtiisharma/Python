a = 17
b = 8
n = 5
print(f"{a} mod {b} is:",a%b)

# modular addition
add = (a+b) % n
print("Addition:", add)

# modular multiplication
prod = (a*b) % n
print("Multiplication:", prod)

# modular exponentiation
print("modular exp:",pow(a,b,n))