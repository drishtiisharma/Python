# Bayes' Theorem

Bayes' Theorem is a mathematical formula used to determine the conditional probability of an event based on prior knowledge and new evidence.

It adjusts probabilities when new information comes in and helps make better decisions in uncertain situations.

#### Formula
$$ P(A \mid B) = \frac{P(B \mid A)\cdot P(A)}{P(B)} $$
where:
- **P(A)** i.e. prior probability (before seeing B) and **P(B)** i.e. marginal likelihood are the probabilities of events A and B; also, P(B) is never equal to zero.
- **P(A|B)** is the probability of event A when event B happens i.e. posterior probability (after seeing B)
- **P(B|A)** is the probability of event B when A happens i.e. likelihood (probability of B given A)

## Quantum Relevance

1. **State Estimation**: Updates the probability distribution of a quantum state (posterior) based on noisy measurement outcomes (likelihood) and prior knowledge.
2. **Error Correction**: Infers the most likely error syndrome in fault-tolerant computing by combining real-time measurement data with known noise models.

# Random Variables

A **random variable** is simply a variable that represents the **numerical outcome of a random experiment**.

**Example: Rolling a die**

Possible outcomes:

```
1, 2, 3, 4, 5, 6
```

We can call the result `X`.

So:

```
X = result of the die roll
```

If we roll a 4:

```
X = 4
```

### Discrete Random Variable

A variable that can take **separate/countable values**.

Examples:

- Dice → 1, 2, 3, 4, 5, 6
- Number of heads → 0, 1, 2, 3...
- Number of photons detected → 0, 1, 2...

It uses a **PMF (Probability Mass Function)**:

$P(X=x)$

which means:

> Probability that X has the value x.

### Continuous Random Variable

A variable that can take **any value within a range**.

Examples:

- Temperature
- Time
- Height
- Measurement error

It uses a **PDF (Probability Density Function)**:

$$f(x)$$

## Quantum Relevance

Represents the **result of a quantum measurement**. For example, measuring a qubit can give `0` or `1`, so the measurement result can be treated as a random variable.
# Expected Value

Expected value basically means:

> **The average value we expect if we repeat the experiment many times.**

### Fair die

Every number has probability:

$P(X=x)=\frac{1}{6}$


Therefore:
$$
E[X] = 1\left(\frac16\right)+ 2\left(\frac16\right)+ 3\left(\frac16\right)+ 4\left(\frac16\right)+ 5\left(\frac16\right)+ 6\left(\frac16\right)
$$
which gives:
$$ E[X]=3.5$$

It means that over many rolls, the **average result approaches 3.5**.

## Quantum Relevance

Gives the **average value of a quantum measurement** over many repeated measurements. In quantum mechanics, this is closely related to the **expectation value of an observable**.
# Variance

Expected value tells us the **center/average**.

Variance tells us:
> **How spread out the values are around the average.**

$$Var(X)=E[(X−E[X])^2]$$

Another useful form is:

$$Var(X)=E[X2]−(E[X])2Var(X)=E[X^2]-(E[X])^2$$

For the die:

$$E[X]=3.5$$

and

$$E[X2]=1+4+9+16+25+366=916$$
$$E[X^2]=\frac{1+4+9+16+25+36}{6} =\frac{91}{6}$$

Therefore:

$$Var(X)=916−(3.5)2$$$$Var(X)=\frac{91}{6}-(3.5)^2 Var(X)=1235​≈2.92$$
## Quantum Relevance

Measures the **spread/uncertainty of quantum measurement results** around their expected value. It is used to quantify measurement uncertainty.

# Probability Distribution

A **probability distribution** tells us:

>**What outcomes are possible and how likely each one is.**

For example, a fair die:

|Result|Probability|
|---|---|
|1|1/6|
|2|1/6|
|3|1/6|
|4|1/6|
|5|1/6|
|6|1/6|

That's a probability distribution.

There are different types of distributions depending on the type of random variable.

## Quantum Relevance

Describes the **probability of obtaining each measurement outcome** when a quantum system is measured.

# Binomial Distribution

Binomial distribution is used when you have:

- A fixed number of trials
- Each trial has **two outcomes** (success/failure)
- Same probability of success each time
- Trials are independent

Example:

**10 coin flips**

Each flip:

```
Heads → success
Tails → failure
```

Probability of heads:

p=0.5

Probability of getting exactly `k` successes:
$$P(X=k)= \binom{n}{k}p^k(1-p)^{n-k}$$

For exactly 7 heads in 10 flips:
$$P(X=7)= \binom{10}{7}(0.5)^7(0.5)^3$$

Since:

$$(0.5)^7(0.5)^3=(0.5)^{10}$$

we get:
$$P(X=7)= 120(0.5)^{10} $$$$P(X=7)≈0.117$$

So there is about an **11.7% probability** of getting exactly 7 heads.

## Quantum Relevance

Useful when repeatedly measuring a **two-outcome quantum system**, such as a qubit giving `0` or `1`, and asking how many times one outcome occurs.

# Normal Distribution

The normal distribution is the familiar **bell-shaped curve**.

It is described by:

- Mean → $\mu$
- Standard deviation → $\sigma$

Its PDF is:
$$f(x)= \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

$\mu$ = center

Where the distribution is centered.

$\sigma$ = spread

How widely the values are distributed.

For example:

```
small σ → values tightly clustered
large σ → values more spread out
```


## Quantum Relevance

Useful for understanding **measurement noise, experimental errors, and statistical fluctuations** in quantum experiments. It can also approximate distributions obtained from many repeated measurements under suitable conditions.