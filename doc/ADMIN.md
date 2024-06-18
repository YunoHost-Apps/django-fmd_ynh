## Settings and upgrades

Almost everything related to django-fmd's configuration is handled in a `"../conf/settings.py"` file.
You can edit the file `/opt/yunohost/django-fmd/local_settings.py` to enable or disable features.

Test sending emails:

```bash
ssh admin@yourdomain.tld
root@yunohost:~# cd /opt/yunohost/django-fmd/
root@yunohost:/opt/yunohost/django-fmd# source venv/bin/activate
(venv) root@yunohost:/opt/yunohost/django-fmd# ./manage.py sendtestemail --admins
```

Background info: Error mails are send to all [settings.ADMINS](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-ADMINS). By default the YunoHost admin is inserted here.
To check current ADMINS run:

```bash
(venv) root@yunohost:/opt/yunohost/django-fmd# ./manage.py sendtestemail --admins
```

If you prefere to send error emails to a extrnal email address, just do something like this:

```bash
echo "ADMINS = (('Your Name', 'example@domain.tld'),)" >> /opt/yunohost/django-fmd/local_settings.py
```

To check the effective settings, run this:

```bash
(venv) root@yunohost:/opt/yunohost/django-fmd# ./manage.py diffsettings
```


## Development CLI

e.g.:

[comment]: <> (✂✂✂ auto generated help start ✂✂✂)
```
Usage: ./dev-cli.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --help      Show this message and exit.                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────╮
│ check-code-style            Check code style by calling darker + flake8                          │
│ diffsettings                Run "diffsettings" manage command against a "local_test" YunoHost    │
│                             installation.                                                        │
│ fix-code-style              Fix code style of all your_cool_package source code files via darker │
│ install                     Run pip-sync and install 'django_fmd_ynh' via pip as editable.       │
│ local-test                  Build a "local_test" YunoHost installation and start the Django dev. │
│                             server against it.                                                   │
│ mypy                        Run Mypy (configured in pyproject.toml)                              │
│ publish                     Build and upload this project to PyPi                                │
│ safety                      Run safety check against current requirements files                  │
│ test                        Compile YunoHost files and run Django unittests                      │
│ tox                         Run tox                                                              │
│ update                      Update "requirements*.txt" dependencies files                        │
│ update-test-snapshot-files  Update all test snapshot files (by remove and recreate all snapshot  │
│                             files)                                                               │
│ version                     Print version and exit                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
```
[comment]: <> (✂✂✂ auto generated help end ✂✂✂)
