from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api

from yaml import load,dump

import os

from ld.utils.exceptions import except_dict

import redis




def init_config():
    base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(base_path)
    with open(base_path+'/../config/config.yaml') as f:
        config=load(f)
        return config

config=init_config()

db=SQLAlchemy()

api=Api(errors=except_dict)


pool=redis.ConnectionPool(host=config["redis"]["host"],port=config["redis"]["port"],password=config["redis"]["password"])
r=redis.Redis(connection_pool=pool)

