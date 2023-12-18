import pandas as pd
import numpy as np

h = np.random.normal(160, 30, size=100)
w = np.random.normal(60, 10, size=100)

df = pd.DataFrame({"height":h, "weight":w})
df.to_csv("dataset.csv")


