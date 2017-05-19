from .base import Base
from sqlalchemy import Column, String, Date, Integer, Text


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, index=True, unique=True)
    crunchbase = Column(String(256), nullable=False, index=True, unique=True)
    url = Column(String(256), nullable=False, index=True, unique=True)
    detail = Column(Text, nullable=False)
    original_description = Column(Text, nullable=False)
    japanese_description = Column(Text)
    founded_date = Column(Date)
    categories = Column(String(256))
    news_page = Column(String(256))
    place = Column(String(32))
    funding = Column(String(32))

    def __repr__(self):
        return "<Company(id={0}, name={1}>".format(self.id, self.name)
