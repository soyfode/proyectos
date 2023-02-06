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
data = pd.DataFrame.from_records(results)
for i in range(len(data)):
    x = data["geocoded_column"][i]["coordinates"][0]
    y = data["geocoded_column"][i]["coordinates"][1]
    print(x,y)

##############################################
##############################################



"""
# groupby model and make
groupModel = df.groupby(["make","model"])["model"].count()
"""
