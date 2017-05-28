from .base import Base
from sqlalchemy import Column, String, Date, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, index=True, unique=True)
    crunchbase_id = Column(Integer, ForeignKey('crunchbase_companies.id'))
    angellist_id = Column(Integer, ForeignKey('angellist_companies.id'))

    def __repr__(self):
        return "<Company(id={0}, name={1}>".format(self.id, self.name)
