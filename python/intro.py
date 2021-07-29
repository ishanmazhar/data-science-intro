import numpy as np
import pandas as pd

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# arr2 = [1,2,3,4,5]
# print(arr2)

# Series
# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)

# Data Frame
data = {
    'Sat':[1,2,3,4,5],
    'Sun':[2,4,6,8,10],
    'Mon':[1,3,5,7,9]
}
df = pd.DataFrame(data=data)
print(df)

# Select 1st 3 rows
print(df.loc[[0,1,2]])

# Select 1st 2 rows using named index
df2 = pd.DataFrame(data=data, index=['Ishan', 'Masum', 'Rana', 'Adnan', 'Hasib']) 
print(df2.loc[['Ishan', 'Masum']])

# Read / open csv files as DF

import pandas as pd
file1 = pd.read_csv('Data.csv')
print(file1)

import pandas as pd
file2 = pd.read_csv('dataset.csv')
print(file2)  # prints the first 5 and the last 5 rows of the Dataset
print(file2.to_string()) # file2.to_string() prints the full Dataset

# Read / open json files as DF

import pandas as pd
file3 = pd.read_json('data.js')
print('File-3')
print(file3)  # prints the first 5 and the last 5 rows of the Dataset
print(file3.to_string()) # file2.to_string() prints the full Dataset

# Printing first rows
import pandas as pd
file3 = pd.read_json('data.js')
print('First 10 rows\n')
print(file3.head(10))  # prints first 10 rows
print('First 5 rows\n')
print(file3.head())  # prints first 5 rows

# Printing last rows
import pandas as pd
file3 = pd.read_json('data.js')
print('Last 10 rows\n')
print(file3.tail(10))  # prints first 10 rows
print('Last 5 rows\n')
print(file3.tail())  # prints first 5 rows

# Printing info of data
import pandas as pd
file3 = pd.read_json('data.js')
print(file3.info()) # prints info of data

# Counting the number of rows
import pandas as pd
file3 = pd.read_json('data.js')
print(file3.shape[0]) # prints the number of rows

# Counting the number of columns
import pandas as pd
file3 = pd.read_json('data.js')
print(file3.shape[1]) # prints the number of columns

# Data Cleaning and Describing
import pandas as pd
file3 = pd.read_json('data.js')
file3.dropna(axis=0, inplace=True) # dropna removes the missing / NaN values; axis=0 removes the entire row
print(file3.to_string()) # file2.to_string() prints the full Dataset
print(file3.info())

pd.set_option('display.max_columns', None)
print(file3.describe()) #describe() gives count, mean, SD, min, max, 25%, 50%, 75%