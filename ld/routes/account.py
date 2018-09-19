from flask_restful import Resource,reqparse,marshal_with,fields
from ld.controllers import account as account_ctrl
from ld.ext import api
from flask import Blueprint,request
from ld.utils.params import auth
from ld.utils.auth import authenticate


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
    a={
        "account":fields.String,
        "name":fields.String,
        "email":fields.String
    }


    """
    帐号
    """
    # decorators = [auth.login_required]
    method_decorators = [authenticate]
    @marshal_with(a)
    def post(self,**kwargs):
        print(request)
        print(dir(request))
        print(kwargs)
        # parse=reqparse.RequestParser()
        # parse.add_argument('account',type=str,required=True,location=['json'])
        # parse.add_argument('name',type=str,required=True,location=['json'])
        # parse.add_argument('email',type=str,required=True,location=['json'])
        # args=parse.parse_args()
        # return  account_ctrl.add_account(account=args.account,name=args.name,email=args.email)

    def delete(self):
        parse=reqparse.RequestParser()
        parse.add_argument('account_id',type=int,required=True,location=['args'])
        args=parse.parse_args()
        return account_ctrl.del_account(account_id=args.account_id)

api.add_resource(Account,'/api/account')
api.add_resource(Login,'/api/login')