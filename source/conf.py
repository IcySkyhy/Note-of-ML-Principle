# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IcySky\'s ML Notes'
copyright = '2026, IcySkyhy'
author = 'IcySkyhy'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx.ext.mathjax', 
]

myst_enable_extensions = [
    "dollarmath",  # 开启 $...$ 和 $$...$$ 支持
    "amsmath",     # 开启高级数学环境支持
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']
