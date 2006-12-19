# Minimal Django Buildout setup.py
# http://code.google.com/p/django-buildout/
# 

from setuptools import setup, find_packages

setup(
    name = "myproject",
    version = "0.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    
    # scripts and dependencies
    dependency_links = [
        "http://code.google.com/p/django-buildout/downloads/list",
	"http://code.google.com/p/django-buildout/wiki/DjangoEggs"],

    install_requires = ['setuptools',
                        'Django>=0.95',
                        ],

    include_package_data = True,
    zip_safe = False,

    # author metadata
    author = 'Nathan R. Yergler',
    author_email = 'nathan@yergler.net',
    description = 'A simple Django app for demonstrating django-buildout.',
    url = 'http://code.google.com/p/django-buildout',

    )
