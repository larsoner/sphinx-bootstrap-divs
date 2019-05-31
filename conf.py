# -*- coding: utf-8 -*-
from datetime import date
import os
import sys

curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir)))

import sphinx_bootstrap_divs  # noqa

extensions = [
    'sphinx_bootstrap_theme',
    'sphinx_bootstrap_divs',
    'sphinx_fontawesome',
]
source_suffix = '.rst'
master_doc = 'index'
nitpicky = True
exclude_trees = ['build', '_templates', '_static']
html_theme = 'bootstrap'
html_theme_options = {
    'bootswatch_theme': "lumen",
}
project = u'sphinx-bootstrap-divs'
td = date.today()
copyright = u'2019-%s, sphinx-bootstrap-div Developers' % (td.year,)
version = release = sphinx_bootstrap_divs.__version__
templates_path = ['_templates']
html_static_path = ['_static']
