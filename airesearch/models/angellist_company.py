from .base import Base
from .image import Image
from sqlalchemy import Column, String, Date, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class ALCompany(Base):
    __tablename__ = 'angellist_companies'

    id = Column(Integer, primary_key=True)
    logo = Column(String(256))
    angellist = Column(String(256), index=True)
    name = Column(String(128), nullable=False, index=True, unique=True)
    url = Column(String(256), index=True)
    abstract = Column(Text)
    japanese_abstract = Column(Text)
    original_description = Column(Text)
    japanese_description = Column(Text)
    founded_date = Column(Date)
    employees = Column(String(128))
    categories = Column(String(256))
    place = Column(String(256))
    followers = Column(Integer)
    video_url = Column(String(256))

    master = relationship('Company', backref="angellist", uselist=False)
    fundings = relationship('ALFunding', backref="company")
    images = relationship('Image', backref="angellist")
    logo_image = relationship('LogoImage', backref="angellist", uselist=False)

    def __repr__(self):
        return "<Company(id={0}, name={1}>".format(self.id, self.name)


class ALFunding(Base):
    __tablename__ = 'angellist_fundings'

    id = Column(Integer, primary_key=True)
    date = Column(String(256), index=True)
    stage = Column(String(128))
    raised = Column(String(128))

    company_id = Column(Integer, ForeignKey('angellist_companies.id'))

    def __repr__(self):
        return "<Funding(id={0}, name={1}>".format(self.id, self.comapany.name)
