# -*- coding: utf-8 -*-
import os
import sys

curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir)))

extensions = [
    'sphinx_bootstrap_theme',
    'sphinx_bootstrap_theme_collapse',
]
source_suffix = '.rst'
master_doc = 'index'
nitpicky = True
exclude_trees = ['build']
html_theme = 'bootstrap'
html_theme_options = {
    'source_link_position': "nav",
    'bootswatch_theme': "sandstone",
    'bootstrap_version': "3",
    'navbar_pagenav': False,
}
