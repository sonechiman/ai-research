from urllib.parse import urljoin
import requests
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import oauthlib

import settings


def auth():
    request_token_url = urljoin(settings.WORDPRESS_URL, 'oauth1/request')
    oauth = OAuth1Session(settings.WORDPRESS_CLIENT_KEY,
                          client_secret=settings.WORDPRESS_CLIENT_SECRET)
    fetch_response = oauth.fetch_request_token(request_token_url)
    owner_key = fetch_response.get('oauth_token')
    owner_secret = fetch_response.get('oauth_token_secret')

    base_auth_url = urljoin(settings.WORDPRESS_URL, 'oauth1/authorize')
    authorization_url = oauth.authorization_url(base_auth_url)
    print('Please go here and authorize,', authorization_url)
    verifier = input('Paste the verification token here: ')

    access_token_url = urljoin(settings.WORDPRESS_URL, 'oauth1/access')
    oauth = OAuth1Session(settings.WORDPRESS_CLIENT_KEY,
                          client_secret=settings.WORDPRESS_CLIENT_SECRET,
                          resource_owner_key=owner_key,
                          resource_owner_secret=owner_secret,
                          verifier=verifier)
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')
    print("WORDPRESS_TOKEN = '%s'" % resource_owner_key)
    print("WORDPRESS_TOKEN_SECRET = '%s'" % resource_owner_secret)


if __name__ == "__main__":
    auth()
