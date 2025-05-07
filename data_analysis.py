import pyreadstat
import pandas as pd

columns_needed = ["MRJDAY30A", "MENTHLTH", "SMOKE100", "ALCDAY5"]
df, meta = pyreadstat.read_xport("LLCP2018.XPT", usecols=columns_needed)

print(df.head())