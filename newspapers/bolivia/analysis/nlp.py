import pandas as pd
import numpy as np
from collections import Counter
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import json
import plotly.express as px

word = open('../data/stopWordList.json')
my_long_list = json.load(word)

with open("../data/paginaSiete_titulo.txt", "r") as csv_file:
    text = csv_file.read()

nltk.download('stopwords')
palabras = stopwords.words('spanish')

for i in range(len(my_long_list)):
    palabras.append(my_long_list[i])

# agregar las palabras El, La a palabras
palabras.append('El')
palabras.append('La')
palabras.append('Santa')
palabras.append('Cruz')
palabras.append('Paz')

# counter text word 
word_counter = Counter(text.split()).most_common(1000)
freq_words = [w for w in word_counter if not w[0] in palabras]
freq_words = freq_words[:20]

"""
sns.set(rc={'figure.figsize':(13,8)})
df = pd.DataFrame(freq_words, columns=['Palabras', 'Frecuencia'])
sns.barchart(data=df, x='Palabras', y='Frecuencia',palette='Blues_d')
plt.xticks(rotation=40)
plt.show()
"""

df = pd.DataFrame(freq_words, columns=['Palabras', 'Frecuencia'])

"""
['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
             'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
             'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
             'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
             'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
             'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
             'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
             'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
             'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
             'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
             'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
             'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
             'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
             'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
             'ylorrd']
"""

fig = px.treemap(df, path=[px.Constant('Palabras más usadas por Página Siete (2013-2022)'), 'Palabras'],
                 values=df['Frecuencia'],
                 color=df['Frecuencia'],
                 color_continuous_scale='plasma',
                 color_continuous_midpoint=np.average(df['Frecuencia'])
                )
fig.data[0]['textfont']['color'] = "black"
fig.data[0]['textfont']['size'] = 15
# font-weight: bold
fig.data[0]['textfont']['family'] = "Courier New"
fig.data[0]['textinfo'] = "label+value"
# change letter type
fig.update_layout(font_family="Courier New")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
fig.write_html("../output/pnlp7.html")
