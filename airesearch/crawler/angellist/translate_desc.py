import settings
from airesearch.models import get_session, ALCompany
from airesearch.translator import translator

Session = get_session(settings.MYSQL_CONNECTION)
session = Session()

# REFACTOR: Dont repeat


def translate_desc():
    companies = session.query(ALCompany)\
                       .filter(ALCompany.original_description != None,
                               ALCompany.japanese_description == None)
    for company in companies:
        company.japanese_description = translator.translate_text(company.original_description)
        session.add(company)
        session.commit()


def translate_abstract():
    companies = session.query(ALCompany)\
                       .filter(ALCompany.abstract != None,
                               ALCompany.japanese_abstract == None)
    for company in companies:
        company.japanese_abstract = translator.translate_text(company.abstract)
        session.add(company)
        session.commit()

if __name__ == "__main__":
    translate_desc()
    translate_abstract()
