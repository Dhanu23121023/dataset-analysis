import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

print(data.head())
print(data.describe())

data['sales'].plot(kind='bar')
plt.show()
