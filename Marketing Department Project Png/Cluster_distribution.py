
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load customer segmentation data
df = pd.read_csv("Customer_Segments.csv")

# Customer count by cluster
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="CLUSTER",
    hue="CLUSTER",
    palette="viridis",
    legend=False
)

plt.title("Customer Distribution by Cluster")
plt.xlabel("Customer Cluster")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("customer_cluster_distribution.png", dpi=300)

plt.show()
