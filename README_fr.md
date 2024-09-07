<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Find My Device pour YunoHost

[![Niveau d’intégration](https://dash.yunohost.org/integration/django-fmd.svg)](https://ci-apps.yunohost.org/ci/apps/django-fmd/) ![Statut du fonctionnement](https://ci-apps.yunohost.org/ci/badges/django-fmd.status.svg) ![Statut de maintenance](https://ci-apps.yunohost.org/ci/badges/django-fmd.maintain.svg)

[![Installer Find My Device avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fmd)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Find My Device rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

Find My Device Server implemented in Python using Django.
Usable for the Andorid App [**FindMyDevice**](https://gitlab.com/Nulide/findmydevice/) by [Nnulide](https://nulide.de/):

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png" alt="Get FindMyDevice on F-Droid" height="80">](https://f-droid.org/packages/de.nulide.findmydevice/)

[![pytest](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh)

[![django-fmd @ PyPi](https://img.shields.io/pypi/v/django-fmd?label=django-fmd%20%40%20PyPi)](https://pypi.org/project/django-fmd/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/pyproject.toml)
[![License GPL V3+](https://img.shields.io/pypi/l/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/LICENSE)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Version incluse :** 0.4.1~ynh1
## Documentations et ressources

- Dépôt de code officiel de l’app : <https://gitlab.com/jedie/django-find-my-device>
- YunoHost Store : <https://apps.yunohost.org/app/django-fmd>
- Signaler un bug : <https://github.com/YunoHost-Apps/django-fmd_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
ou
sudo yunohost app upgrade django-fmd -u https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
