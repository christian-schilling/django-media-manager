# -*- coding: utf-8 -*-
from django.http import Http404
from django.conf import settings
import django.views.static
import re
from media_manager import media_dirs

class MediaServeMiddleware(object):
    def process_response(self, request, response):
        if not hasattr(settings,"SITE_MEDIA_PREFIX"):
            return response

        for appname,mediadir in media_dirs(settings.INSTALLED_APPS):
            exp = "(%s%s)(.*)" % (settings.APP_MEDIA_PREFIX,appname)
            result = re.match(exp,request.path)
            if result:
                base,path = result.groups()
                return django.views.static.serve(request, path, mediadir)

        exp = "(%s)(.*)" % settings.SITE_MEDIA_PREFIX
        result = re.match(exp,request.path)
        if result:
            base,path = result.groups()
            return django.views.static.serve(request, path, settings.SITE_MEDIA_ROOT)

        return response


