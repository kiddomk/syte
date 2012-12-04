# -*- coding: utf-8 -*-

DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'


#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'junseki.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = 'ySu1LivIWeq7qCvxMzA7ztC8Y0QSD51aTCifUoh3v0tVKdWKn0'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'https://api.twitter.com/'
TWITTER_CONSUMER_KEY = 'tSLEtdr22I9MWaPkeVkgQ'
TWITTER_CONSUMER_SECRET = 'xmsfG1lSKopDXk3CUFHpWRTwlZt90nOMTeDRlgEAhI'
TWITTER_USER_KEY = '17222732-3f5Q5aM3ni3AxdFiSN6vd3qhOXBoWC3KZJvqGF2FU'
TWITTER_USER_SECRET = '2137EkHncPn0BkxK6dmLR4UJuVHnPKRroAgVm2NR0'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '72f3fb42e6bada65c75d494e833d7a44d8cc6cc1'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '363930b334e0adb0a2e6'
GITHUB_CLIENT_SECRET = '15e0d5355cf19e023710c715e0e71e0dcabff525'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '348708.2823769.c28f079198854570ba730fb8cc65fc78'
INSTAGRAM_USER_ID = '348708'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = '282376990cb14a93a3484310328b229d'
INSTAGRAM_CLIENT_SECRET = 'ccc21d3dcce94a959341c31794bee8d1'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Foursquare Integration
FOURSQUARE_INTEGRATION_ENABLED = True
FOURSQUARE_API_URL = 'https://api.foursquare.com/v2/'
FOURSQUARE_ACCESS_TOKEN = 'UTA24PQFNOVHRPXRPSTERDLMFQ5NF3B420NKAGOKFC4PCC12'
FOURSQUARE_SHOW_CURRENT_DAY = True

FOURSQUARE_OAUTH_ENABLED = False
FOURSQUARE_CLIENT_ID = 'OPRS3JYNLRQM2QPTMTRFBGPNJFAEDALZGVD1SXCIVAWZYX2A'
FOURSQUARE_CLIENT_SECRET = '0C5LRRPRH1ADN4YZOBQEJEPI5PP23A3MDGNA04ZW23UBGLRP'
FOURSQUARE_OAUTH_AUTHORIZE_URL = 'https://foursquare.com/oauth2/authenticate'
FOURSQUARE_OAUTH_ACCESS_TOKEN_URL = 'https://foursquare.com/oauth2/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = 'UA-36758978-1'


#Woopra
WOOPRA_TRACKING_DOMAIN = 'junseki.com'
WOOPRA_TRACKING_IDLE_TIMEOUT = 300000  # 5 minutes
WOOPRA_TRACKING_INCLUDE_QUERY = False



#Disqus Integration
DISQUS_INTEGRATION_ENABLED = False
DISQUS_SHORTNAME = 'jseki'


#Lastfm Integration
LASTFM_INTEGRATION_ENABLED = True
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'
LASTFM_API_KEY = '29218ef112ec454d6020f1f6f5b1a3a8'

#SoundCloud Integration
SOUNDCLOUD_INTEGRATION_ENABLED = True
SOUNDCLOUD_API_URL = 'https://api.soundcloud.com/'
SOUNDCLOUD_CLIENT_ID = '704100d9b527d40c338daa5ee75ab3b4'
SOUNDCLOUD_SHOW_ARTWORK = False
SOUNDCLOUD_PLAYER_COLOR = 'ff912b'


#Bitbucket Integration
BITBUCKET_INTEGRATION_ENABLED = False
BITBUCKET_API_URL = 'https://api.bitbucket.org/1.0/'
# Forks count require one connection for each repository,
# set BITBUCKET_SHOW_FORKS to false to disable
BITBUCKET_SHOW_FORKS = False

#Tent.io Integration
TENT_INTEGRATION_ENABLED = True
TENT_ENTITY_URI = 'http://junseki.tent.is'
TENT_FEED_URL = 'http://junseki.tent.is'




if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://junseki.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
