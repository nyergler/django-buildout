import os
import sys

import zc.buildout
import zc.recipe.egg

class DjangoDeploy:

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

        self.egg = zc.recipe.egg.Egg(buildout, name, options)

    def install(self):

        # make a copy of the current python path so we can restore when complete
        orig_path = sys.path[:]
        
        # get our project [develop-]egg onto the python path
        requirements, ws = self.egg.working_set()
        sys.path = ws.entries + sys.path

        # determine the root path for our static files
        static_root = self.options.get('static_files_root', None)

        if static_root is None:

            # import our project settings
            from django.conf import Settings
            settings = Settings(self.options['django_settings'])

            # check if the root is specified in the project's settings file
            try:
                static_root = settings.STATIC_FILES_ROOT
            except AttributeError, e:
                raise zc.buildout.UserError("""Root path for static files must be specified as static_files_root in buildout.cfg or STATIC_FILES_ROOT in settings.py""")

        # make sure the root path exists
        static_root = os.path.abspath(static_root)
        if not(os.path.exists(static_root)):
            raise zc.buildout.UserError("""The static file root, %s, does not exists.""" % static_root)
        
        # iterate over the static file entry points
        static_files = []
        for ep in ws.iter_entry_points('django_buildout', 'static_files'):
            static_files += ep.load()(static_root)

        # reset the python path
        sys.path = orig_path

        # return the list of static files installed
        return static_files

    update = install


## def find_urls():
##     """Iterates over djangodeploy:urls entry points returning an
##     urlpatterns object."""

##     # XXX we need a way to get back the working set of modules we
##     # XXX had in the DjangoDeploy.install call... or do we just use
##     # INSTALLED_APPS?
##     # that seems reasonable, we just need to figure out how to build
##     # up a working set of the packages... hrmm... of course there are cases
##     # where the package name != distribution name... maybe as SETTING?
##     #
##     # INSTALLED_APP_URLS that maps prefixes to each distribution name?
