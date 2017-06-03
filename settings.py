import os

MYSQL_CONNECTION = os.environ.get(
    'AIRESEARCH_DATA_MYSQL',
    'mysql+pymysql://root@localhost/airesearch?charset=utf8'
)

DRIVER_PATH = "/Users/user/util"

CRUNCHBASE_API_KEY = ""

WORDPRESS_URL = ""
WORDPRESS_CLIENT_KEY = ""
WORDPRESS_CLIENT_SECRET = ""
WORDPRESS_TOKEN = ""
WORDPRESS_TOKEN_SECRET = ""

PROXY_LIST_PATH = "/Users/user/util"

CRAWLERA_API_KEY = ""


try:
    import local_settings
    for var in dir(local_settings):
        vars()[var] = getattr(local_settings, var)
except ImportError:
    pass
