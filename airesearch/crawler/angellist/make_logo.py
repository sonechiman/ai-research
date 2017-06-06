import settings
from airesearch.models import get_session, ALCompany, LogoImage
from sqlalchemy import and_

Session = get_session(settings.MYSQL_CONNECTION)
session = Session()


def make_logo():
    companies = session.query(ALCompany) \
                       .filter(and_(ALCompany.logo != None,
                               ALCompany.logo_image==None))
    for c in companies:
        c.logo_image = LogoImage(url=c.logo)
        session.add(c)
        session.commit()


if __name__ == "__main__":
    make_logo()
