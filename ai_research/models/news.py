from .base import Base
from sqlalchemy import Column,  String, Date


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    media = Column(String)
    date = Column(Date)
    news_url = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    original_description = Column(Text)
    japanese_description = Column(Text)
