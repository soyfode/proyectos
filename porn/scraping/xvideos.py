import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

opts = Options()
opts.add_experimental_option("detach", True)

opts.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
)

symbol = ["09","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

url_list = []

for i in symbol:
    link = 'https://www.xvideos.com/tags/{}'.format(i)
    url_list.append(link)

print(url_list)

sleep(random.uniform(2.0, 3.0))

for url in url_list:

    sleep(random.uniform(2.0, 3.0))

    print(url)

    driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

    driver.get(url)

    sleep(random.uniform(2.0, 3.0))

    xvideos = driver.find_elements(By.XPATH, '//*[@id="tags"]/li')

    for x in xvideos:
        etiqueta = x.find_element(By.XPATH, './/a/b').text
        cantidad = x.find_element(By.XPATH, './/a/span').text
        data = {'etiqueta': etiqueta, 'cantidad': cantidad}
        with open('xvideos.json', 'a') as f:
            json.dump(data, f,ensure_ascii=False)
            f.write(',\n')

    driver.quit()
