from scipy.integrate import dblquad

def f(y, x):
    return x**2

res = dblquad(
    f,
    0, 1,
    lambda x: 0,
    lambda x: 1
)

print(res)