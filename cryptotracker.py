from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import smtplib,ssl
import time

def send_mail(s):
  context = ssl.create_default_context()
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls(context=context)
  server.ehlo()

  server.login("sender@gmail.com","app password")
  
  subject = 'Price Fell Down'
  body = "Hurry!! Price of "+s+" fell down."

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'sender@gmail.com',
    'receiver@gmail.com',
    msg
  )
  print('Hey Email has been sent')
  server.quit()


def get_cryptocurrency_prices():
    url = "https://coinmarketcap.com/"
    options = Options()
    options.add_argument("--headless=new")  
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    btc_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.sc-48e202ed-1.hJWPVO > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-996d6db8-2.kQcCjW > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > a > span"))).text
    eth_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div.sc-48e202ed-1.hJWPVO > div.main-content > div.cmc-body-wrapper > div > div:nth-child(1) > div.sc-996d6db8-2.kQcCjW > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > a > span"))).text

    driver.quit()

    return btc_price, eth_price
def display_prices(btc_price, eth_price):
    print(f"Bitcoin (BTC) Price: ${btc_price}")
    print(f"Ethereum (ETH) Price: ${eth_price}")

def check_price(thres,price,f):
    if(price<thres):
        if(f==0):
            send_mail("Bitcoin")
        else:
            send_mail("Ethereum")

def fetch_cryptocurrency_prices(interval):
    while True:
        btc_price, eth_price = get_cryptocurrency_prices()

        btc_price = btc_price[1:].split(',')
        btc_price = "".join(btc_price)

        eth_price = eth_price[1:].split(',')
        eth_price = "".join(eth_price)
        thresbit = 30000
        threseth = 1800
        print(f"Threshold Bitcoin Price: ${thresbit}")
        print(f"Threshold Ethereum Price: ${threseth}")
        check_price(thresbit,float(btc_price),0)
        check_price(threseth,float(eth_price),1)

        display_prices(btc_price, eth_price)
        time.sleep(interval)

if __name__ == "__main__":
    fetch_cryptocurrency_prices(1) 