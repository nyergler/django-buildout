import django.core.management

def djangoAdmin():
    
    django.core.management.execute_from_command_line()

def projectManage():

    try:
        import settings # Assumed to be in the same directory.
    except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
        sys.exit(1)

    django.core.management.execute_manager(settings)
