#!/usr/bin/env python3
"""
    urls.py
    ~~~~~~~
"""
from django.conf import settings
from django.urls import include, path
from django.views.static import serve

import findmydevice


if settings.PATH:
    # settings.PATH is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH":
    urlpatterns = [
        path(f'{settings.PATH}/', include('findmydevice_project.urls')),
        #
        # TODO: Serve from nginx server ;)
        path(f'{settings.PATH}/<path:path>', serve, {'document_root': findmydevice.WEB_PATH})
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from findmydevice_project.urls import urlpatterns  # noqa

    # TODO: Serve from nginx server ;)
    urlpatterns.append(path('<path:path>', serve, {'document_root': findmydevice.WEB_PATH}))
