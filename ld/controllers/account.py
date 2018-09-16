from ld.models.entities import Account
from ld.ext import db
from sqlalchemy import or_, and_
from uuid import uuid4
import time
from ld.utils import exceptions, params


def add_account(account, name, email, is_admin=False):
    if Account.query.filter(and_(or_(Account.account == account,
                                      Account.email == email),
                                  Account.status != Account.StatusDeleted)).count()>0:
        raise exceptions.AccountExist()

    # pwd = params.generate_password_hash(str(uuid4()))
    pwd = params.generate_password_hash("123456")
    new_account = Account(account=account, name=name, email=email, pwd=pwd)
    db.session.add(new_account)
    db.session.commit()


def login(account, passwd):
    userinfo=Account.query.filter(and_(Account.account == account, Account.status != Account.StatusDeleted)).first()
    if userinfo is None:
        raise exceptions.LoginFail()
    else:
        print("cc")
        if params.check_password(userinfo.pwd,passwd):
            token=params.create_token({"account":account,"passwd":userinfo.pwd,"time":int(time.time())})
            return token
        else:
            raise exceptions.LoginFail()



def del_account(account_id):

    account=Account.query.filter(and_(Account.id==account_id,Account.status!=Account.StatusDeleted)).first()
    if account is None:
        raise exceptions.AccountNotFound()
    else:
        account.status=Account.StatusDeleted
        db.session.add(account)
        db.session.commit()

def set_account_pwd(account_id,oldpwd,newpwd):
    account = Account.query.filter(and_(Account.id == account_id, Account.status != Account.StatusDeleted)).first()
    if params.check_password(account.pwd,oldpwd):
        account.pwd=params.encrypt(newpwd)
        db.session.add(account)
        db.session.commit()
    else:
        raise exceptions.OldPwdIsError()





