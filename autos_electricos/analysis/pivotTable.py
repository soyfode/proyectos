import sys
sys.path.append("..")
from poblacionAutosElectricos import df

##########################################
########### Data exploration #############
"""
# print first 5 rows
print(df.head())

# shape of data
print(df.shape)

# column names list of data 
print(df.columns.tolist())

# summary of data
print(df.describe())
"""
##########################################
##########################################

df1 = df[["model_year","make","model"]]
model = df1.pivot_table(values = "model", index=["make"],columns="model_year", aggfunc="count",fill_value="-",margins=True)
timeCar = model.sort_values("All",ascending=True)
print(timeCar)

