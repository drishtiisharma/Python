import matplotlib.pyplot as plt 
import numpy as np 

# data
labels = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 5, 2, 4]


angles = np.linspace(
    0,
    2 * np.pi,
    len(labels),
    endpoint = False
)

values += values[:1]
angles = np.append(angles, angles[0])

plt.polar(angles,values)
plt.fill(angles,values,alpha=0.2,color='deeppink')

plt.xticks(angles[:-1],labels)
plt.show()