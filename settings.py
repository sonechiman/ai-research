import os

MYSQL_CONNECTION = os.environ.get(
    'AIRESEARCH_DATA_MYSQL',
    'mysql+pymysql://root@localhost/airesearch?charset=utf8'
)

DRIVER_PATH = "/Users/user/util"

CRUNCHBASE_API_KEY = ""


try:
    import local_settings
    for var in dir(local_settings):
        vars()[var] = getattr(local_settings, var)
except ImportError:
    pass
