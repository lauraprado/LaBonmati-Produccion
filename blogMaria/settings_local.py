ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'bae53cf1953e.ngrok.io']
DEBUG = True
SECRET_KEY = '0prc8c+vw5$!$#+ur85t0ko-v@_5*n2xbomy@9*yj1^om%j=z^'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False