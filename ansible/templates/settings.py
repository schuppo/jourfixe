# Django settings for mail project.
import os
from logging.handlers import SysLogHandler

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MODOBOA_DIR = os.path.dirname(__file__)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    'test'
]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mail',                       # Or path to database file if using sqlite3.
        'USER': 'mail',                     # Not used with sqlite3.
        'PASSWORD': 'test',                 # Not used with sqlite3.
        'HOST': 'localhost',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {
            "init_command" : 'SET foreign_key_checks = 0;',
        },
    },

    # "pfxadmin" : {
    #     "ENGINE" : "django.db.backends.",
    #     "NAME" : "",
    #     "USER" : "",
    #     "PASSWORD" : ""
    # },

    'amavis': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'amavis',                       # Or path to database file if using sqlite3.
        'USER': 'amavis',                     # Not used with sqlite3.
        'PASSWORD': 'amavis',                 # Not used with sqlite3.
        'HOST': 'localhost',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {
            "init_command" : 'SET foreign_key_checks = 0;',
        },
    },

}

DATABASE_ROUTERS = ["modoboa.extensions.amavis.dbrouter.AmavisRouter"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(MODOBOA_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(MODOBOA_DIR, 'sitestatic')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/sitestatic/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8q_a6f8#llj&amp;%qb_1dgl#4-ecl$=s5%*4iqj4!43&amp;ri251+#na'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',

    'modoboa.lib.middleware.AjaxLoginRedirect',
    'modoboa.lib.middleware.CommonExceptionCatcher',
    'modoboa.lib.middleware.ExtControlMiddleware',
)

ROOT_URLCONF = 'mail.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mail.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'reversion',
)

# A dedicated place to register Modoboa applications
# Do not delete it.
# Do not change the order.
MODOBOA_APPS = (
    'modoboa',
    'modoboa.core',
    'modoboa.lib',
    # Modoboa extensions here.
    'modoboa.extensions.admin',
    'modoboa.extensions.postfix_relay_domains',
    'modoboa.extensions.limits',
    'modoboa.extensions.postfix_autoreply',
    'modoboa.extensions.webmail',
    'modoboa.extensions.stats',
    'modoboa.extensions.sievefilters',
    'modoboa.extensions.amavis',
)

INSTALLED_APPS += MODOBOA_APPS

AUTH_USER_MODEL = 'core.User'

SOUTH_TESTS_MIGRATE = False

#MODOBOA_CUSTOM_LOGO = os.path.join(MEDIA_URL, "custom_logo.png")

#DOVECOT_LOOKUP_PATH = ('/path/to/dovecot', )

AUTHENTICATION_BACKENDS = (
    'modoboa.lib.authbackends.SimpleBackend',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'syslog': {
            'format': '%(name)s: %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'syslog-auth': {
            'class': 'logging.handlers.SysLogHandler',
            'facility': SysLogHandler.LOG_AUTH,
            'formatter': 'syslog'
        },
        'modoboa': {
            'class': 'modoboa.core.loggers.SQLHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'modoboa.auth': {
            'handlers': ['syslog-auth', 'modoboa'],
            'level': 'INFO',
            'propagate': False
        },
        'modoboa.admin': {
            'handlers': ['modoboa'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/mail.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'mail': {
            'handlers': ['logfile'],
            'level': 'WARNING', # Or maybe INFO or DEBUG
            'propagate': False
        },
    },
}
