import numpy as np
import pandas as pd

def createnew(df: pd.DataFrame, columns: set[any]):
    cols_total: set[any] = set(df.columns)
    diff: set[any] = cols_total - columns
    df.drop(diff, axis = 1, inplace = True)

df = pd.read_csv("data.csv")

createnew(df, {"NAME", "CENSUS2010POP", "ESTIMATESBASE2010", "POPESTIMATE2010", "POPESTIMATE2011", "POPESTIMATE2012", "POPESTIMATE2013", "POPESTIMATE2014", "POPESTIMATE2015", "POPESTIMATE2016", "POPESTIMATE2017", "POPESTIMATE2018", "POPESTIMATE2019"})
print(df)
df.to_csv("new_data.csv")