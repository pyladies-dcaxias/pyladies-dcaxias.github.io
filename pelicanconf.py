#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Paula Grangeiro'
SITENAME = u'PyLadies Duque de Caxias'
SITEURL = 'http://duquedecaxias.pyladies.com'


PATH = 'content'


TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt'


STATIC_PATHS = ['images', 'media']
STATIC_URL = '/output/theme/'


DEFAULT_PAGINATION = 10


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Collections
from collections import namedtuple

Menu = namedtuple('Menu', ['id', 'name', 'url', 'css_class', 'css_id'])
items = (
    (1, 'Home', '/', '', ''),
    (2, 'Sobre', '#about', 'scroller', ''),
    (3, 'Ajude-nos', '#support', 'scroller', ''),
    (4, 'Recursos', '/resources', '', ''),
    (5, 'Blog', '', '#', ''),
)

MENU = [Menu(*item) for item in items]
