import numpy as np 

# Create |0⟩
zero = np.array(([1],[0]))
print("|0>:")
print(zero)
print("\n")

# Create Hadamard Matrix H
H = (1/np.sqrt(2))* np.array([[1,1],[1,-1]])
print("Hadamard Matrix:")
print(H)
print("\n")

# Verify H is Unitary
H_dagger = H.conj().T
result = H_dagger @ H
is_unitary = np.allclose(result,np.eye(2))
if is_unitary == True:
    print("H is a unitary matrix")
else:
    print("H is not an unitary matrix")
print("\n")

# Calculate |ψ⟩ = H|0⟩
psi = H @ zero
print("|ψ⟩ =")
print(psi)
print("\n")


# Calculate P(0), P(1)
p0= abs(psi[0,0]) ** 2
p1 = abs(psi[1,0]) ** 2

print("P(0): ",p0)
print("P(1): ",p1)

print("\n")

# Run 1000 shots
shots = 1000
measurements = np.random.choice(
    [0,1],
    size = shots,
    p = [p0,p1]
)
print("\n")

# Count 0 and 1
count0 = np.sum(measurements == 0)
count1 = np.sum(measurements == 1)
print("number of 0s:",count0)
print("number of 1s:",count1)

if count0 +  count1 == 1000:
    print("1000 shots completed")
else:
    print("1000 shots NOT completed")
print("\n")

# Calculate Experimental Probability
exp0 = count0 / shots
exp1 = count1 / shots

print("Experimental P(0): ", exp0)
print("Experimental P(1): ", exp1)
print("\n")

# Calculate Mean
mean = np.mean(measurements)
print("Experimental Mean:",mean)
print("\n")


# Calculate Variance
variance = np.var(measurements)
print("Experimental Variance: ",variance)
print("\n")