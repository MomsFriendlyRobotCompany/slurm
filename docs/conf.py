# make clean && sphinx-build -E -W -b html . _build/html

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
# sys.setrecursionlimit(1500)


# -- Project information -----------------------------------------------------

project = 'slurm'
copyright = '2014, Kevin Walchko'
author = 'Kevin J. Walchko'

# The full version, including alpha/beta/rc tags
import slurm
release = slurm.__version__         # major.minor.patch
version = release.rsplit('.', 1)[0] # major.minor

source_suffix = ['.rst', '.md']
# default_role = "any"
# The master toctree document.
master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "recommonmark",
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    # "sphinx.ext.todo",
    'sphinx.ext.mathjax',
    "m2r2",
]

# https://sphinx-autoapi.readthedocs.io/en/latest/tutorials.html
autoapi_options = [
    "members",
    'undoc-members',
    # 'private-members',
    # 'show-inheritance',
    'show-module-summary',
    # 'special-members',
    # 'imported-members'
]
autoapi_dirs = ['../slurm']
autoapi_type = "python"
# autoapi_template_dir = '_templates'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
pygments_style = 'sphinx'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme_options = {
    "description": "this is my description",
    "fixed_sidebar": True,
    'logo': 'logo.png',
    'github_user': 'walchko',
    'github_repo': 'slurm',
    "github_button": True,
    # "sidebar_width": "200px",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# def setup(app):
#     app.add_config_value('recommonmark_config', {
#             'enable_math': True,
#             'enable_eval_rst': True,
#             'enable_auto_doc_ref': True,
#             'auto_code_block': True,
#             }, True)
#     app.add_transform(AutoStructify)
