from urllib.parse import urljoin
import requests
from requests_oauthlib import OAuth1Session
from jinja2 import Environment, FileSystemLoader
from inflection import parameterize
from sqlalchemy import and_

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

        tags = post.model.categories.split(',')
        for t in tags:
            post.dict["tags"].append(self.convert_tag(t))

        if post_data:
            url = urljoin(url, str(post_data[0]['id']))
            r = self.oauth.post(url, json=post.dict)
        else:
            r = self.oauth.post(url, json=post.dict)
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
            'featured_media': model.logo_image.wordpress_id,
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
            'fundings': self.model.fundings,
            'place': self.model.place,
            'url': self.model.url
        }
        if self.model.images:
            render_dict['main_image'] = self.model.images[0].url
        if len(self.model.images) > 1:
            render_dict['sub_images'] = [i.url for i in self.model.images[1:]]
        render_dict['followers'] = self._get_follwers()
        render_dict['employees'] = self._get_employees()

        html = tpl.render(render_dict)
        self.dict['content'] = html

    def _get_follwers(self):
        if self.model.followers:
            return max(self.model.followers // 10, 100)
        else:
            return None

    def _get_employees(self):
        if self.model.employees == '201-500':
            return '500人未満'
        elif self.model.employees == '51-200':
            return '200人未満'
        elif self.model.employees == '11-50':
            return '50人未満'
        elif self.model.employees == '1-10':
            return '10人未満'
        return None



def main():
    session = WPSession()
    # companies = dbsession.query(ALCompany)\
    #                      .filter(and_(ALCompany.japanese_description != None,
    #                              ALCompany.logo_image != None))
    companies = dbsession.query(ALCompany)\
                         .filter(ALCompany.id==782)
    for c in companies:
        post = WPPost(c)
        session.post(post)


if __name__ == "__main__":
    main()
