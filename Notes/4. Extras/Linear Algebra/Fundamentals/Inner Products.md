
# Inner Products

## What is an Inner Product

An **inner product** is a mathematical operation that takes two vectors and returns a scalar (a single number). It generalizes the concept of the dot product and provides a way to measure angles, lengths, and orthogonality in vector spaces. It measures the similarity between two vectors and plays a crucial role in geometry, physics, machine learning, and numerical computations.

- An inner product is a way to multiply two vectors together to get a single number (a scalar).
- It tells us how much two vectors point in the same direction.
- If the result is zero, the vectors are perpendicular (orthogonal) to each other.
- If the result is positive, they point in a similar direction.
- If the result is negative, they point in opposite directions.

## Axioms of Inner Products

- **Rule 1 (Symmetry):** The order doesn't matter. Multiplying vector $u$ by $v$ gives the same result as multiplying $v$ by $u$.
  - $\langle u, v \rangle = \langle v, u \rangle$

- **Rule 2 (Linearity):** You can pull out constants and split up additions. If you add two vectors before multiplying, it's the same as multiplying them separately and then adding the results.
  - $\langle au + bv, w \rangle = a\langle u, w \rangle + b\langle v, w \rangle$
	**Example**
	Let's use simple 2D vectors to see how this rule works in practice.
	
	**Given:**
	- $u = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$
	- $v = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$
	- $w = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$
	- Scalars: $a = 2$ and $b = 3$
	
	We want to check if $\langle au + bv, w \rangle = a\langle u, w \rangle + b\langle v, w \rangle$.
	
	**Step 1: Calculate the Left Side $\langle au + bv, w \rangle$**
	
	First, find the combined vector $au + bv$:
	$$au = 2 \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}$$
	$$bv = 3 \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 9 \\ 12 \end{bmatrix}$$
	$$au + bv = \begin{bmatrix} 2 \\ 4 \end{bmatrix} + \begin{bmatrix} 9 \\ 12 \end{bmatrix} = \begin{bmatrix} 11 \\ 16 \end{bmatrix}$$
	
	Now, take the inner product with $w$:
	$$\langle au + bv, w \rangle = (11)(0) + (16)(1) = 0 + 16 = \mathbf{16}$$
	
	**Step 2: Calculate the Right Side $a\langle u, w \rangle + b\langle v, w \rangle$**
	
	First, find the individual inner products:
	$$\langle u, w \rangle = (1)(0) + (2)(1) = 0 + 2 = 2$$
	$$\langle v, w \rangle = (3)(0) + (4)(1) = 0 + 4 = 4$$
	
	Now, multiply by the scalars and add:
	$$a\langle u, w \rangle + b\langle v, w \rangle = 2(2) + 3(4) = 4 + 12 = \mathbf{16}$$


- **Rule 3 (Positive Length):** When you multiply a vector by itself, the result is always zero or positive. It can never be negative.
  - $\langle v, v \rangle \geq 0$

- **Rule 4 (Zero Vector):** The only time a vector multiplied by itself equals zero is if the vector itself is just zeros everywhere.
  - $\langle v, v \rangle = 0$ if and only if $v = 0$

## Why Inner Products Matter

- **Geometry**: They let us measure distances and angles in any space.
- **Optimization**: They help computers find the best solution in machine learning.
- **Physics**: They calculate work, like how much energy a force uses to move an object.
- **Signal Processing**: They check how similar two signals (like audio waves) are.
- **Quantum Mechanics**: This is the most famous use. In quantum physics, particles are treated as vectors. The inner product tells us the **probability** of a particle being in a certain state. It’s the math behind why we can’t know everything about a particle at once.

## Example

- **Example 1:** 
  - Let $u = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $v = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$.
  - Multiply corresponding parts: $(1 \times 3) + (2 \times 4)$.
  - Add them up: $3 + 8 = 11$.
  - The inner product is **11**.

- **Example 2 (Perpendicular Vectors):**
  - Let $u = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $v = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.
  - Multiply corresponding parts: $(1 \times 0) + (0 \times 1)$.
  - Add them up: $0 + 0 = 0$.
  - The inner product is **0**, which means these vectors are perpendicular.


## Difference between Dot and Inner Product

**Dot Product:** A single, fixed formula for standard vectors. It always treats every direction equally.
**Inner Product:** A flexible framework. It includes the dot product but allows for custom rules (like weights) to measure "similarity" differently.

**Example:** 
Vectors $u = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ and $v = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$

**Dot Product (Fixed Rule)**
Multiply corresponding elements and add.
$$1(3) + 2(4) = 3 + 8 = \mathbf{11}$$

**Weighted Inner Product (Custom Rule)**
Imagine the second direction is 5x more important. The rule becomes $\langle u,v \rangle = u_1v_1 + 5u_2v_2$.
$$1(3) + 5(2)(4) = 3 + 40 = \mathbf{43}$$

**Result:** The same vectors produce different results because the **Inner Product** allows us to change the "lens" through which we view them, while the **Dot Product** is just one specific lens.




