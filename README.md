<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-traceback.svg?longCache=True)](https://pypi.org/project/django-traceback/)
[![](https://img.shields.io/pypi/v/django-traceback.svg?maxAge=3600)](https://pypi.org/project/django-traceback/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-traceback.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-traceback.py/)

#### Installation
```bash
$ [sudo] pip install django-traceback
```

#### Models
model|`__doc__`
-|-
`Traceback` |Traceback(id, type, value, traceback, path, created_at)

#### Functions
function|`__doc__`
-|-
`django_traceback.utils.save_traceback(path=None)` |save a traceback

#### Examples
```python
from django_traceback.utils import save_traceback
import requests
from apps.celery import celery_app

@celery_app.task
def task():
    try:
        r = requests.get('url')
    except (requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        save_traceback(__file__)
        # init task again
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>