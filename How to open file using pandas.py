# in this program open a csv file
#And print the rows and columns

import pandas as pd
df=pd.read_csv('pandas2csv.csv')
print(df)
# print only rows using rows index
print(df[:1])

# print columns using columns name
print(df['Date'])
