import numpy as np 

alpha = 2
beta = 1

state =  np.array([alpha,beta])
print()
print("Original State:")
print(state)

norm =  np.linalg.norm(state)
print()
print("Norm: ",norm)

if np.isclose(norm,1):
    print("state is already normalized!")
else:
    print("state is not normalized.")
    print("normalizing state...")
    print()
    state = state / norm

alpha = state[0]
beta =  state[1]
print()
print("normalized state:")
print(state)

p0 = abs(alpha) ** 2
p1 = abs(beta) ** 2
print()
print("P(0):",p0)
print("P(1):",p1)

print("P(0)+P(1):", p0+p1)
print()
if np.isclose(p0+p1,1):
    print("probabilities are valid")
else:
    print("probabilities are not valid")
print()