# Tensor

A [Tensor](https://i.ibb.co/TBxwJzw8/image.png) is a **N-dimensional Matrix**:

- A Scalar is a 0-dimensional tensor
- A Vector is a 1-dimensional tensor
- A Matrix is a 2-dimensional tensor

A **Tensor** is a generalization of **Vectors** and **Matrices** to higher dimensions.

## Tensor Ranks

The number of directions a tensor can have in a **N**-dimensional space, is called the **Rank** of the tensor.

The rank is denoted **R**.

A **Scalar** is a single number.

- It has 0 Axes
- It has a **Rank of 0**
- It is a 0-dimensional Tensor

A **Vector** is an array of numbers.

- It has 1 Axis
- It has a **Rank of 1**
- It is a 1-dimensional Tensor

A **Matrix** is a 2-dimensional array.

- It has 2 Axis
- It has a **Rank of 2**
- It is a 2-dimensional Tensor
## Real Tensors

Technically, all of the above are tensors, but when we speak of [tensors](https://www.statisticshowto.com/wp-content/uploads/2020/02/tensor-cube.png), we generally speak of matrices with a dimension larger than 2 (**R > 2**).

Here is the breakdown of the simplest real [tensor](https://www.statisticshowto.com/wp-content/uploads/2020/02/tensor-cube.png)

This image illustrates the **Cauchy stress tensor**, a classic example of a real-world rank-2 tensor used in continuum mechanics and physics. The cube represents an infinitesimal volume element within a material, and the nine symbols ($\sigma_{ij}$) represent the components of the stress tensor acting on its faces.

*   **The Faces:** Each face of the cube corresponds to a specific direction (axis). For example, the yellow face is perpendicular to the x-axis (direction $\mathbf{e}_1$), the red face to the y-axis ($\mathbf{e}_2$), and the orange face to the z-axis ($\mathbf{e}_3$).
*   **The Vectors ($\mathbf{T}^{(\mathbf{e})}$):** The blue arrows labeled $\mathbf{T}^{(\mathbf{e}_1)}$, $\mathbf{T}^{(\mathbf{e}_2)}$, etc., are **traction vectors**. They represent the total force per unit area acting on that specific face.
*   **The Components ($\sigma_{ij}$):** Each traction vector is decomposed into three components (the black arrows):
    *   **Normal Stress ($\sigma_{11}, \sigma_{22}, \sigma_{33}$):** These act perpendicular to the face (pulling or pushing directly into/out of the surface).
    *   **Shear Stress ($\sigma_{12}, \sigma_{13}, \dots$):** These act parallel to the face (sliding forces).

**Why is this a Tensor?**
It perfectly fits the definition because it maps a **direction** (the normal vector of a face, like $\mathbf{e}_1$) to a **force vector** (the traction $\mathbf{T}$). We cannot describe this physical state with just a scalar (magnitude) or a single vector; we need a $3\times3$ matrix (a rank-2 tensor) to fully capture how forces are transmitted through the material in all directions simultaneously.

<u>**Role of these components**</u>

1.  **The Faces ($\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$):** These define the specific plane being analyzed. Each face corresponds to one axis of the coordinate system and serves as the reference surface upon which forces are measured.
2.  **The Traction Vectors ($\mathbf{T}$):** These represent the total force per unit area acting on a given face. They are the vector sum of all stress components acting on that specific surface.
3.  **Normal Stress Components ($\sigma_{11}, \sigma_{22}, \sigma_{33}$):** These measure the magnitude of force acting perpendicular to the face. Their indices match (e.g., $\sigma_{11}$ acts on the x-face in the x-direction), indicating alignment with the surface normal.
4.  **Shear Stress Components ($\sigma_{ij}$ where $i \neq j$):** These measure the magnitude of force acting parallel to the face. Their indices differ (e.g., $\sigma_{12}$ acts on the x-face in the y-direction), indicating the force is orthogonal to the surface normal.

## What is a Tensor Index?

A tensor index is simply a label that tells us exactly which number in a multi-dimensional array we are referring to.

In [this specific diagram](https://www.statisticshowto.com/wp-content/uploads/2020/02/tensor-cube.png), the labels follow this rule:
**$\sigma_{ij}$ = The force component pointing in direction $j$, acting on the face perpendicular to axis $i$.**

This means for *this specific diagram*:
-   The **second index ($j$)** tells you **which face** the arrow is drawn on.
    -   $j=1$ → Red Face
    -   $j=2$ → Yellow Face
    -   $j=3$ → Orange Face
-   The **first index ($i$)** tells you **which direction** the arrow points.
    -   $i=1$ → Points Left/Right (Red-direction)
    -   $i=2$ → Points Front/Back (Yellow-direction)
    -   $i=3$ → Points Up/Down (Orange-direction)


## Tensor Operations

### 1. Addition and Scalar Multiplication
These operations do not change the rank or shape of the tensor. They are performed element-by-element.

**Example:**
Let $A$ and $B$ be two rank-2 tensors (matrices):
$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$

*   **Addition:** Add corresponding components.
    $$C_{ij} = A_{ij} + B_{ij} \implies C = \begin{bmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}$$
*   **Scalar Multiplication:** Multiply every component by a scalar $k=3$.
    $$D_{ij} = 3 \cdot A_{ij} \implies D = \begin{bmatrix} 3 & 6 \\ 9 & 12 \end{bmatrix}$$

### 2. Tensor Product ($\otimes$)

The tensor product combines two tensors into a new, higher-rank tensor. The new rank is the sum of the original ranks. We multiply every component of the first tensor by every component of the second tensor.

> **Tensor rank = the number of axes/indices needed to describe the tensor.**

We can loosely think of it as the number of **directions/dimensions of organization**.

For example:

- **Scalar** → rank 0 → just one value
    
- **Vector** → rank 1 → one axis
    
- **Matrix** → rank 2 → two axes (rows, columns)
    
- **3D tensor** → rank 3 → three axes
    
- **4D tensor** → rank 4 → four axes

$$rank(A⊗B)=rank(A)+rank(B)​$$

where here **rank means tensor order/number of axes**, not matrix rank.

**Examples:**
###### Rank - 1 Tensor
Take a vector $u$ (rank-1, size 2) and a vector $v$ (rank-1, size 2):
$$u = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad v = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$$

The tensor product $T = u \otimes v$ creates a rank-2 tensor (matrix). The component $T_{ij}$ is calculated as $u_i \times v_j$:

*   $T_{11} = u_1 \times v_1 = 1 \times 3 = 3$
*   $T_{12} = u_1 \times v_2 = 1 \times 4 = 4$
*   $T_{21} = u_2 \times v_1 = 2 \times 3 = 6$
*   $T_{22} = u_2 \times v_2 = 2 \times 4 = 8$

So,

$$
u \otimes v =
\begin{bmatrix}
1 \\
2
\end{bmatrix}
\otimes
\begin{bmatrix}
3 \\
4
\end{bmatrix}
=
\begin{bmatrix}
3 & 4 \\
6 & 8
\end{bmatrix}
$$


**Result:** Two rank-1 tensors produced one rank-2 tensor.

###### Rank - 2 Tensor
Let $A$ and $B$ be two rank-2 tensors with shape $(2, 2)$:

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
$$

The tensor product $C = A \otimes B$ produces a new tensor with rank $2 + 2 = 4$. Since each input has dimensions $(2, 2)$, the output will have dimensions $(2 \times 2, 2 \times 2) = (4, 4)$.

The component formula is:
$$C_{(i,k),(j,l)} = A_{ij} \cdot B_{kl}$$

This means every single element in $A$ is multiplied by the entire matrix $B$, and the results are arranged in a block structure.


**Block (1,1):** Multiply $A_{11}=1$ by all of $B$
$$1 \cdot \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$$

**Block (1,2):** Multiply $A_{12}=2$ by all of $B$
$$2 \cdot \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 10 & 12 \\ 14 & 16 \end{bmatrix}$$

**Block (2,1):** Multiply $A_{21}=3$ by all of $B$
$$3 \cdot \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 15 & 18 \\ 21 & 24 \end{bmatrix}$$

**Block (2,2):** Multiply $A_{22}=4$ by all of $B$
$$4 \cdot \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 20 & 24 \\ 28 & 32 \end{bmatrix}$$

Assemble the four blocks into the final $4 \times 4$ rank-4 tensor:

$$
A \otimes B = \begin{bmatrix}
5 & 6 & | & 10 & 12 \\
7 & 8 & | & 14 & 16 \\
\hline
15 & 18 & | & 20 & 24 \\
21 & 24 & | & 28 & 32
\end{bmatrix}
$$
**Result:** Two rank-2 tensors produced one rank-4 tensor.

> [!NOTE]
> When we take the tensor product of two matrices, the result is a complex 4D object. Since we can't easily draw or calculate with 4D objects on paper, we use the **Kronecker Product** to arrange that 4D object into a big, simple **2D Matrix**, the above example is a **Kronecker Product representation**.

### 3. Contraction

Contraction **reduces the rank of a tensor by 2.** It works by setting one upper index equal to one lower index and summing over all possible values of that index. This is equivalent to taking the trace for matrices.

**Example:**

###### Rank - 2 Tensor (2x2 Matrix)
Take a rank-2 mixed tensor $M^i_j$ (one upper, one lower index), represented as a 2×2 matrix:
$$M = \begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix} \quad \text{(where rows are } i \text{ and columns are } j)$$

To contract $M$, we set $i = j$ and sum:
$$\text{Contraction} = \sum_{i=1}^{2} M^i_i = M^1_1 + M^2_2$$
$$= 2 + 3 = 5$$

**Result:** A rank-2 tensor became a rank-0 tensor (scalar).

###### Rank - 2 Tensor (3x3 Matrix):


Take a rank-2 mixed tensor $T^i_j$ (1 upper, 1 lower index), represented as a 3×3 matrix:

$$T = \begin{pmatrix} 
T^1_1 & T^1_2 & T^1_3 \\
T^2_1 & T^2_2 & T^2_3 \\
T^3_1 & T^3_2 & T^3_3 
\end{pmatrix}$$
**Contraction:**
Set $i = j$ and sum over all values:

$$C = \sum_{i=1}^{3} T^i_i = T^1_1 + T^2_2 + T^3_3$$

Let's say our matrix is:
$$T = \begin{pmatrix} 
5 & 2 & 7 \\
3 & 8 & 1 \\
4 & 6 & 9 
\end{pmatrix}$$

Then:

$$C = T^1_1 + T^2_2 + T^3_3 = 5 + 8 + 9 = 22$$

### 4. Raising and Lowering Indices

This operation changes an index from upper (contravariant) to lower (covariant), or vice versa. It requires a **metric tensor** ($g$), which defines distances and angles in the space. We cannot raise or lower indices without a metric.

**The Rule:**
*   **Lowering:** Multiply the tensor by the metric $g_{ij}$ and sum over the shared index.
*   **Raising:** Multiply the tensor by the inverse metric $g^{ij}$ and sum over the shared index.

**Example Calculation:**
###### Lowering Indice

Let the metric tensor be non-identity:

$$
g_{ij} =
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
$$

Let a contravariant vector (upper index) be:

$$
v^j =
\begin{bmatrix}
5 \\
7
\end{bmatrix}
$$

To lower the index and find $v_i$, we calculate:

$$
v_i = \sum_j g_{ij}v^j
$$

- For $i=1$:

$$
v_1 = g_{11}v^1 + g_{12}v^2
= (2)(5) + (0)(7)
= 10
$$

- For $i=2$:

$$
v_2 = g_{21}v^1 + g_{22}v^2
= (0)(5) + (3)(7)
= 21
$$

Therefore:

$$
v_i =
\begin{bmatrix}
10 \\
21
\end{bmatrix}
$$


###### Raising Indice

Let the metric tensor be:

$$
g_{ij} =
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
$$

First, find the inverse metric $g^{ij}$:

$$
g^{ij} =
\begin{bmatrix}
\frac{1}{2} & 0 \\
0 & \frac{1}{3}
\end{bmatrix}
$$

Let a covariant vector (lower index) be:

$$
v_j =
\begin{bmatrix}
10 \\
21
\end{bmatrix}
$$

To raise the index and find $v^i$, we calculate:

$$
v^i = \sum_j g^{ij}v_j
$$

- For $i=1$:

$$
v^1 = g^{11}v_1 + g^{12}v_2
= \left(\frac{1}{2}\right)(10) + (0)(21)
= 5
$$

- For $i=2$:

$$
v^2 = g^{21}v_1 + g^{22}v_2
= (0)(10) + \left(\frac{1}{3}\right)(21)
= 7
$$

Therefore:

$$
v^i =
\begin{bmatrix}
5 \\
7
\end{bmatrix}
$$


## Difference between Tensor & Array

| Tensor                                                                                                        | Matrix                                                                                            |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| A multi-dimensional array with any number of dimensions (rank ≥ 0)                                            | A two-dimensional array (rank = 2)                                                                |
| Can represent scalars (0D), vectors (1D), matrices (2D), and higher-dimensional data                          | Specifically represents a 2D grid of numbers with rows and columns                                |
| Generalization of matrices to n-dimensions                                                                    | A special case of a tensor (2nd-order tensor)                                                     |
| Used extensively in deep learning frameworks (e.g., TensorFlow, PyTorch) for handling complex data structures | Commonly used in linear algebra for operations like transformations, solving systems of equations |
| Operations include element-wise, broadcasting, and dimension-specific manipulations across multiple axes      | Operations include matrix multiplication, determinant, inverse, eigenvalue decomposition          |

