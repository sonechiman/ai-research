import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings

# crunchbase block selenium


def get_items(url):
    driver = webdriver.Chrome(os.path.join(
                              settings.DRIVER_PATH, 'chromedriver'))
    driver.get(url)
    prior = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        print(current)
        break
        time.sleep(5)
        if temp == document.body.scrollHeight:
            break
    driver.close()

get_items("https://techcrunch.com/2017/05/19/these-are-the-arguments-against-net-neutrality-and-why-theyre-wrong/")
