import numpy as np 
shots = 1000
successes = 620
p = successes/shots
se = np.sqrt(p*(1-p)/shots)

lower = p - 1.96 * se
upper = p + 1.96 * se

print("estimated probability:",p)
print(f"95% confidence interval: {lower:.2f} {upper:.2f}")