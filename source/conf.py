# Configuration file for Sphinx documentation builder
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
project = 'String Manipulation for Technical Writers Documentation'
author = 'me'
version = '1.0'
release = '1.0.0'

# Add any Sphinx extension module names here
extensions = ['sphinx_simplepdf',]


# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# The master toctree document
master_doc = 'index'

# List of patterns, relative to the source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The HTML theme for the documentation
html_theme = 'alabaster'
