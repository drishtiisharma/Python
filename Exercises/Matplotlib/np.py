import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,10,100)
y = x**2

plt.plot(x,y,color = 'orange')
plt.xlabel("x")
plt.ylabel("x²")
plt.title("y = x²")
plt.show()