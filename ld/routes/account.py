from flask_restful import Resource,reqparse
from ld.controllers import account as account_ctrl
from ld.ext import api
from flask import Blueprint
from ld.utils.params import auth


account_bp=Blueprint("account",__name__)



@auth.verify_token
def verify_token(token):
    """验证token"""

    pass

class Login(Resource):
    """
    登录
    """
    def post(self):
        parse=reqparse.RequestParser()
        parse.add_argument('account',type=str,required=True,location=['json'])
        parse.add_argument('password',type=str,required=True,location=['json'])
        args=parse.parse_args()
        return account_ctrl.login(account=args.account,passwd=args.password)

class Account(Resource):
    """
    帐号
    """
    decorators = [auth.login_required]
    def post(self):
        parse=reqparse.RequestParser()
        parse.add_argument('account',type=str,required=True,location=['json'])
        parse.add_argument('name',type=str,required=True,location=['json'])
        parse.add_argument('email',type=str,required=True,location=['json'])
        args=parse.parse_args()
        return  account_ctrl.add_account(account=args.account,name=args.name,email=args.email)

    def delete(self):
        parse=reqparse.RequestParser()
        parse.add_argument('account_id',type=int,required=True,location=['args'])
        args=parse.parse_args()
        return account_ctrl.del_account(account_id=args.account_id)

api.add_resource(Account,'/api/account')
api.add_resource(Login,'/api/login')