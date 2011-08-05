import os

def media_dirs(apps):
    for app_name in apps:
        try:
            mod = __import__(app_name, {}, {}, [''])
        except ImportError:
            continue

        mediadir = os.path.join(os.path.dirname(mod.__file__),"media")
        if os.path.isdir(mediadir):
            yield app_name.rsplit(".",1)[-1],mediadir


