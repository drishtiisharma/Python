import matplotlib.pyplot as plt 

subs = ["math","physics","computers","chemistry","biology"]
marks = [80,76,90,78,76]

explode_vals = [0,0,0.2,0,0]
colors = ['green','blue','deeppink','khaki','orange']
legends = ['math','phtysics','computers','chemistry','biology']

plt.figure(figsize=(8,6))
# pie chart
plt.pie(
    marks, 
    labels = subs,
    autopct = "%1.1f%%",
    startangle = 270,
    explode = explode_vals,
    shadow = True,
    colors = colors
)

plt.legend(title="subjects:")
plt.savefig("piechart.png")
plt.show()