import pandas as pd
df=pd.read_csv("cleaned_data.csv")
print(df.shape)
category_revenue = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
print(category_revenue)

import matplotlib.pyplot as plt
category_revenue.plot(kind="bar", figsize=(10,5), title="Revenue by Category", color="teal")
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.tight_layout()
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
print(df["Date"].min(), df["Date"].max())
df.groupby("Month")["Amount"].sum().plot(kind="line", figsize=(12,5), title="Monthly Sales Trend", marker="o", color="green")
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df["Status"].value_counts().plot(kind="bar", figsize=(12,5), title="Order Status Breakdown", color="green")
plt.ylabel("Number of Orders")
plt.xlabel("Status")
plt.tight_layout()
plt.show()