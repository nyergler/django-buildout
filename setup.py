# XXX license header here

from setuptools import setup, find_packages

setup(
    name = "django_buildout",
    version = "0.3",
    packages = find_packages('src'),
    package_dir = {'':'src'},

    # scripts and dependencies
    install_requires = ['setuptools',
                        'zc.buildout',
                        'zc.recipe.egg',
                        'Django',
                        ],
    include_package_data = True,
    zip_safe = True,

    # entry point for zc.buildout recipe
    entry_points = {
       'zc.buildout':
           ['deploy = django_buildout.deploy:DjangoDeploy',],
       'console_scripts':
           ['django-admin = django_buildout.scripts:djangoAdmin',
            'manage = django_buildout.scripts:projectManage',],
    },
    
    # author metadata
    author = 'Nathan R. Yergler',
    author_email = 'nathan@yergler.net',
    description = '.',
    license = 'GNU LGPL',
    url = 'http://code.google.com/p/django-buildout/',

    )
