import sympy as sp 
g = 2 # number
h = 8 # result of g % p
p = 11 # divisor

# we have to find the exponent 'x'
x =  sp.discrete_log(p,h,g)
print("Discrete Logarithm:",x)

# To verify
verf =  pow(g,x,p)
if verf == h:
    print("verified!")
else:
    print("not verified...")