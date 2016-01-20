"""
This module includes helper methods and decorators that don't fit
into any particular grouping elsewhere.
"""

import os
import glob
import sys
from functools import wraps

STATIC_DIR = os.path.join(os.path.dirname(sys.argv[0]), 'static', 'gen')


def use_generated_assests(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        css_files = glob.glob(os.path.join(STATIC_DIR, '*.css'))
        kwargs['css'] = [os.path.split(item)[1] for item in css_files]
        js_files = glob.glob(os.path.join(STATIC_DIR, '*.js'))
        kwargs['js'] = [os.path.split(item)[1] for item in js_files]

        print(kwargs)
        return f(*args, **kwargs)

    return wrapper
