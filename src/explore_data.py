import pandas as pd  # this means bring me the pandas tool

# think df as: Our table in python
df = pd.read_csv("Data/Raw/sales_data.csv")  # this means go to the sales_data.csv file and read it

# show me the first five head
print(df.head())

# This will give us information regarding how many rows are there how many columns are there
print(df.shape) # .shape is an attribute

# what are all the columns in my data set
print(df.columns)



