import matplotlib.pyplot as plt 
x = [10,20,30,40,50]
y = [1,2,3,4,5]


font1 = {'family':'serif','color':'purple','size':20}
font2 = {'family':'serif','color':'deeppink','size':10}

plt.xlabel('y*10',fontdict = font2)
plt.ylabel('y',fontdict =  font2)
plt.title("checking fonts",fontdict = font1,loc = 'right')
plt.plot(x,y,color = 'peru',linewidth = 5)

plt.grid(axis = 'y',color ='green',linestyle='--',linewidth=2)

plt.show()