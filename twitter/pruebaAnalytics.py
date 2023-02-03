import pandas as pd
# import tweets.csv file to a dataframe with name columns tweet and place
df = pd.read_csv('tweets.csv', names=['tweet', 'place'])
# print place column of df without NaN values
print(df['place'].dropna())


