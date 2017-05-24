

list_page = {
    "ml": "",
    "ai": "",
    "iot": ""
}

urls = {
    "ml": [],
    "ai": []
}

names = {
    "ml": [],
    "ai": []
}

try:
    import local_urls
    for var in dir(local_urls):
        vars()[var] = getattr(local_urls, var)
except ImportError:
    pass
