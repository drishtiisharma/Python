import matplotlib.pyplot as plt
import numpy as np 

x = [10,20,30,40,50]
y = [1,2,3,4,5]

a = [52,65,74,82,75]
b = [10,20,30,40,50]

# scatter plot
plt.scatter(x,y,linewidth = 3, color = 'steelblue', marker = 'o',label = 'something')

plt.scatter(a,b,linewidth = 3, color = 'deeppink', marker = 'x',label = 'something')
plt.show()

m = np.array([23,45,56,89])
n = np.array([12,45,78,16])
colors = np.array(['green','deeppink','black','blue'])
plt.scatter(m,n,c=colors)
plt.show()