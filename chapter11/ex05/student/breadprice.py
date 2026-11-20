import pandas as pd
import matplotlib.pyplot as plt

# original table
frame = pd.read_csv("breadprice.csv")
print(frame)

# cleaned up table
years = frame.pop("Year")
newVal = frame.loc[10].mean()
frame.fillna(newVal, inplace = True)
print(frame)

# setup for line plot
averages = []
for i in range(len(frame)):
    averages.append(frame.iloc[i].mean())

# making of the line plot
plt.plot(years, averages, marker = "o")
plt.title("Average price of bread")
plt.xlabel("Year")
plt.ylabel("Average price")
plt.show()