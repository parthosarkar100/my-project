import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/power_outage_data.csv")

print("Summary of Dataset:\n", df.describe())

plt.figure(figsize=(8,5))
df.groupby("Reason")["Duration(hours)"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Reasons for Power Outage")
plt.show()
