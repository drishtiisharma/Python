# Statistics for Quantum Measurement

When a quantum circuit is measured repeatedly, we do **not** directly get the exact probability of each outcome. We get a set of **measurement results (shots)** and use statistics to estimate the underlying probabilities.

For example, suppose a qubit is measured 1,000 times:

- `0` occurs 620 times
- `1` occurs 380 times

We estimate:

$P(0)≈6201000=0.62P(0) \approx \frac{620}{1000}=0.62$
$P(1)≈3801000=0.38P(1) \approx \frac{380}{1000}=0.38$


But the true probabilities could be slightly different. This is where **confidence intervals** and **sampling statistics** are useful.

## Shots

A **shot** is one execution of a quantum circuit followed by measurement.

If we run a circuit 1,000 times:

$Number of shots=1000$

Suppose the results are:

```
0 → 620 times
1 → 380 times
```

Then the observed frequencies are:

$\hat{p}_0=\frac{620}{1000}=0.62$
$\hat{p}_1=\frac{380}{1000}=0.38$

Here, $\hat{p}$ means **estimated probability**.

## Why don't we get the exact probability?

In quantum measurement, the probability of an outcome does not mean that we will get that exact percentage in every set of measurements. For example, if the true probability of measuring `0` is 60%, measuring the qubit 10 times might give 7 zeros and 3 ones, so the observed probability of `0` is 70%. If we increase the number of measurements to 1,000, we might get 614 zeros and 386 ones, giving an observed probability of 61.4%.

**And why is that?**

When we increase the number of shots, we perform the quantum measurement more times, so the calculated probability becomes more reliable. The result can still vary, but the variation usually becomes smaller as the number of shots increases. Therefore, shots are used to **estimate** the actual quantum probability, not to directly give its exact value.


## Sampling Error

The difference between the observed proportion and the true probability is called **sampling error**.

For example, suppose:
$$
P(0)=0.60
$$
but after 1,000 shots:
$$
\hat{p}_0=0.62
$$
Then:

$$Sampling error=0.62−0.60=0.02$$

So the observed result is 2 percentage points away from the true probability.

We usually **do not know the true probability**, so statistics helps us quantify how uncertain our estimate is.

## Confidence Interval

A **confidence interval** gives a range of plausible values for the underlying probability based on the observed measurements.

Suppose:

```
Shots = 1000
Number of 0s = 620
```

Therefore:

$\hat{p}=\frac{620}{1000}=0.62$

For a large number of shots, an approximate 95% confidence interval for a proportion is:

$\hat{p}\pm1.96\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$

where:

- $\hat{p}$ = observed probability
- $n$ = number of shots
- $1.96$ = approximate 95% confidence coefficient

**Example**

Given:

$\hat{p}=0.62$
$n=1000$


Standard error:

$SE = \sqrt{\frac{0.62(1-0.62)}{1000}}$
$SE\approx0.0153$

Therefore:


95 % CI = 0.62 ± 1.96(0.0153)
95 % CI ≈ 0.62 ± 0.030


**Calculate the margin of error**

For an approximate **95% confidence interval**, we use:  $1.96×SE$

So:  $1.96×0.0153≈0.030$

This means our estimated probability has an uncertainty of about **±0.030**.

**Create the range**

Our estimated probability was:  0.62

Subtract the uncertainty:  0.62 − 0.030 = **0.590**

Add the uncertainty: 0.62 + 0.030 = **0.650**

Therefore: $$\boxed{0.590\leq p\leq0.650}$$
So the range **0.590–0.650** is simply:

$\boxed{\text{estimate}\pm\text{margin of error}}$

or: $\boxed{0.62±0.030}$​

The estimated probability is therefore: $\boxed{P(0)\approx0.62}$

with an approximate 95% confidence interval of: $$\boxed{[0.590,0.650]}$$
```python
import numpy as np 
shots = 1000
successes = 620
p = successes/shots
se = np.sqrt(p*(1-p)/shots)

lower = p - 1.96 * se
upper = p + 1.96 * se

print("estimated probability:",p)
print(f"95% confidence interval: {lower:.2f} {upper:.2f}")
```

## Why factoring is hard classically

**Factoring** means taking a large integer and finding the prime numbers that multiply together to produce it.

For example:

15=3×5

Here, factoring is easy because the number is small.

But consider a much larger number:

N=12345678912345678989592229584262

The problem is to find its prime factors.

The main issue is that there is **no known efficient classical algorithm** that can factor arbitrary large integers in polynomial time.

A simple classical approach is to try possible divisors:

```
2
3
4
5
6
7
...
```

For a large number, there can be an enormous number of possibilities to check.

For example, if:

N=p×q

where $p$ and $q$ are large prime numbers, knowing $N$ does not directly tell us what $p$ and $q$ are.

We can multiply:

p×q=N

quickly if we already know $p$ and $q$.

But going in the opposite direction:

N→p,q

is computationally difficult for sufficiently large numbers.

**Why is this important for cryptography?**

This difficulty is used by **RSA cryptography**.

**RSA (Rivest–Shamir–Adleman)** is a widely used public-key encryption algorithm that secures data transmitted over the internet.

RSA uses two mathematically linked keys: 

- public key to lock (encrypt) data; anyone can use this shared key to scramble a message into unreadable code.
- private key to unlock (decrypt) it; only the intended receiver keeps this secret key, which is the only tool capable of unscrambling the code.

Prime Numbers: The security relies on the extreme difficulty of factoring the product of two very large prime numbers

N=pq

where $p$ and $q$ are large primes.

The public key contains $N$, but finding the original $p$ and $q$ from $N$ is believed to be computationally difficult for classical computers when the numbers are sufficiently large.

Therefore:

**Factoring a sufficiently large product is hard for known classical algorithms.**

### Quantum connection

This is important because **Shor's algorithm** provides a quantum algorithm that can factor integers efficiently in theory.

So the basic idea is:

Classical computer→large integer factoring is computationally difficult

while:

Quantum computer + Shor’s algorithm→factoring can be done efficiently in theory

This is one of the major reasons quantum computing is important for **cryptography**.