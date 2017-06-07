import os

from sqlalchemy import and_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
from airesearch.models import get_session, ALCompany, Image, LogoImage, ALFunding

Session = get_session(settings.MYSQL_CONNECTION)


class ALClawler:
    def __init__(self):
        self.session = Session()
        self.driver = webdriver.Chrome(os.path.join(settings.DRIVER_PATH, 'chromedriver'))
        self.driver.implicitly_wait(4)
        self.wait = WebDriverWait(self.driver, 10)

    def crawl_all_pages(self):
        companies = self.session.query(ALCompany)\
                        .filter(ALCompany.original_description == None,
                                ALCompany.logo_image == None)
        for c in companies[:30]:
            self.crawl_page(c)

    def crawl_page(self, company):
        self.driver.get(company.angellist)
        try:
            company.original_description = self._parse_description()
        except:
            company.original_description = ""
            print('%s: No text' % company.name)

        company.url = self.driver.find_element_by_css_selector('.company_url').text
        company.place = self.driver.find_element_by_css_selector('.js-location_tags a').text
        company.employees = self.driver.find_element_by_css_selector('.js-company_size').text
        company.categories = self._parse_categories()
        if company.employees:
            company.employees = company.employees.strip()
        company.images = self._parse_images()
        logo, logo_image = self._parse_logo_image()
        company.logo = logo
        company.logo_image = logo_image
        company.fundings = self._parse_fundings(company.id)
        try:
            company.video_url = self.driver.find_element_by_css_selector('.big iframe')\
                                    .get_attribute('src')
        except:
            print('%s: Not video url' % company.name)
        print(company.name)
        self.session.add(company)
        self.session.commit()

    def _parse_description(self):
        content_box = self.driver.find_element_by_css_selector('.product_desc .content')
        content_box.find_element_by_css_selector('.hidden_more').click()
        return content_box.text

    def _parse_categories(self):
        categories = self.driver.find_elements_by_css_selector('.js-market_tags a')
        return ', '.join([c.text for c in categories])

    def _parse_images(self):
        image_items = self.driver.find_elements_by_css_selector('.big-mobile-container img')
        images = []
        for item in image_items:
            url = item.get_attribute("src")
            image = self.session.query(Image).filter_by(url=url).first()
            if not image:
                image = Image(url=url)
            images.append(image)
        return images

    def _parse_logo_image(self):
        url = self.driver.find_element_by_css_selector('.photo.subheader-avatar img')\
                  .get_attribute('src')
        image = self.session.query(LogoImage).filter_by(url=url).first()
        if not image:
            image = LogoImage(url=url)
        return url, image

    def _parse_fundings(self, c_id):
        sels = self.driver.find_elements_by_css_selector('.details.inner_section')
        fundings = []
        for s in sels:
            f_type = s.find_element_by_css_selector('.type').text.strip()
            f_date = s.find_element_by_css_selector('.date_display').text
            f_raised = s.find_element_by_css_selector('.raised').text
            funding = self.session.query(ALFunding)\
                          .filter(and_(ALFunding.date == f_date,
                                  ALFunding.company_id == c_id)).first()
            if not funding:
                funding = ALFunding(date=f_date)
            funding.type = f_type
            funding.raised = f_raised
            fundings.append(funding)
        return fundings


if __name__ == "__main__":
    crawler = ALClawler()
    crawler.crawl_all_pages()
