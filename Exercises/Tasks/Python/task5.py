import sympy as sp 

a = 17
b = 5
n = 23

print()
print(f"{a} is prime: ", sp.isprime(a))
print(f"{b} is prime: ", sp.isprime(b))
print()

print(f"gcd of {a} and {b}: ",sp.gcd(a,b))
print()
print(f"{a} % {b}: ",a%b)
print()
print(f"{a}^{b} % {n}: ",pow(a,b,n))

print()
if sp.gcd(a,n) == 1:
    inverse = sp.mod_inverse(a,n)
    print("inverse: ",inverse)

    print(f"({a} * inverse) % n:",(a*inverse)%n)
else:
    print("modular inverse does not exist")

print()