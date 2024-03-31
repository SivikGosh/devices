# bookish-octo-engine
devices

build dev compose:
- docker compose -f .\compose_dev.yaml -p dev_devices up --build -d

build prod compose:
- docker compose -f .\compose.yaml -p devices up --build -d

dumpdata:
- -Xutf8 dumpdata --natural-foreign -e contenttypes -e auth.Permission -o dump.json

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

with list of objects with name "data" in "devices.py" file on the app directory.

## 2nd step

Move comment columns to foreign model. Add manage command for moving data.

    python manage.py move_comments
