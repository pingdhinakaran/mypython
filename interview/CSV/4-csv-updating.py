# importing the pandas library
import pandas as pd

# reading the csv file
df = pd.read_csv("AllDetails.csv")

# updating the column value/data
df.loc[0,'Name'] = 'dhinakaran'

# writing into the file
df.to_csv("AllDetails.csv", index=False)

print(df)
