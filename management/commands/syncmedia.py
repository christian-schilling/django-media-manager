from django.core.management.base import BaseCommand
from media_manager import media_dirs

class Command(BaseCommand):
    def handle(self, **kwargs):
        from django.conf import settings
        import os
        if hasattr(settings,"APP_MEDIA_ROOT"):
            for appname,mediadir in media_dirs(settings.INSTALLED_APPS):
                if os.path.isdir(os.path.join(mediadir,appname)):
                    os.system("rsync -avc %s/ %s" % (mediadir,settings.APP_MEDIA_ROOT))
                else:
                    os.system("rsync -avc %s/ %s" % (mediadir,os.path.join(settings.APP_MEDIA_ROOT,appname)))
