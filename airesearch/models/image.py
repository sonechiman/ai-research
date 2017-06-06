from .base import Base
from sqlalchemy import Column, String, Date, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    url = Column(String(256), index=True)
    wordpress_id = Column(Integer, index=True)
    wordpress_url = Column(String(256))

    angellist_id = Column(Integer, ForeignKey('angellist_companies.id'))
    crunchbase_id = Column(Integer, ForeignKey('crunchbase_companies.id'))

    def __repr__(self):
        return "<Image(id={0}>".format(self.id)


class LogoImage(Base):
    __tablename__ = 'logo_images'

    id = Column(Integer, primary_key=True)
    url = Column(String(256), index=True)
    wordpress_id = Column(Integer, index=True)
    wordpress_url = Column(String(256))

    angellist_id = Column(Integer, ForeignKey('angellist_companies.id'))
    crunchbase_id = Column(Integer, ForeignKey('crunchbase_companies.id'))

    def __repr__(self):
        return "<LogoImage(id={0}>".format(self.id)
