from django.conf import settings
from django.urls import include, path
from django.views.static import serve

import findmydevice


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path(f'{settings.PATH_URL}/', include('findmydevice_project.urls')),
        #
        # TODO: Serve from nginx server ;)
        path(f'{settings.PATH_URL}/<path:path>', serve, {'document_root': findmydevice.WEB_PATH})
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from findmydevice_project.urls import urlpatterns  # noqa

    # TODO: Serve from nginx server ;)
    urlpatterns.append(path('<path:path>', serve, {'document_root': findmydevice.WEB_PATH}))
