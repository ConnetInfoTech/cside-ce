AUTHOR = 'Connet Information Technology. Shanghai'
SITENAME = "CSIDE"
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'

SUBTITLE = 'Connect Scripting Integrated Development Environment (CSIDE)'
SUBTEXT = '''
Scripting: choosing a goal and writing like it has already come true.

'''
COPYRIGHT = '©2024 · Connet Information Technology. Shanghai'
PATH = 'content'
THEME = 'themes/Papyrus'
OUTPUT_PATH = 'docs'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors', 'pelican-toc']

DISPLAY_PAGES_ON_MENU = False
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'about', 'blog'))
PAGINATED_TEMPLATES = {'index':None,'tag':None,'category':None,'author':None,'archives':24,'blog':None}

# Site search plugin
# SEARCH_MODE = "docs"
# SEARCH_HTML_SELECTOR = "main"
# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = None

# Social widgets
SOCIAL = (
    ('github', 'https://github.com/ConnetInfoTech'),
)

# Article share widgets
SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''
