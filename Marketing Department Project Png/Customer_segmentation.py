
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# Load cleaned dataset
df = pd.read_csv("Marketing_data_Cleaned.csv")

# Select important features
features = [
    "BALANCE",
    "PURCHASES",
    "CASH_ADVANCE",
    "CREDIT_LIMIT",
    "PAYMENTS",
    "TENURE"
]

X = df[features].copy()

# Handle missing values
X = X.fillna(X.median())

# Reduce skewness
X = np.log1p(X)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["CLUSTER"] = kmeans.fit_predict(X_scaled)

# Save segmented dataset
df.to_csv("Customer_Segments.csv", index=False)

print("Customer Segmentation Completed!")
print(df["CLUSTER"].value_counts().sort_index())

# Visualize clusters
plt.figure(figsize=(9, 6))

plt.scatter(
    df["BALANCE"],
    df["PURCHASES"],
    c=df["CLUSTER"],
    cmap="viridis",
    alpha=0.5
)

plt.xlabel("Balance")
plt.ylabel("Purchases")
plt.title("Customer Segmentation using K-Means")
plt.colorbar(label="Cluster")
plt.tight_layout()

plt.savefig("customer_segments.png")
plt.show()
