from werkzeug.security import generate_password_hash,check_password_hash

from flask_httpauth import HTTPTokenAuth

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from ld.ext import config

auth=HTTPTokenAuth(scheme='Bearer')


serializer = Serializer(config["security"]["SECRET_KEY"], expires_in=1800)


def encrypt(password):
    return generate_password_hash(password)


def check_password(pwd1,pwd2):
    #pwd1 in database
    #pwd2 from request params
    print(pwd1,pwd2)
    return check_password_hash(pwd1,pwd2)


def create_token(data):
    """生成token"""
    token = serializer.dumps(data)
    return token.decode("utf-8")

