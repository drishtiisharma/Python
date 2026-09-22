import numpy as np 
import matplotlib.pyplot as plt 

days = np.arange(1,366)


base_temp = 25
seasonal_temp = 10 * np.sin(2 *  np.pi * days/365) # multiplying by 10 for seasonal variation

# 3 years
year1 = base_temp + seasonal_temp + np.random.normal(0,2,365)
year2 = base_temp + seasonal_temp + np.random.normal(0,2,365)
year3 = base_temp + seasonal_temp + np.random.normal(0,2,365)


temps = np.array([year1,year2,year3])

min_temp = temps.min(axis=0)
max_temp = temps.max(axis=0)

month = np.repeat(
    np.arange(1,13),
    [31,28,31,30,31,30,31,31,30,31,30,31]
)

summer = (month >= 6) & (month <= 8)

# graph

fig, (c1,c2) = plt.subplots(1,2,figsize=(14,6))

# yearly temp patterns for 3 years

c1.fill_between(days, min_temp, max_temp, alpha = 0.2)

c1.plot(days, year1, label='Year 1',color='green')
c1.plot(days, year2, label='Year 2',color='deeppink')
c1.plot(days, year3, label='Year 3',color='steelblue')

c1.set_title("Temperature Patterns")
c1.set_xlabel("Day of Year")
c1.set_ylabel("Temperature")
c1.legend()


# summer temp patterns for 3 years
c2.plot(days[summer], year1[summer], label='Year 1', color='green')
c2.plot(days[summer], year2[summer], label='Year 2', color='deeppink')
c2.plot(days[summer], year3[summer], label='Year 3', color='steelblue')

c2.set_title("Summer (June-August)")
c2.set_xlabel("Day of Year")
c2.set_ylabel("Temperature")
c2.legend()

plt.suptitle("Seasonal Temperature Patterns")
plt.savefig("seasonal_temp_patterns.png")
plt.show()