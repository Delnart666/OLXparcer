from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

list_card_url = []
PROXY = [
    "154.83.29.201:999" # IP:PORT or HOST:PORT
    "154.83.29.202:999" # IP:PORT or HOST:PORT
    "154.83.29.203:999"  # IP:PORT or HOST:PORT
    "154.83.29.204:999"  # IP:PORT or HOST:PORT
    "154.83.29.205:999"  # IP:PORT or HOST:PORT
    "154.83.29.206:999"  # IP:PORT or HOST:PORT
    "154.83.29.207:999"  # IP:PORT or HOST:PORT
    "154.83.29.208:999"  # IP:PORT or HOST:PORT
    "154.83.29.209:999"  # IP:PORT or HOST:PORT
    "154.83.29.200:999"  # IP:PORT or HOST:PORT
]
headers = {'User-Agent': "Chrome/ (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.98"}

pages = 11
for count in range(1, pages):
    url = f'https://www.olx.ua/d/uk/dom-i-sad/stroitelstvo-remont/metalloprokat-armatura/odessa/?page={count}'

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


howmanysits = 0
for card_url in list_card_url:
    driver.get(card_url)
    time.sleep(75)
    try:
        find_more_element = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1vnw4ly > div.css-1p8n2mw')
        action = ActionChains(driver)
        action.move_to_element(find_more_element).perform()
        time.sleep(75)
    except:
        pass

    try:
        elements = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1vnw4ly > div.css-1p8n2mw > div > div > div.css-1saqqt7 > div > button')
        elements.click()
        time.sleep(75)
        name = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1vnw4ly > div.css-1p8n2mw > div > div > div.css-1ucpzm6 > div > div.css-1fp4ipz > h4').text
        phone = driver.find_element(By.CSS_SELECTOR, '#root > div.css-50cyfj > div.css-1on7yx1 > div:nth-child(3) > div.css-1vnw4ly > div.css-1p8n2mw > div > div > div.css-1saqqt7 > div > ul > li > a').text

    except:
        phone = None
    if phone == None:
        file = open(r"C:\Users\38099\Desktop\ПРОГРАММИРОВАНИЕ\ПРОЕКТЫ\Парсинг на пайтоне\Сайты для ручной проверки.txt", 'a',encoding='utf=8')
        file.write(card_url)
        file.write('\n')
        file.close()

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
    file.write(' - ')
    file.write(card_url)
    file.write('\n')
    file.close()
    howmanysits += 1
    print(howmanysits,'.',name, '-', phone, '-', card_url)







