from scipy.integrate import quad

def f(x):
    return x**2

res,err = quad(f,0,2)

print(res)
print(err)