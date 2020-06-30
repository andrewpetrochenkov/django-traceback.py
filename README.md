<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-traceback.svg?maxAge=3600)](https://pypi.org/project/django-traceback/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-traceback.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-traceback.py/actions)

### Installation
```bash
$ [sudo] pip install django-traceback
```

#### Examples
```python
from django_traceback.utils import save_traceback
import requests
from apps.celery import celery_app

@celery_app.task
def task():
    try:
        r = requests.get('url')
    except (requests.exceptions.ConnectionError,...):
        save_traceback(__file__)
        # init task again
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>