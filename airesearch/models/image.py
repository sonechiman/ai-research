from .base import Base
from sqlalchemy import Column, String, Date, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    url = Column(String(256), index=True)

    angellist_id = Column(Integer, ForeignKey('angellist_companies.id'))
    crunchbase_id = Column(Integer, ForeignKey('crunchbase_companies.id'))

    def __repr__(self):
        return "<Images(id={0}>".format(self.id)
