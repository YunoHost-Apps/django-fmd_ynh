<!--
NOTA: Este README foi creado automáticamente por <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON debe editarse manualmente.
-->

# Find My Device para YunoHost

[![Nivel de integración](https://dash.yunohost.org/integration/django-fmd.svg)](https://ci-apps.yunohost.org/ci/apps/django-fmd/) ![Estado de funcionamento](https://ci-apps.yunohost.org/ci/badges/django-fmd.status.svg) ![Estado de mantemento](https://ci-apps.yunohost.org/ci/badges/django-fmd.maintain.svg)

[![Instalar Find My Device con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fmd)

*[Le este README en outros idiomas.](./ALL_README.md)*

> *Este paquete permíteche instalar Find My Device de xeito rápido e doado nun servidor YunoHost.*  
> *Se non usas YunoHost, le a [documentación](https://yunohost.org/install) para saber como instalalo.*

## Vista xeral

Find My Device Server implemented in Python using Django.
Usable for the Andorid App [**FindMyDevice**](https://gitlab.com/Nulide/findmydevice/) by [Nnulide](https://nulide.de/):

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png" alt="Get FindMyDevice on F-Droid" height="80">](https://f-droid.org/packages/de.nulide.findmydevice/)

[![pytest](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh)

[![django-fmd @ PyPi](https://img.shields.io/pypi/v/django-fmd?label=django-fmd%20%40%20PyPi)](https://pypi.org/project/django-fmd/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/pyproject.toml)
[![License GPL V3+](https://img.shields.io/pypi/l/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/LICENSE)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versión proporcionada:** 0.4.1~ynh1
## Documentación e recursos

- Repositorio de orixe do código: <https://gitlab.com/jedie/django-find-my-device>
- Tenda YunoHost: <https://apps.yunohost.org/app/django-fmd>
- Informar dun problema: <https://github.com/YunoHost-Apps/django-fmd_ynh/issues>

## Info de desenvolvemento

Envía a túa colaboración á [rama `testing`](https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing).

Para probar a rama `testing`, procede deste xeito:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
ou
sudo yunohost app upgrade django-fmd -u https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
```

**Máis info sobre o empaquetado da app:** <https://yunohost.org/packaging_apps>
