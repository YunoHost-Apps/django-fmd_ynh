<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# django-fmd untuk YunoHost

[![Tingkat integrasi](https://dash.yunohost.org/integration/django-fmd.svg)](https://ci-apps.yunohost.org/ci/apps/django-fmd/) ![Status kerja](https://ci-apps.yunohost.org/ci/badges/django-fmd.status.svg) ![Status pemeliharaan](https://ci-apps.yunohost.org/ci/badges/django-fmd.maintain.svg)

[![Pasang django-fmd dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fmd)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang django-fmd secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

Find My Device Server implemented in Python using Django.
Usable for the Andorid App [**FindMyDevice**](https://gitlab.com/Nulide/findmydevice/) by [Nnulide](https://nulide.de/):

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png" alt="Get FindMyDevice on F-Droid" height="80">](https://f-droid.org/packages/de.nulide.findmydevice/)

[![pytest](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh)

[![django-fmd @ PyPi](https://img.shields.io/pypi/v/django-fmd?label=django-fmd%20%40%20PyPi)](https://pypi.org/project/django-fmd/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/pyproject.toml)
[![License GPL V3+](https://img.shields.io/pypi/l/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/LICENSE)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versi terkirim:** 0.4.1~ynh1
## Dokumentasi dan sumber daya

- Dokumentasi pengguna resmi: <https://gitlab.com/jedie/django-find-my-device>
- Dokumentasi admin resmi: <https://github.com/YunoHost-Apps/django-fmd_ynh>
- Depot kode aplikasi hulu: <https://github.com/YunoHost-Apps/django-fmd_ynh>
- Gudang YunoHost: <https://apps.yunohost.org/app/django-fmd>
- Laporkan bug: <https://github.com/YunoHost-Apps/django-fmd_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
atau
sudo yunohost app upgrade django-fmd -u https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
