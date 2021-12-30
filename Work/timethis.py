# timethis.py

import time


def timethis(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        end_time = time.time()
        print('%s.%s %f' % (func.__module__, func.__name__, end_time - start_time))

    return wrapper
