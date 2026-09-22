import matplotlib.pyplot as plt 
x = [10,20,30,40,50]
y = [1,2,3,4,5]
plt.plot(x,y) # creates the line
plt.title("A Simple Graph") # must come before show()
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.plot(x,y,linestyle='--',linewidth = 3, color = 'hotpink', marker = 'o',label = 'something')

plt.grid() # adds grid
plt.legend() 
plt.show() # displays the graph
 # width, height
plt.figure(figsize=(8, 5))
plt.plot(x,y,'o:r',ms=10,mec = 'green',mfc='steelblue')
plt.show()