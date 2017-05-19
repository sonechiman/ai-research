from .base import Base
from sqlalchemy import Column,  String, Date


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, index=True, unique=True)
    crunchbase = Column(String, nullable=False, index=True, unique=True)
    url = Column(String, nullable=False, index=True, unique=True)
    detail = Column(Text, nullable=False)
    original_description = Column(Text, nullable=False)
    japanese_description = Column(Text)
    founded_date = Column(Date)
    categories = Column(String)
    news_page = Column(String)
    place = Column(String)
    funding = Column(String)

    def __repr__(self):
        return "<Company(id={0}, name={1}>".format(self.id, self.name)


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    media = Column(String)
    date = Column(Date)
    news_url = Column(String)
    company_name = Column(String)
    original_description = Column(Text)
    japanese_description = Column(Text)
