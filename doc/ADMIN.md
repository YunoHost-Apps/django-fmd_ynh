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
usage: ./dev-cli.py [-h]
                    {coverage,install,lint,mypy,nox,pip-audit,publish,test,update,update-test-snapshot-files,version}



╭─ options ─────────────────────────────────────────────────────────────────────────────────────────╮
│ -h, --help        show this help message and exit                                                 │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ subcommands ─────────────────────────────────────────────────────────────────────────────────────╮
│ {coverage,install,lint,mypy,nox,pip-audit,publish,test,update,update-test-snapshot-files,version} │
│     coverage      Run tests and show coverage report.                                             │
│     install       Install requirements and 'django_fmd_ynh' via pip as editable.                  │
│     lint          Check/fix code style by run: "ruff check --fix"                                 │
│     mypy          Run Mypy (configured in pyproject.toml)                                         │
│     nox           Run nox                                                                         │
│     pip-audit     Run pip-audit check against current requirements files                          │
│     publish       Build and upload this project to PyPi                                           │
│     test          Run unittests                                                                   │
│     update        Update "requirements*.txt" dependencies files                                   │
│     update-test-snapshot-files                                                                    │
│                   Update all test snapshot files (by remove and recreate all snapshot files)      │
│     version       Print version and exit                                                          │
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```
[comment]: <> (✂✂✂ auto generated help end ✂✂✂)
