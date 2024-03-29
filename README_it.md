<!--
N.B.: Questo README è stato automaticamente generato da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON DEVE essere modificato manualmente.
-->

# django-fmd per YunoHost

[![Livello di integrazione](https://dash.yunohost.org/integration/django-fmd.svg)](https://dash.yunohost.org/appci/app/django-fmd) ![Stato di funzionamento](https://ci-apps.yunohost.org/ci/badges/django-fmd.status.svg) ![Stato di manutenzione](https://ci-apps.yunohost.org/ci/badges/django-fmd.maintain.svg)

[![Installa django-fmd con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fmd)

*[Leggi questo README in altre lingue.](./ALL_README.md)*

> *Questo pacchetto ti permette di installare django-fmd su un server YunoHost in modo semplice e veloce.*  
> *Se non hai YunoHost, consulta [la guida](https://yunohost.org/install) per imparare a installarlo.*

## Panoramica

Find My Device Server implemented in Python using Django.
Usable for the Andorid App [**FindMyDevice**](https://gitlab.com/Nulide/findmydevice/) by [Nnulide](https://nulide.de/):

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png" alt="Get FindMyDevice on F-Droid" height="80">](https://f-droid.org/packages/de.nulide.findmydevice/)

[![pytest](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh)

[![django-fmd @ PyPi](https://img.shields.io/pypi/v/django-fmd?label=django-fmd%20%40%20PyPi)](https://pypi.org/project/django-fmd/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/pyproject.toml)
[![License GPL V3+](https://img.shields.io/pypi/l/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/LICENSE)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versione pubblicata:** 0.3.2~ynh1
## Documentazione e risorse

- Sito web ufficiale dell’app: <https://gitlab.com/jedie/django-find-my-device>
- Repository upstream del codice dell’app: <https://gitlab.com/jedie/django-find-my-device>
- Store di YunoHost: <https://apps.yunohost.org/app/django-fmd>
- Segnala un problema: <https://github.com/YunoHost-Apps/django-fmd_ynh/issues>

## Informazioni per sviluppatori

Si prega di inviare la tua pull request alla [branch di `testing`](https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing).

Per provare la branch di `testing`, si prega di procedere in questo modo:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
o
sudo yunohost app upgrade django-fmd -u https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
```

**Maggiori informazioni riguardo il pacchetto di quest’app:** <https://yunohost.org/packaging_apps>
