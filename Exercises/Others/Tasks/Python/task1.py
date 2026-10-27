import numpy as np
import pandas as pd

# Task 1: Define a gain scalar k = 2.5.
k = 2.5

# Task 2: Create a signal vector v (length 5) and scale it: v_scaled = k * v.
v = np.array([10,20,30,40,50])
v_scaled = v*k


#Task 3: Build a 5×5 "system" matrix A (random values) representing the transformation the signal passes through, and store it in a DataFrame with labeled rows/columns.
A = np.random.rand(5,5)
df = pd.DataFrame(
    A,
    index=[f"row_{i}" for i in range(5)],columns=[f"col_{i}" for i in range(5)]
)
print(df)

# Task 4: Apply the system: output = Matrix Multiplication between A and v_scaled.
output = A.dot(v_scaled)


# Task 5: Compute Determinant. If it's 0 (or near-zero), regenerate A — explain why a singular system matrix would be a problem here.
det_A =np.linalg.det(A)

if np.isclose(det_A,0):

    while True:
        A = np.random.rand(5,5)
        det_A = np.linalg.det(A)
        if not np.isclose(det_A,0):
            break

    df = pd.DataFrame(
    A,
    index=[f"row_{i}" for i in range(5)],
    columns=[f"col_{i}" for i in range(5)]
    )

else:
    pass
        

# Task 6: Compute eigenvalues/eigenvectors of A. Identify the eigenvector with the largest eigenvalue — this is the "dominant mode" the system amplifies most.
eigenvalues, eigenvectors = np.linalg.eig(A)

dominant_idx = np.argmax(np.abs(eigenvalues))

dominant_eigenvalue = eigenvalues[dominant_idx]
dominant_eigenvector = eigenvectors[:,dominant_idx]


# Task 7: Create a second small vector channel = [1, 0] representing a 2-channel system, and combine it with v via Tensor Products to build a 10-dim joint signal.
channel = np.array([1,0])
joint_signal = np.kron(channel,v)


# Task 8: Verify vector norm via the complex conjugate identity — build a complex version of v inline (e.g. v_complex = v + 0.1j, or reuse v cast as complex) and confirm sqrt(v_complex.conj() @ v_complex) matches np.linalg.norm(v_complex)
v_complex = np.array([10+1.0j, 20+2.0j, 30+3.0j, 40+4.0j, 50+5.0j])

conjugate_prod = v_complex.conjugate() @ v_complex

v_complex_norm_via_conjugate = np.sqrt(conjugate_prod)
v_complex_norm_builtin = np.linalg.norm(v_complex)

norms_match = np.isclose(v_complex_norm_via_conjugate,v_complex_norm_builtin)


# Task 9: Log every intermediate result (v, v_scaled, output, Computed Determinant, dominant eigenvalue, v_complex_norm_via_conjugate, v_complex_norm_builtin,norm_match(True/False)) into one summary DataFrame.


summary_data = {
    'Metric': [
        'Original Vector (v)', 
        'Scaled Vector (v_scaled)', 
        'System Output', 
        'Determinant of A', 
        'Dominant Eigenvalue', 
        'Norm (Manual Conjugate)', 
        'Norm (NumPy Built-in)', 
        'Norms Match?'
    ],
    'Value': [
        v.tolist(),              
        v_scaled.tolist(),        
        output.tolist(),         
        det_A,                   
        dominant_eigenvalue,     
        v_complex_norm_via_conjugate,             
        v_complex_norm_builtin,             
        norms_match             
    ]
}

summary_df = pd.DataFrame(summary_data)
print(summary_df.to_string(index=False))