import pandas as pd

# Load customer segments file
df_segments = pd.read_csv("customer_segments.csv")

# Display first few rows
print(df_segments.head())

# Check how many customers belong to each cluster
print(df_segments['Cluster'].value_counts())

import matplotlib.pyplot as plt

# Load customer segments
df_segments = pd.read_csv("customer_segments.csv")

# Group by cluster and calculate mean values
segment_profiles = df_segments.groupby("Cluster").mean()

# Plot bar chart
segment_profiles[['Recency', 'Frequency', 'TotalPrice']].plot(kind="bar", figsize=(10, 5))
plt.title("Customer Segment Profiles")
plt.ylabel("Scaled RFM Values")
plt.xlabel("Cluster")
plt.legend(["Recency", "Frequency", "TotalPrice"])
plt.show()


# Cluster distribution
df_segments['Cluster'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7), startangle=90, cmap='coolwarm')
plt.title("Customer Segment Distribution")
plt.ylabel("")
plt.show()
