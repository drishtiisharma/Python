# Eigen Values & Eigen Vectors

A vector is an arrow with direction and length. Most vectors rotate when a matrix acts on them. An **eigenvector** is special because it never rotates. It stays on its original line. The matrix only stretches or shrinks it. Each eigenvector has its own **eigenvalue**, which is the specific number telling us how much that particular vector changed in length. Different eigenvectors can stretch by different amounts.

Mathematically: **Av = λv**

Where:

- **A** = square matrix
- **v** = eigenvector (non-zero)
- **λ** = eigenvalue (scalar)

## How to find them?

1. **Finding Eigen Values(λ**): $det(A - λI) = 0$
2. **For Eigen Vectors ($v$, for each λ)**: $(A - λI)v = 0$

## Example

[Finding Eigenvalues and Eigenvectors for a given matrix](https://i.ibb.co/DHHHB3ZJ/image.png)
