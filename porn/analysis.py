import json
import pandas as pd


# CLEANING DATA
#########################################################################
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
##########################################################################

"""
#TOP 10 ETIQUETAS EN RUSO MÁS USADAS E
##########################################################################
# ordenar por cantidad
xvideos_rusia = xxx.sort_values(by=['cantidad'], ascending=False).head(10)
##########################################################################
"""

#TOP 10 ETIQUETAS EN INGLÉS MÁS USADAS 
##########################################################################
import nltk
nltk.download('words')
nltk.download('stopwords')


english_words = set(nltk.corpus.words.words())
stop_words = set(nltk.corpus.stopwords.words('english'))

xxx['etiqueta'] = xxx['etiqueta'].apply(nltk.word_tokenize)
xxx['etiqueta'] = xxx['etiqueta'].apply(lambda x: [word.lower() for word in x if word.lower() in english_words])
xxx['etiqueta'] = xxx['etiqueta'].apply(lambda x: ' '.join(x))

vacias = xxx[xxx['etiqueta'] != '']
vacias['etiqueta'] = vacias['etiqueta'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
vacias = vacias[vacias['etiqueta'] != '']
vacias = vacias.drop_duplicates(subset='etiqueta')

xvideos_ingles = vacias.sort_values(by='cantidad', ascending=False).head(10)
print(xvideos_ingles)
##########################################################################


#TOP 10 ETIQUETAS EN ESPAÑOL MÁS USADAS 
##########################################################################
nltk.download('cess_esp')
spanish_words = set(nltk.corpus.cess_esp.words())
stop_words_es = set(nltk.corpus.stopwords.words('spanish'))

xxx['etiqueta'] = xxx['etiqueta'].apply(nltk.word_tokenize)
xxx['etiqueta'] = xxx['etiqueta'].apply(lambda x: [word.lower() for word in x if word.lower() in spanish_words])
xxx['etiqueta'] = xxx['etiqueta'].apply(lambda x: ' '.join(x))

vacias = xxx[xxx['etiqueta'] != '']
vacias['etiqueta'] = vacias['etiqueta'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words_es]))
vacias = vacias[vacias['etiqueta'] != '']
vacias = vacias[vacias['etiqueta'] != 'amateur']
vacias = vacias[vacias['etiqueta'] != 'sexy']
vacias = vacias[vacias['etiqueta'] != 'une']
vacias = vacias[vacias['etiqueta'] != 'solo']
vacias = vacias[vacias['etiqueta'] != 'sur']
vacias = vacias[vacias['etiqueta'] != '1-2']
vacias = vacias[vacias['etiqueta'] != '?']
vacias = vacias[vacias['etiqueta'] != 'anal']
vacias = vacias[vacias['etiqueta'] != 'das']
vacias = vacias[vacias['etiqueta'] != 'man']
vacias = vacias[vacias['etiqueta'] != 'dos']
vacias = vacias[vacias['etiqueta'] != 'ama']
vacias = vacias[vacias['etiqueta'] != 'bien']
vacias = vacias[vacias['etiqueta'] != 'mal']
vacias = vacias[vacias['etiqueta'] != 'red']
vacias = vacias[vacias['etiqueta'] != 'come']
vacias = vacias[vacias['etiqueta'] != 'legal']
vacias = vacias[vacias['etiqueta'] != 'glamour']
vacias = vacias[vacias['etiqueta'] != 'lei']
vacias = vacias.drop_duplicates(subset='etiqueta')

xvideos_espanol = vacias.sort_values(by='cantidad', ascending=False).head(10)
print(xvideos_espanol)
##########################################################################
