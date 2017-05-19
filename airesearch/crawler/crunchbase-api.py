import json
import urllib.parse
import urllib.request
import settings
from urls import urls


def encode_name(urls, category="ml"):
    names = list(map(lambda x: x.split("/")[-1], urls["ml"]))
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
        if not filter or item["properties"]["permalink"] == filter:
            return item["properties"]


def get_companies_data():
    names = encode_name(urls)
    search_names = list(map(lambda x: x.replace('-', ' ').title(), names))
    for n, search_n in zip(names, search_names):
        company = get_company(search_n, n)
        save_company(company)


def save_company(c):
    print(c)


def main():
    get_companies_data()


if __name__ == "__main__":
    main()
