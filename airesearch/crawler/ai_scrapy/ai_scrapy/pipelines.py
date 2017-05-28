import logging

import settings
from airesearch.models import get_session, ALCompany, Image, ALFunding
from .items import AngelListItem

Session = get_session(settings.MYSQL_CONNECTION)


class MysqlPipeline(object):
    item_class = None

    def __init__(self):
        self.session = Session()

    def process_item(self, item, spider):
        if isinstance(item, self.__class__.item_class):
            self._process_item(item, spider)
            self.session.commit()
        return item

    def _process_item(self, item, spider):
        pass

    def _set_attributes(self, db_item, item):
        for k, v in item.items():
            if v is not None:
                setattr(db_item, k, v)


class AngellistPipeline(MysqlPipeline):
    item_class = AngelListItem

    def _process_item(self, item, spider):
        company = self.session.query(ALCompany) \
                      .filter_by(angellist=item['angellist']) \
                      .first()
        if not company:
            company = ALCompany(angellist=item['angellist'])

        self._set_images(company, item)
        self._set_fundings(company, item)
        self._set_attributes(company, item)
        if company not in self.session:
            self.session.add(company)

    def _set_images(self, company, item):
        images = item.pop('images', [])
        for i in images:
            image = self.session.query(Image).filter_by(url=i).first()
            if not image:
                    image = Image(url=i)
            company.images.append(image)

    def _set_fundings(self, company, item):
        fundings = item.pop('fundings', [])
        for f in fundings:
            funding = self.session.query(ALFunding)\
                          .filter(ALFunding.date == f["date"],
                                  ALFunding.company_id == company.id).first()
            if not funding:
                    funding = ALFunding(date=f["date"])
            funding.raised = f["raised"]
            funding.stage = f["type"]
            company.fundings.append(funding)
