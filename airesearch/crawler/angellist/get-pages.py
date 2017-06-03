import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
from airesearch.models import get_session, ALCompany

Session = get_session(settings.MYSQL_CONNECTION)
session = Session()

# target_url = "https://angel.co/artificial-intelligence"
# target_url = "https://angel.co/deep-learning-2"
# target_url = "https://angel.co/natural-language-processing"
# target_url = "https://angel.co/machine-learning"
# target_url = "https://angel.co/image-recognition"
# target_url = "https://angel.co/speech-recognition"
# target_url = "https://angel.co/predictive-analytics"
target_url = "https://angel.co/big-data"


def item_waiter(num):
    def wait(driver):
        items = driver.find_elements_by_css_selector('.results_holder .base')
        if len(items) > num:
            return True
        else:
            return False
    return wait


def loading_waiter(driver):
    item = driver.find_elements_by_css_selector('.results_holder.disabled')
    if item:
        return False
    else:
        return True


def save_item(item):
    name = item.find_element_by_css_selector('.text .name a').text
    company = session.query(ALCompany) \
                     .filter_by(name=name).first()
    if not company:
        company = ALCompany(name=name)
    company.angellist = item.find_element_by_css_selector('.text .name a') \
                            .get_attribute("href")
    company.abstract = item.find_element_by_css_selector('.blurb').text
    company.followers = item.find_element_by_css_selector('.followers .value').text
    session.add(company)
    session.commit()


def get_items(url, filter=""):
    driver = webdriver.Chrome(os.path.join(
                              settings.DRIVER_PATH, 'chromedriver'))
    driver.implicitly_wait(10)
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    if filter == "followers":
        wait.until(loading_waiter)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.header .followers')))
        driver.find_element_by_css_selector('.header .followers').click()
        wait.until(loading_waiter)
    elif filter == "latest":
        wait.until(loading_waiter)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.header .joined')))
        driver.find_element_by_css_selector('.header .joined').click()
        wait.until(loading_waiter)
    item_num = 0
    items = []
    while True:
        try:
            wait.until(item_waiter(item_num))
        except:
            break
        items = driver.find_elements_by_css_selector('.results_holder .base')
        item_num = len(items)
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.content .more')))
            more = driver.find_element_by_css_selector('.content .more')
            more.click()
        except:
            break
    for item in items:
        save_item(item)
    driver.close()

if __name__ == "__main__":
    get_items(target_url)
    get_items(target_url, "followers")
    get_items(target_url, "latest")
