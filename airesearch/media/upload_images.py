from urllib.parse import urljoin
import requests
from requests_oauthlib import OAuth1Session

import settings
from airesearch.models import get_session, Image, LogoImage


Session = get_session(settings.MYSQL_CONNECTION)
session = Session()


class WPImageUploadrer():
    def __init__(self):
        self.base_url = urljoin(settings.WORDPRESS_URL, '/wp-json/')
        self.oauth = OAuth1Session(settings.WORDPRESS_CLIENT_KEY,
                                   client_secret=settings.WORDPRESS_CLIENT_SECRET,
                                   resource_owner_key=settings.WORDPRESS_TOKEN,
                                   resource_owner_secret=settings.WORDPRESS_TOKEN_SECRET)

    def get_image_query(self, model=Image):
        images = session.query(model)\
                        .filter(model.wordpress_id==None)
        return images

    def download_image(self, url, timeout=10):
        print(url)
        response = requests.get(url, allow_redirects=False, timeout=timeout)
        if response.status_code != 200:
            e = Exception("HTTP status: " + str(response.status_code))
            raise e
        content_type = response.headers["content-type"]
        if 'image' not in content_type:
            e = Exception("Content-Type: " + content_type)
            raise e
        return response.content

    def upload_image(self, image, filename):
        url = urljoin(self.base_url, 'wp/v2/media')
        files = {
            'file': (filename, image),
            'Content-Type': 'image/jpeg'
        }
        r = self.oauth.post(url, files=files)
        print(r.json())
        return r.json()

    def transfer_image(self, model="image"):
        class_name = Image if model == "image" else LogoImage
        raw_images = self.get_image_query(class_name)
        for i in raw_images:
            image = self.download_image(i.url)
            res = self.upload_image(image, "%s_%s.jpg" % (model, i.id))
            i.wordpress_id = res["id"]
            i.wordpress_url = res["source_url"]
            session.add(i)
            session.commit()


if __name__ == "__main__":
    uploader = WPImageUploadrer()
    uploader.transfer_image("logoimage")
    uploader.transfer_image()
