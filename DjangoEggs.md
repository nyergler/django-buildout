# Introduction #

[setuptools](http://peak.telecommunity.com/DevCenter/setuptools) searches the
[Python Package Index](http://cheeseshop.python.org/pypi) for
[eggs](http://peak.telecommunity.com/DevCenter/PythonEggs) when attempting to
resolve packages.  It can also be pointed at an "index" page with specially formed links
to enable resolution of packages not present in PyPI.  This page serves as a stable URL
for an index of Django-related eggs.

# Using the Index #

## setuptools and easy\_install ##

To use this index page with [http://peak.telecommunity.com/DevCenter/EasyInstall
easy\_install] specify the URL with the `-f` parameter.  For example:
```

  $ easy_install -f http://code.google.com/p/django-buildout/wiki/DjangoEggs yahoo-ui

```

## zc.buildout ##

To enable zc.buildout to find packages using this index, specify the URL as `find-links`
parameter.  For example, in `buildout.cfg`:
```

[buildout]
find-links = http://code.google.com/p/django-buildout/wiki/DjangoEggs

[part_n]
...
```

See ProjectLifecycle for details on using zc.buildout with Django applications.

# Adding to the Index #

To add a package to the index, add it to the list below.  Your link should conform to
setuptools expectation of a "primary link".  For example, to specify that a link is to the
egg FooBar 1.0, the link would be formed as:
```
http://example.com/eggs/FooBar.tgz#egg=FooBar-1.0
```

Note that the version is optional; the link may be to a tarball, an egg, or executable
file.  For details on package discovery, see the
[setuptools documentation](http://peak.telecommunity.com/DevCenter/setuptools).

# Index Contents #

  * [Django 0.95](http://code.djangoproject.com/svn/django/tags/releases/0.95/#egg=Django-0.95)
  * [django\_buildout](http://django-buildout.googlecode.com/files/django_buildout-0.2-py2.4.egg)
  * yahoo-ui
  * fckeditor
  * fckeditor-connector