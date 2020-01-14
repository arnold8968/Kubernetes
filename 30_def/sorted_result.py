import pandas as pd

raw_file = "./result/default_0723.csv"
out_file = "./result/default_0723.csv"

df = pd.read_csv(raw_file)
df = df.sort_values(["start_time"])
df.to_csv(out_file)