from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def get_session(connection_string):
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    return Session
