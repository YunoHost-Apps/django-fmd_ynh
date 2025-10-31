import findmydevice
from django.conf import settings
from django.urls import path
from django.views.static import serve
from django_yunohost_integration.yunohost_utils import SSOwatLoginRedirectView


assert not settings.PATH_URL, f'App must installed on domain root! Not here: {settings.PATH_URL=}'


# Installed to domain root, without a path prefix
# Just use the default project urls.py
from findmydevice_project.urls import urlpatterns  # noqa


urlpatterns = [
    path('admin/sso-login/', SSOwatLoginRedirectView.as_view(), name='ssowat-login'),
    #
    *urlpatterns,
    #
    # TODO: Serve from nginx server:
    path('<path:path>', serve, {'document_root': findmydevice.WEB_PATH}),
]
