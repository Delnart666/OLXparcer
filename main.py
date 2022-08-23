from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Edge()

list_card_url = []

headers = {'User-Agent': "Edge/ (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.98"}



url = 'https://www.olx.ua/d/uk/uslugi/odessa/q-строительные-работы/?page=2'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml') #parser
data = soup.find_all('div', class_ = 'css-19ucd76')

for i in data:
    try:
        card_url = i.find('a').get('href')
        card_url = 'https://www.olx.ua' + card_url
        if card_url in list_card_url:
            pass
        else:
            list_card_url.append(card_url)
    except:
        card_url = None

for card_url in list_card_url:
    driver.get(card_url)
    driver.maximize_window()
    time.sleep(5)

    find_more_element = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(4) > div:nth-child(2)')
    action = ActionChains(driver)
    action.move_to_element(find_more_element).perform()
    time.sleep(5)

    try:
        elements = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1vnw4ly > div.css-1p8n2mw > div > div > div.css-1saqqt7 > div > button')
        elements.click()
        time.sleep(5)
        name = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1pyxm30 > div:nth-child(1) > div:nth-child(2) > div > a > div > div.css-1fp4ipz > h4').text
        phone = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1pyxm30 > div:nth-child(1) > div:nth-child(4) > div > button.css-65ydbw-BaseStyles > span > a').text

    except:
        phone = None
        name = None
    file = open(r"C:\Users\38099\Desktop\ПРОГРАММИРОВАНИЕ\ПРОЕКТЫ\Парсинг на пайтоне\Результат парсера.txt", 'a',encoding='utf=8')
    try:
        file.write(name)
    except:
        file.write('None')
    file.write(' - ')
    try:
        file.write(phone)
    except:
        file.write('None')
    file.write('\n')
    file.close()
    print(name, '-', phone)







