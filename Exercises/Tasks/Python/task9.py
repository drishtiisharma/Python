import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ratings out of 10
data = {
    'price': [9, 5, 8, 7],
    'quality': [7, 9, 4, 6],
    'speed': [9, 7, 6, 8],
    'design': [7, 8, 6, 4],
    'battery': [8, 7, 4, 5],
    'support': [4, 5, 8, 3],
    'features': [9, 8, 2, 4]
}

df = pd.DataFrame(
    data,
    index=['A', 'B', 'C', 'D']
)

# print(df)

attributes = df.columns
values = df.values


# radar chart
angles = np.linspace(
    0,
    2 * np.pi,
    len(attributes),
    endpoint=False
)

angles = np.concatenate(
    (
        angles,
        [angles[0]]
    )
)

fig = plt.figure(figsize=(14, 7))

c1 = fig.add_subplot(1, 2, 1, polar=True)
c2 = fig.add_subplot(1, 2, 2)

colors = ['green', 'deeppink', 'steelblue', 'darkkhaki']

for i in range(4):

    data_values = np.concatenate(
        (
            values[i],
            [values[i][0]]
        )
    )

    c1.plot(
        angles,
        data_values,
        color=colors[i],
        label=df.index[i]
    )

    c1.fill(
        angles,
        data_values,
        color=colors[i],
        alpha=0.5
    )

c1.set_xticks(angles[:-1])
c1.set_xticklabels(attributes)

c1.set_ylim(0, 10)
c1.set_title("Product Comparison")
c1.legend()


# heatmap
c2.imshow(df.values, aspect='auto')

c2.set_xticks(range(7))
c2.set_xticklabels(attributes, rotation=45)

c2.set_yticks(range(4))
c2.set_yticklabels(df.index)


for i in range(4):
    for j in range(7):
        c2.text(
            j,
            i,
            df.iloc[i, j],
            ha='center',
            va='center'
        )

c2.set_title("Heatmap")

# super title
plt.suptitle(
    "Comparison of 4 Products across 7 Attributes",
    fontsize=16
)

# source footnote
fig.text(
    0.5,
    0.01,
    "Data source: Illustrative scores created for demonstration",
    ha="center"
)

plt.savefig("comparison_4_products.png")
plt.show()