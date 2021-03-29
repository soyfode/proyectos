import requests
from lxml import html

encabezados = { "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" }

url_holafan = "https://holafan.com/collections/all"

respuesta = requests.get(url_holafan,headers=encabezados)

parser = html.fromstring(respuesta.text)

#nombres=parser.xpath("//div[@class='product-item__caption  reviews-visible ']/h3/text()")
#print(nombres)

# extracción de nombres
nombre = parser.find_class('product-item__title')
nombres = [i.text_content() for i in nombre]
print(nombres)

#extracción de precios en pesos
precio = parser.find_class('money')
precios = [i.text_content() for i in precio]
print(precios)

