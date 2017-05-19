import json
import urllib.parse
import urllib.request
import csv

import settings
from airesearch.models import get_session, Company
from airesearch.translator import translator
from urls import urls, names

Session = get_session(settings.MYSQL_CONNECTION)
session = Session()


def encode_name(urls, category="ml"):
    names = list(map(lambda x: x.split("/")[-1], urls[category]))
    return names


def get_company(name, filter=""):
    base_url = "https://api.crunchbase.com/v/3/odm-organizations?"
    query = {
        "user_key": settings.CRUNCHBASE_API_KEY,
        "name": name
    }
    q = urllib.parse.urlencode(query)
    response = urllib.request.urlopen(base_url + q)
    result = json.loads(response.read().decode('utf-8'))
    for item in result["data"]["items"]:
        if not filter or item["properties"]["permalink"] == filter or item["properties"]["name"] == filter:
            return item["properties"]

# FIXME: avoid to duplicate


def get_companies_data_query():
    names = encode_name(urls)
    search_names = list(map(lambda x: x.replace('-', ' ').title(), names))
    unknowns = []
    for n, search_n in zip(names, search_names):
        if get_exiting_company(n) or get_exiting_company(search_n):
            print("%s already" % n)
            continue
        company_data = get_company(search_n, n)
        if company_data:
            save_company(company_data)
        else:
            print(n)
            unknowns.append(n)
    write_csv(unknowns, "unknown")


def get_companies_data():
    unknowns = []
    for n in names["ml"]:
        if get_exiting_company(n):
            print("%s already" % n)
            # continue
        company_data = get_company(n, n)
        if company_data:
            save_company(company_data)
        else:
            print(n)
            unknowns.append(n)
        write_csv(unknowns, "unknown")


def get_exiting_company(name):
    company = session.query(Company) \
                     .filter_by(name=name).first()
    return company


def write_csv(list, filename):
    f = open('%s.csv' % filename, 'ab')
    csvWriter = csv.writer(f)
    for item in list:
        csvWriter.writerow(item)


def save_company(c):
    company = get_exiting_company(c["name"])
    if not company:
        company = Company(name=c["name"])
    crunchbase_url = "https://www.crunchbase.com"
    company.abstract = c["short_description"]
    if not company.japanese_abstract:
        print("nothing")
        company.japanese_abstract = translator.translate_text(company.abstract)
    company.place = c["country_code"]
    company.url = c["homepage_url"]
    company.role = c["primary_role"]
    company.crunchbase = urllib.parse.urljoin(crunchbase_url, c["web_path"])
    session.add(company)
    session.commit()


def main():
    get_companies_data()

if __name__ == "__main__":
    main()
