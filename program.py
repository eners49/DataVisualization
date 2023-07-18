import pandas as pd

df = pd.read_csv("data.csv")
df = df[["NAME", "RBIRTH2015", "RDEATH2015", "RNETMIG2015"]]
df = df.drop(df.index[[0, 1, 2, 3, 4]])
print(df)
df.to_csv("new_data.csv", index = False)