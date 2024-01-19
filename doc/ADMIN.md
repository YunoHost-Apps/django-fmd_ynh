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
