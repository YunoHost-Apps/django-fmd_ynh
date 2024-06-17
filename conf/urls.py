from django.conf import settings
from django.urls import include, path
from django.views.static import serve
from django.views.generic import RedirectView

import findmydevice

if settings.PATH_URL:
    # settings.PATH_URL is __PATH__
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        #
        # TODO: Serve from nginx server ;)
        path(f'{settings.PATH}/<path:path>', serve, {'document_root': findmydevice.WEB_PATH}),
        #
        path('', RedirectView.as_view(url=f'{settings.PATH_URL}/')),
        path(f'{settings.PATH_URL}/', include('findmydevice_project.urls')),
    ]
else:
    # Installed to domain root, without a path prefix
    # Just use the default project urls.py
    from findmydevice_project.urls import urlpatterns  # noqa

    # TODO: Serve from nginx server ;)
    urlpatterns.append(path('<path:path>', serve, {'document_root': findmydevice.WEB_PATH}))
