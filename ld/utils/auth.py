from functools import wraps
from ld.utils import exceptions
from ld.ext import r

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(dir(func))
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
        # raise exceptions.LoginFail()
    return wrapper
