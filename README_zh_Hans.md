<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 上的 Find My Device

[![集成程度](https://dash.yunohost.org/integration/django-fmd.svg)](https://ci-apps.yunohost.org/ci/apps/django-fmd/) ![工作状态](https://ci-apps.yunohost.org/ci/badges/django-fmd.status.svg) ![维护状态](https://ci-apps.yunohost.org/ci/badges/django-fmd.maintain.svg)

[![使用 YunoHost 安装 Find My Device](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django-fmd)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 Find My Device。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

Find My Device Server implemented in Python using Django.
Usable for the Andorid App [**FindMyDevice**](https://gitlab.com/Nulide/findmydevice/) by [Nnulide](https://nulide.de/):

[<img src="https://fdroid.gitlab.io/artwork/badge/get-it-on.png" alt="Get FindMyDevice on F-Droid" height="80">](https://f-droid.org/packages/de.nulide.findmydevice/)

[![pytest](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/pytest.yml) [![YunoHost apps package linter](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml/badge.svg)](https://github.com/YunoHost-Apps/django-fmd_ynh/actions/workflows/package_linter.yml) [![Coverage Status on codecov.io](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh/branch/master/graph/badge.svg)](https://codecov.io/gh/YunoHost-Apps/django-fmd_ynh)

[![django-fmd @ PyPi](https://img.shields.io/pypi/v/django-fmd?label=django-fmd%20%40%20PyPi)](https://pypi.org/project/django-fmd/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/pyproject.toml)
[![License GPL V3+](https://img.shields.io/pypi/l/django-fmd)](https://gitlab.com/jedie/django-find-my-device/-/blob/main/LICENSE)

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**分发版本：** 0.4.1~ynh1
## 文档与资源

- 官方用户文档： <https://gitlab.com/jedie/django-find-my-device>
- 官方管理文档： <https://github.com/YunoHost-Apps/django-fmd_ynh>
- 上游应用代码库： <https://github.com/YunoHost-Apps/django-fmd_ynh>
- YunoHost 商店： <https://apps.yunohost.org/app/django-fmd>
- 报告 bug： <https://github.com/YunoHost-Apps/django-fmd_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
或
sudo yunohost app upgrade django-fmd -u https://github.com/YunoHost-Apps/django-fmd_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>
