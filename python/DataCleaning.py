# import pandas as pd
# dirty_data = pd.read_csv('dirtydata.csv')
# #print(dirty_data)

# new_df = dirty_data.dropna()
# print(new_df)

# # Finding mean / median / mode of all columns
# mean = new_df.mean()
# print(mean)

# median = new_df.median()
# print(median)

# mode = new_df.mode() 
# print(mode)

# # Finding mean / median / mode of one column
# duration_mean = new_df['Duration'].mean()
# print('Duraion Mean =', duration_mean)

# pulse_mean = new_df['Pulse'].mean()
# print('Pulse Mean =', pulse_mean)

# maxpulse_mean = new_df['Maxpulse'].mean()
# print('Maxpulse Mean =', maxpulse_mean)

# calories_mean = new_df['Calories'].mean()
# print('Calories Mean =', calories_mean)

# duration_mode = new_df['Duration'].mode()[0] 
# print('Duration Mode =', duration_mode)

# calories_mode = new_df['Calories'].mode()[0]
# print('Calories Mode =', calories_mode) 

# Replacing NaN values with respective column means

import pandas as pd
df = pd.read_csv('dirtydata.csv')
#print(df, '\n')

calories_mean = df['Calories'].mean()

df['Calories'].fillna(calories_mean, inplace=True) 
#print(df)

# Cleaning Date Column 

df['Date'] = pd.to_datetime(df['Date']) # converting wrong formats into date
#print(df)

df.dropna(subset=['Date'], inplace=True) # dropping rows in NaN values in Date Column only
#print(df) 

# # Replacing wrong value in Duration Column


# # Changing values one by one by manually observing in a small dataset

# df.loc[7, 'Duration'] = 45
# print(df)


# Looping though the whole column in a large dataset

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120
print(df)


# # Removing rows with wrong values

# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.drop(x, inplace=True) 
# print(df) 


# Discovering Duplicate Rows
print(df.duplicated()) # returns true for duplicates

# Removing Duplicate Rows
df.drop_duplicates(inplace=True)
print(df) 


# Finding correlations between each column in the dataset 
# Correlation coefficients ranges between [-1, 1]
# a good correlation is somewhat > 0.6 or < -0.6 

print(df.corr())  
