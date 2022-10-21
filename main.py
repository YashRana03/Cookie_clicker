from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Setting up the driver to connect to the website
chrome_driver_path = "C:\dev\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# List of items that can be bought to produce cookies
list_of_items = ["buyPortal", "buyShipment", "buyMine", "buyFactory", "buyGrandma", "buyCursor"]

# Countdown clock of 5 seconds
count_down = time.time() + 5

while True:
    cookie = driver.find_element(by="id", value="cookie")
    cookie.click()
    money = driver.find_element(by="id", value="money").text

    if time.time() > count_down:
        # This checks if the most priced item can be bought, if not it buys whatever it can with the money available
        for item in list_of_items:
            feature = driver.find_element(by="css selector", value=f"#{item} b")
            feature_price = driver.find_element(by="css selector", value=f"#{item} b")
            feature_price = int(float(feature_price.text.split("-")[1].replace(",", "").strip(" ")))
            if int(money) >= feature_price:
                feature.click()
                break
        # Starts the 5-second countdown again
        count_down = time.time() + 5

