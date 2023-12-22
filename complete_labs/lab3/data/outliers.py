import pandas as pd
import numpy as np

data = pd.read_csv("labs/lab3/data/lab_2_dataset.csv")
subset = data
outlier_indices = np.random.choice(
    subset.index, size=int(0.01 * len(subset)), replace=False
)
data.loc[outlier_indices, "cost"] = -1000000
japan_rows = data[(data["destination"] == "Tokyo") & (data["cost"] > 0)].index
data.loc[japan_rows, "cost"] *= 158

data.to_csv("labs/lab3/data/lab_3_dataset.csv", index=False)
