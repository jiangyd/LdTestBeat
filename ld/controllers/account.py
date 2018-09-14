from ld.models.entities import Account
from ld.ext import db
from sqlalchemy import or_, and_
from uuid import uuid4

from ld.utils import exceptions, params


def add_account(account, name, email, is_admin=False):
    if Account.query.filter(and_(or_(Account.account == account,
                                      Account.email == email),
                                  Account.status != Account.StatusDeleted)).count()>0:
        raise exceptions.AccountExist()

    pwd = params.generate_password_hash(str(uuid4()))
    print(pwd)
    new_account = Account(account=account, name=name, email=email, pwd=pwd)
    db.session.add(new_account)
    db.session.commit()


def login(account, passwd):
    pwd = params.generate_password_hash(passwd)
    if Account.query.filter(and_(Account.account == account, Account.pwd == pwd,
                                     Account.status != Account.StatusDeleted)
                                ).count()>0:
        print("login")
    else:
        raise exceptions.LoginFail()


def del_account(account_id):
    if Account.query.filter(Account.id==account_id).count()>0:
        update_account=Account(status=Account.StatusDeleted)
        db.session.add(update_account)
        db.session.commit()
    else:
        raise exceptions.AccountNotFound()


def set_account_pwd(oldpwd,newpwd):
    pass




