#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lev Stipakov'
SITENAME = u'Lev Stipakov'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'fi'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Blogini puheenvuorossa', 'http://levstipakov.puheenvuoro.uusisuomi.fi/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lstipakov'),
          ('facebook', 'http://facebook.com/lstipakov'),
          ('linkedin', 'https://fi.linkedin.com/in/lstipakov'),
          ('github', 'http://github.com/lstipakov'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITENAME="Lev Stipakov"
DEFAULT_DATE = 'fs'

THEME = "../Projects/pelican-themes/blue-penguin"

PLUGIN_PATHS = ["/home/lev/Projects/pelican-plugins"]
PLUGINS = ['i18n_subsites',]

I18N_SUBSITES = {
    'ru': {
        'SITENAME': 'Блог Льва Стипакова',
    }
}

languages_lookup = {
             'en': 'English',
             'fi': 'Suomeksi',
             'ru': 'По-русски'
             }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
             'lookup_lang_name': lookup_lang_name,
             }
