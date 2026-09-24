import numpy as np 
from scipy import linalg 

A = np.array([
    [4,7],
    [2,6]
])
b = np.array([5,6])
print("determinant: ",linalg.det(A))
print("inverse: ",linalg.inv(A))
print("eqn: ",linalg.solve(A,b))
print("eigen values:",linalg.eigvals(A))

U, S, Vt = linalg.svd(A)

print("U:",U) # directions
print('S:',S) # singular values that tell us how important/scaled those directions are
print('Vt:',Vt) # describes another set of dirtections