import pandas as pd

# hard coded data for df
data = [['Andrew',29],['Connor',25],['Smit',24]]

# creates and displays dataframe with name and age
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)
