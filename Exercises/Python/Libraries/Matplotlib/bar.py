import matplotlib.pyplot as plt 
import numpy as np 


subs = ["math","physics","computers","chemistry","biology"]
marks = [80,76,90,78,76]

plt.figure(figsize=(8,6))
# regular bar chart
plt.bar(subs,marks,color='hotpink',width = 0.5) # default bar width is 0.8; for barh-> use 'height' in place of 'width'
plt.title("Subject Marks")
plt.xlabel("subjects",color='red',size=20)
plt.ylabel("marks",color="red",size=20)
plt.show()

# horizontal bar chart
# plt.barh(subs,marks)
# plt.title("Subject Marks")
# plt.xlabel("marks")
# plt.ylabel("subjects")
# plt.show()

# histogram
m =  np.random.normal(100,10,100) # mean,standard deviation, number of values
plt.hist(m,ec='black',bins=5,linewidth=2)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
