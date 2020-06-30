__all__ = ['save_traceback']


import sys
from traceback import format_tb


from .models import Traceback

"""
from django_traceback.utils import save_traceback

try:
    ...
except:
    save_traceback(__file__)
"""


def get_full_class_name(cls):
    module = cls.__module__
    if module is None:
        return cls.__name__
    return module + '.' + cls.__name__


def save_traceback(path=None):
    """save a traceback"""
    exctype, value, tb = sys.exc_info()
    Traceback(
        type=get_full_class_name(exctype),
        value=value if value else '',
        traceback='\n'.join(format_tb(tb)),
        path=path
    ).save()
