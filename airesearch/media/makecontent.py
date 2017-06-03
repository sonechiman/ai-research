from urllib.parse import urljoin
import requests
from requests_oauthlib import OAuth1Session


import settings


class WPSession():
    def __init__(self):
        self.base_url = urljoin(settings.WORDPRESS_URL, '/wp-json/')
        self.oauth = OAuth1Session(settings.WORDPRESS_CLIENT_KEY,
                                   client_secret=settings.WORDPRESS_CLIENT_SECRET,
                                   resource_owner_key=settings.WORDPRESS_TOKEN,
                                   resource_owner_secret=settings.WORDPRESS_TOKEN_SECRET)

    def get(self):
        url = urljoin(self.base_url, 'wp/v2/posts')
        r = self.oauth.get(url)
        print(r.json())

    def post(self):
        url = urljoin(self.base_url, 'wp/v2/posts')
        data = {}
        data["title"] = "タイトル"
        data["content"] = """
        <h1>これは</h1>
        <div>テストです<img src="http://160.16.221.238/wp-content/uploads/2017/06/4e0e9bcd12fd70168ca4ea1e963ceb49.jpg"></div>
        """
        data["slug"] = "title"
        data["status"] = "pending"
        data["excerpt"] = "これはびっくりするやつ"
        data["featured_media"] = 12
        data["comment_status"] = "closed"
        data["categories"] = 5
        data["tags"] = [8, 9]
        r = self.oauth.post(url, json=data)
        print(r.json())


class WPPost():
    def __init__(self):
        pass


def main():
    session = WPSession()
    session.post()
    # session.get()


if __name__ == "__main__":
    main()
