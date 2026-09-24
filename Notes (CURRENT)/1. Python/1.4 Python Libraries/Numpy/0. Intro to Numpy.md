# Introduction to Numpy

## What is NumPy?

- **NumPy** (Numerical Python) is a Python library for working with arrays and matrices
- It provides fast, efficient operations on large datasets of numbers
- Core feature: **n-dimensional array object** (called `ndarray`)
## What is it used for?

NumPy is used for performing mathematical operations like addition, multiplication, and linear algebra on entire arrays simultaneously rather than element by element. 

It enables efficient data manipulation tasks such as reshaping, slicing, and filtering large datasets without the overhead of standard Python loops. 

In scientific computing, it provides built-in functions for statistics, Fourier transforms, and random number generation.

Additionally, it serves as the foundational library for many other popular Python packages, including pandas, SciPy, and scikit-learn, which rely on its array structure for their core functionality.

## Why is NumPy Faster Than Lists?

NumPy arrays store all their data values directly next to each other in one single block of memory. In contrast, Python lists store pointers that link to data items located in various separate places in memory. Because NumPy keeps the actual values together in a continuous sequence, the computer can read and process them much faster and with less memory usage than lists.

This behavior is called <u>locality of reference</u> in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

## Why Use NumPy?

- In Python we have lists that serve the purpose of arrays, but they are **slow to process.**
- NumPy aims to provide an **array object** that is up to **50x faster** than traditional Python lists.
- The array object in NumPy is called `ndarray`, it provides a lot of supporting functions that make working with `ndarray` very easy.

> [!NOTE]
> **Additionally**: NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

# Quantum **Relevance**

## Why study it for Quantum Computing?

NumPy is essential for quantum computing because it provides the efficient data structures needed to represent and manipulate quantum systems. **Quantum states** are stored as **vectors of complex numbers**, and **quantum gates** are represented as **matrices**. 

NumPy allows us to perform the necessary linear algebra operations, such as matrix multiplication and tensor products, directly on these arrays. 

Since classical simulations of quantum circuits involve heavy numerical computations, NumPy’s optimized performance ensures these calculations run quickly. Additionally, major quantum development frameworks like Qiskit, Cirq, and PennyLane rely on NumPy internally, making it a fundamental skill for interacting with these tools and understanding the underlying mathematical operations.

## How does it help in Quantum?

NumPy helps in quantum computing by providing direct tools to implement quantum mechanics mathematically. 

We store **qubit states as NumPy arrays of complex numbers** and **apply quantum gates using matrix-vector multiplication with the `@` operator**. 

For multi-qubit systems, we combine **individual qubit states into larger state vectors using the Kronecker product function** `np.kron()`. 

NumPy natively handles complex arithmetic required for quantum amplitudes and performs these operations efficiently through vectorization, avoiding slow Python loops. 

Finally, we calculate measurement probabilities by squaring the absolute values of the state vector elements using `np.abs()**2`, completing the full cycle of quantum state manipulation and readout.

> [!NOTE]
> **Bottom line**: NumPy is the computational backbone for representing and manipulating quantum systems classically.

# More about Numpy

[[1. Dimensions]]
[[2. Array Indexing]]
[[3. Array Slicing]]
[[4. Numpy Data Types]]
[[5. Copy and View]]

