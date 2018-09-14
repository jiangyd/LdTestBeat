from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api

from ld.utils.exceptions import except_dict

db=SQLAlchemy()

api=Api(errors=except_dict)
