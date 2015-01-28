import os

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as f:
    __version__ = f.read().strip()

try:
    from django.core.exceptions import ImproperlyConfigured
except ImportError:
    ImproperlyConfigured = ImportError

try:
    from .fields import TimedeltaField
    from .helpers import (
        divide, multiply, modulo, 
        parse, nice_repr, 
        percentage, decimal_percentage,
        total_seconds
    )
except (ImportError, ImproperlyConfigured):
    pass