import numpy as np 

zero = np.array(([1],[0]))

print("|0>:")
print(zero)


H = (1/np.sqrt(2))* np.array([[1,1],[1,-1]])
print("Hadamard Matrix:")
print(H)

H_dagger = H.conj().T
result = H_dagger @ H


is_unitary = np.allclose(result,np.eye(2))
if is_unitary == True:
    print("H is a unitary matrix")
else:
    print("H is not an unitary matrix")