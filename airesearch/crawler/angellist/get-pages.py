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
    more = driver.find_element_by_class_name('more')
    items = driver.find_element_by_class_name('base')
    print(items)
    if more:
        more.click()
    driver.close()

get_items("https://angel.co/artificial-intelligence")
