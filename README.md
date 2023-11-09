# bookish-octo-engine
devices

## 1st step

Create app and upload devices data with management custom management command.

Device data example:

    {
        "Наклейка": "str",
        "Дом": "str",
        "ip address": "str",
        "Район": "str",
        "model": "str",
        "comment": "str",
        "wtf": "str",
        "netmask": "str",
        "comment_2": "str",
        "serial number": "str",
        "mac": "str",
        "comment_3": "str",
        "Улица": "str",
    }

Start uploading data

    python manage.py upload_devices

with data in "devices.py" file.
