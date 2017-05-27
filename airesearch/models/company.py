from .base import Base
from sqlalchemy import Column, String, Date, Integer, Text


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, index=True, unique=True)
    crunchbase = Column(String(256), index=True)
    angellist = Column(String(256), index=True)
    url = Column(String(256), index=True)
    angellist_name = Column(String(128), index=True, unique=True)
    abstract = Column(Text)
    japanese_abstract = Column(Text)
    original_description = Column(Text)
    japanese_description = Column(Text)
    founded_date = Column(Date)
    role = Column(String(256))
    categories = Column(String(256))
    news_page = Column(String(256))
    place = Column(String(256))
    funding = Column(String(256))

    def __repr__(self):
        return "<Company(id={0}, name={1}>".format(self.id, self.name)
