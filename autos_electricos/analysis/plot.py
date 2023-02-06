import sys
sys.path.append("..")
from poblacionAutosElectricos import *

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

"""
countModelYear = df.groupby("model_year")["model_year"].count()
countModelYear.plot(kind="bar", title="Count of Model Year")
plt.show()
"""

"""
dfgeo = df[["make","Vehicle Location"]]
dfgeo.plot(kind="scatter", x="Make", y="Vehicle Location", title="Make and Vehicle Location")
plt.show()
"""



