# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Быстрый старт FindFace Lite Руководство'
copyright = '2022, NtechLab'
author = 'DimDimit'

release = '1.2'
version = '0.1.0'

# -- General configuration
language = 'ru'
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
html_favicon = '_static/index.ico'

html_sidebars = { '**': [
    'localtoc.html',
    'ethicalads.html',  # Put the ad below the navigation but above previous/next
    'relations.html',
    'sourcelink.html',
    'searchbox.html',
] }

# -- Options for EPUB output
epub_show_urls = 'footnote' 
# epub_show_urls = 'inline'
epub_tocdepth = 3
epub_language = 'ru'
