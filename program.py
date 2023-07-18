import pandas as pd

df = pd.read_csv("data.csv")
df = df[["NAME", "RBIRTH2015", "RDEATH2015", "RNETMIG2015"]]
df = df.drop(df.index[[0, 1, 2, 3, 4]])
df.to_csv("new_data.csv", index = False)

ul = df.values.tolist()
print(ul)

l = []
for i in range(156): l.append([0, 0, 0])
for i in range(52):
	l[i][0] = ul[i][0]
	l[i][1] = "RBIRTH2015"
	l[i][2] = ul[i][1]
	l[52 + i][0] = ul[i][0]
	l[52 + i][1] = "RDEATH2015"
	l[52 + i][2] = ul[i][2]
	l[104 + i][0] = ul[i][0]
	l[104 + i][1] = "RNETMIG2015"
	l[104 + i][2] = ul[i][3]

df = pd.DataFrame(l, columns = ["NAME", "METRIC", "QUANTITY"])
print(df)

df.to_csv("new_data_stacked.csv", index = False)