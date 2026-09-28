import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([10,20,30])
y = np.array([40,50,60])

plt.figure(figsize=(8,6))
 
# total_rows, total_cols, position
# graph 1
plt.subplot(2,2,1)
plt.plot(x,y,color ='deeppink')

# graph 2
plt.subplot(2,2,2)
plt.scatter(x,y,color='darkkhaki')

# graph 3
plt.subplot(2,2,3)
plt.barh(x,y,color ='lime')

# graph 4
plt.subplot(2,2,4)
plt.bar(x,y,color='tomato')

plt.suptitle("Subplots")

plt.show()