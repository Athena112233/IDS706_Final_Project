import pandas as pd
import dask.dataframe as dd

data = dd.read_csv("../data/Cleaned_2018_Flights.csv")
print(data.head(10))