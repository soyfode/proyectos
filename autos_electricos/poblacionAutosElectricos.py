######## Libraries ###########
#############################

from dotenv import load_dotenv
from sodapy import Socrata
import os
import json
import pandas as pd
import matplotlib.pyplot as plt

###############################
###############################



########################### TOKEN ##############################
################################################################

load_dotenv()

API_Key_ID_dataWaGov = os.getenv("API_Key_ID_dataWaGov")
API_Key_Secret_dataWaGov = os.getenv("API_Key_Secret_dataWaGov")
APP_Token_dataWaGov= os.getenv("APP_Token_dataWaGov")
Secret_Token_dataWaGov = os.getenv("Secret_Token_dataWaGov")
Password_dataWaGov = os.getenv("Password_dataWaGov")

client =  Socrata("data.wa.gov",
                  APP_Token_dataWaGov,
                  username = "soyfode@gmail.com",
                  password = Password_dataWaGov,
                  )

################################################################
################################################################

################# DATA FRAME ################
#############################################

results = client.get("f6w7-q2d2",limit=114600)
df = pd.DataFrame.from_records(results)

##############################################
##############################################


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

countModelYear = df.groupby("model_year")["model_year"].count()
# plot x-label years and y-label count
countModelYear.plot(kind="bar", title="Count of Model Year")
plt.show()


df1 = df[["model_year","make","model"]]
model = df1.pivot_table(values = "model", index=["make"],columns="model_year", aggfunc="count",fill_value="-",margins=True)
timeCar = model.sort_values("All",ascending=True)
print(timeCar)


"""
# groupby model and make
groupModel = df.groupby(["make","model"])["model"].count()
"""

"""
dfgeo = df[["make","Vehicle Location"]]

print(dfgeo["Vehicle Location"].head())
"""

"""
dfgeo.plot(kind="scatter", x="Make", y="Vehicle Location", title="Make and Vehicle Location")
plt.show()
"""



























