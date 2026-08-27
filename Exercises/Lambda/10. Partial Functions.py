# Exercise 10: Partial Functions
# Problem Statement: Write a general multiply(x, n) function that returns x * n. Use functools.partial() to create two specialised functions from it: double(x), which always multiplies by 2, and triple(x), which always multiplies by 3. Call both with several values.
from functools import partial
def prod(x,n):
    return x*n
d = partial(prod,n=2)
t = partial(prod,n=3)
print(d(5))
print(t(5))
print(f"{d(5.2):.2f}")
print(f"{t(5.2):.2f}")