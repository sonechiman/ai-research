from .base import Base
from sqlalchemy import Column, Integer, String, Date, Text


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    media = Column(String(32))
    date = Column(Date)
    news_url = Column(String(256), nullable=False)
    company_name = Column(String(32), nullable=False)
    original_description = Column(Text)
    japanese_description = Column(Text)
