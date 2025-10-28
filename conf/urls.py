import findmydevice
from django.conf import settings
from django.urls import path
from django.views.static import serve


assert not settings.PATH_URL, f'App must installed on domain root! Not here: {settings.PATH_URL=}'


# Installed to domain root, without a path prefix
# Just use the default project urls.py
from findmydevice_project.urls import urlpatterns  # noqa

# TODO: Serve from nginx server ;)
urlpatterns.append(path('<path:path>', serve, {'document_root': findmydevice.WEB_PATH}))
