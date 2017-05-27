import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings

# crunchbase block selenium


def item_waiter(num):
    def wait(driver):
        items = driver.find_elements_by_css_selector('.results_holder .base')
        if len(items) > num:
            return True
        else:
            return False
    return wait


def get_items(item):
    pass


def get_items(url):
    driver = webdriver.Chrome(os.path.join(
                              settings.DRIVER_PATH, 'chromedriver'))
    driver.implicitly_wait(10)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    item_num = 0
    items = []
    while True:
        try:
            wait.until(item_waiter(item_num))
        except:
            driver.close()
            break
        items = results.find_elements_by_css_selector('.results_holder .base')
        item_num = len(items)
        more = driver.find_element_by_css_selector('.content .more')
        more.click()
    print(items)


get_items("https://angel.co/artificial-intelligence")
