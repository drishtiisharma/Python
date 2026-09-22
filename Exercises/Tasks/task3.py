import numpy as np

# Set theoretical P(1) = 0.7
theoretical_p1 = 0.7

# number of shots
shot_counts = [10,100,1000,10000]

# experimental probabilities
exp_probs = []
print()
print("Theoretical P(1): ",theoretical_p1)
print()

print("Shots\tExperimental P(1)\tError")
print("-----------------------------------------------")

# running 10,100,1000,10000 shots + calculating experimental probabilities + error comparison
for shots in shot_counts:
    measurements = np.random.choice(
        [0,1],
        size = shots,
        p = [0.3,0.7]
    )
    count_1 =  np.sum(measurements)

    experimental_p1 = count_1 / shots

    error = abs(experimental_p1 - theoretical_p1)

    exp_probs.append(experimental_p1)

    print(f"{shots}\t{experimental_p1:.3f}\t\t\t{error:.3f}")

# calculating standard deviation
std_dev = np.std(exp_probs)

print()
print("experimental probabilities")
print([float(round(x, 3)) for x in exp_probs])

print()
print("standard deviation: ",std_dev)
print()
