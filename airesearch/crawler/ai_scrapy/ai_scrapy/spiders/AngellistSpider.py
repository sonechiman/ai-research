# -*- coding: utf-8 -*-
import scrapy

import settings
from airesearch.models import get_session, ALCompany

from ..items import AngelListItem
import random


class AngellistSpider(scrapy.Spider):
    name = "angellist"
    allowed_domains = ["angel.co"]
    count = 0
    session_count = 2
    request_list = [
                    "https://angel.co/artificial-intelligence",
                    "https://angel.co/deep-learning-2",
                    # "https://angel.co/natural-language-processing",
                    "https://angel.co/machine-learning",
                    # "https://angel.co/image-recognition"
                    ]

    def __init__(self, *args, **kwargs):
        super(AngellistSpider, self).__init__(*args, **kwargs)
        Session = get_session(settings.MYSQL_CONNECTION)
        self.session = Session()
        urls = self.session.query(ALCompany.angellist)\
                   .filter(ALCompany.original_description == None)
        urls = [url[0] for url in urls]
        self.start_urls = urls

    def parse(self, response):
        company = AngelListItem()
        company["angellist"] = response.url
        company["original_description"] = self.parse_description(response)
        company["url"] = response.css('.company_url::text').extract_first()
        company["place"] = response.css('.js-location_tags a::text')\
                                   .extract_first()
        company["categories"] = ', '.join(response.css('.js-market_tags a::text').extract())
        company["employees"] = response.css('.js-company_size::text')\
                                       .extract_first()
        if company["employees"]:
            company["employees"] = company["employees"].strip()
        company["images"] = response.css('.big-mobile-container img')\
                                    .xpath('@src').extract()
        company["fundings"] = self.parse_funding(response)
        company["logo"] = response.css('.photo.subheader-avatar img')\
                                  .xpath('@src').extract_first()
        company["video_url"] = response.css(".big iframe").xpath('@src')\
                                       .extract_first()
        yield company
        self.count += 1
        print(self.count, self.session_count)
        if self.count % self.session_count == 0:
            self.session_count = random.randint(3, 15)
            print("Random request happen!!")
            yield scrapy.http.Request(random.choice(self.request_list), dont_filter=True,
                                      callback=self.parse_nothing)

    def parse_funding(self, response):
        sel = response.css('.details.inner_section')
        types = list(map(lambda x: x.strip(),
                     response.css('.details .type::text').extract()))
        dates = response.css('.details.inner_section .date_display::text')\
                        .extract()
        prices = response.css('.details .raised a::text').extract()
        result = []
        for t, d, p in zip(types, dates, prices):
            temp = {}
            temp["type"] = t
            temp["date"] = d
            temp["raised"] = p
            result.append(temp)
        return result

    def parse_nothing(self, response):
        pass

    def parse_description(self, response):
        text_list = response.css('.product_desc .content::text').extract()
        text_list = [t.strip() for t in text_list if t != '\n']
        hidden_list = response.css('.product_desc .content .hidden ::text')\
                              .extract()
        if hidden_list:
            hidden_list = [t.strip() for t in hidden_list if t != '\n']
            text_list[-1] += hidden_list[0]
            text_list += hidden_list[1:]
        return '\n'.join(text_list)
