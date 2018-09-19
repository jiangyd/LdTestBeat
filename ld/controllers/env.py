from ld.models.entities import Environment

from ld.ext import db

import time

from ld.utils import exceptions

def add_env(key,value):
    if Environment.query.filter(Environment.key==key).first() is not None:
        raise exceptions.EnvKeyIsExist()
    else:
        env=Environment()
