import json
import pandas as pd

# import data xvideos.json to dataframe etiqueta y cantidad
with open('xvideos.json') as f:
    data = json.load(f)
    xxx = pd.DataFrame(data)

# drop dot in column cantidad
xxx['cantidad'] = xxx['cantidad'].str.replace('.', '')

# convert column cantidad to int
xxx['cantidad'] = xxx['cantidad'].astype(int)

# drop row with value 0 in column cantidad
for i in range(0, 100):
    xxx.drop(xxx[xxx.cantidad == i].index, inplace = True)

# ordenar por cantidad
print(xxx.sort_values(by=['cantidad'], ascending=False))



