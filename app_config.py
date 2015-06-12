import os

from authomatic.providers import oauth2
from authomatic import Authomatic

"""
COPY EDITING
"""
					  # CHANGE GOOGLE KEY HERE
COPY_GOOGLE_DOC_KEY = '1EB0Xq0mt_MkszaBHeSpIWGdlSnt0errmxo7pQqTdvCw'

COPY_PATH = 'data/copy.xlsx'

"""
OAUTH
"""

GOOGLE_OAUTH_CREDENTIALS_PATH = '~/.google_oauth_credentials'

authomatic_config = {
    'google': {
        'id': 1,
        'class_': oauth2.Google,
        'consumer_key': os.environ.get('GOOGLE_OAUTH_CLIENT_ID'),
        'consumer_secret': os.environ.get('GOOGLE_OAUTH_CONSUMER_SECRET'),
        'scope': ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/userinfo.email'],
        'offline': True,
    },
}

authomatic = Authomatic(authomatic_config, os.environ.get('AUTHOMATIC_SALT'))