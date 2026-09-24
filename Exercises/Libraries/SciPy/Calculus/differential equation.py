from scipy.integrate import solve_ivp

def f(t, y):
    return y

solution = solve_ivp(
    f,
    [0, 5],
    [1]
)

print(solution.y)