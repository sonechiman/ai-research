from urllib.parse import urljoin
import requests
from requests_oauthlib import OAuth1Session
from jinja2 import Environment, FileSystemLoader
from inflection import parameterize

import settings
from airesearch.models import get_session, ALCompany


DBSession = get_session(settings.MYSQL_CONNECTION)
dbsession = DBSession()


class WPSession():
    def __init__(self):
        self.base_url = urljoin(settings.WORDPRESS_URL, '/wp-json/')
        self.oauth = OAuth1Session(settings.WORDPRESS_CLIENT_KEY,
                                   client_secret=settings.WORDPRESS_CLIENT_SECRET,
                                   resource_owner_key=settings.WORDPRESS_TOKEN,
                                   resource_owner_secret=settings.WORDPRESS_TOKEN_SECRET)
        self.tags = {}

    def get(self):
        url = urljoin(self.base_url, 'wp/v2/posts')
        r = self.oauth.get(url)
        print(r.json())

    def get_with_slug(self, slug):
        url = urljoin(self.base_url, 'wp/v2/posts?slug=%s&status=any' % slug)
        r = self.oauth.get(url)
        return r.json()

    def post(self, post):
        url = urljoin(self.base_url, 'wp/v2/posts/')
        post_data = self.get_with_slug(post.key)
        # data = {}
        # data["featured_media"] = 12

        tags = post.model.categories.split(',')
        for t in tags:
            post.dict["tags"].append(self.convert_tag(t))

        if post_data:
            url = urljoin(url, str(post_data[0]['id']))
            r = self.oauth.post(url, json=post.dict)
        else:
            r = self.oauth.post(url, json=post.dict)
            pass
        print(r.json())

    def convert_tag(self, tag):
        tag = tag.strip()
        if not self.tags:
            url = urljoin(self.base_url, 'wp/v2/tags?per_page=100')
            r = self.oauth.get(url)
            for item in r.json():
                self.tags[item['slug']] = item['id']
        if parameterize(tag) in self.tags:
            return self.tags[parameterize(tag)]
        else:
            post_url = urljoin(self.base_url, 'wp/v2/tags')
            new_tag = {'name': tag, 'slug': parameterize(tag)}
            r = self.oauth.post(post_url, json=new_tag).json()
            self.tags[r['slug']] = r['id']
            print('*** Make new tag: %s ***' % tag)
            print(r)
            return r['id']


class WPPost:
    def __init__(self, model):
        self.model = model
        self.key = model.angellist.split('/')[-1]
        self.dict = {
            'title': model.name,
            'status': 'pending',
            'categories': [2],
            'excerpt': model.japanese_abstract,
            'comment_status': 'closed',
            'slug': self.key,
            'tags': []
        }
        self.set_content()

    def set_content(self):
        env = Environment(loader=FileSystemLoader('./', encoding='utf8'),
                          extensions=['pyjade.ext.jinja.PyJadeExtension'])
        tpl = env.get_template('template.jade')
        render_dict = {
            'abstract': self.model.japanese_abstract,
            'description': self.model.japanese_description,
            'video_url': self.model.video_url,
            'fundings': self.model.fundings
        }
        if self.model.images:
            render_dict['main_image'] = self.model.images[0].url
        if len(self.model.images) > 1:
            render_dict['sub_images'] = [i.url for i in self.model.images[1:]]
        html = tpl.render(render_dict)
        print(html)
        self.dict['content'] = html


def main():
    session = WPSession()
    companies = dbsession.query(ALCompany)\
                         .filter(ALCompany.japanese_description != None)
    for c in companies[:1]:
        print(c.name)
        post = WPPost(c)
        session.post(post)


if __name__ == "__main__":
    main()
