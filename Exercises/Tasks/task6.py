import pandas as pd 
import matplotlib.pyplot as plt 

# dataframe with 10 regions and 3 candidates
data = {

    "region":
    ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10'],

    "A": 
    [520,120,252,560,759,456,156,265,423,548],

    "B": 
    [745,541,854,564,256,489,451,894,566,481],

    "C": 
    [456,565,545,456,151,515,119,417,854,565]

}
df = pd.DataFrame(data)


df['total'] = df['A'] + df['B'] + df['C']


df['A%'] = df['A'] / df['total'] * 100
df['B%'] = df['B'] / df['total'] * 100
df['C%'] = df['C'] / df['total'] * 100

df['margin'] = [
    10,56,89,78,10,
    85,78,95,45,22
]


# charts

fig, (c1,c2) = plt.subplots(1,2, figsize=(12,6))

# regional chart

c1.barh(
    df['region'],
    df['A%'],
    label = 'A',
    color ='steelblue'
)

c1.barh(
    df['region'],
    df['B%'], 
    left=df['A%'],
    label = 'B',
    color = 'orange'
)

c1.barh(
    df['region'],
    df['A%'], 
    left=df['A%']+df['B%'], 
    label = 'C',
    color = 'green'
)

c1.set_title("Regional Vote Share")
c1.set_xlabel("Vote Share (%)")
c1.set_ylabel("Regions")

# national chart

c2.bar(
    ['A','B','C'],
    [df['A'].sum(),
    df['B'].sum(),
    df['C'].sum()],
    color = ['steelblue','orange','green'],
    width = 0.5
)
c2.set_title("National Votes")
c2.set_ylabel("Total Votes")
c2.set_xlabel("Candidates")

fig.legend()

plt.show()