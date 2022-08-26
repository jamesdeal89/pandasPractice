# exercise 1: print the first five and last five rows of data
import pandas as pd
table = pd.read_csv("Automobile_data.csv")
print(table.head(5))
print(table.tail(5))