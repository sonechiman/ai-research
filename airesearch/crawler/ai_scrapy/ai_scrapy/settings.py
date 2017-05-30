# -*- coding: utf-8 -*-
import settings

BOT_NAME = 'ai_scrapy'

SPIDER_MODULES = ['ai_scrapy.spiders']
NEWSPIDER_MODULE = 'ai_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
# USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 20
RANDOMIZE_DOWNLOAD_DELAY = True
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ai_scrapy.middlewares.AiScrapySpiderMiddleware': 543,
#}

# RETRY_TIMES = 10
# # Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    # 'scrapy_crawlera.CrawleraMiddleware': 610
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    # 'scrapy_proxies.RandomProxy': 100,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# CRAWLERA_ENABLED = True
# CRAWLERA_APIKEY = settings.CRAWLERA_API_KEY
# PROXY_LIST = settings.PROXY_LIST_PATH
# RANDOM_UA_PER_PROXY =True

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
# PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
# CUSTOM_PROXY = "http://host1:port"

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


ITEM_PIPELINES = {
    'ai_scrapy.pipelines.AngellistPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 20
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
