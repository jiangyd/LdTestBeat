import sys
import os
base_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)


from ld.ext import db

class Account(db.Model):
    StatusDeleted=2
    __tablename__="account"
    __table_args__ = {"extend_existing": True}
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    account=db.Column(db.String(32),nullable=False)
    name=db.Column(db.String(32),nullable=False)
    email=db.Column(db.String(64),nullable=False)
    pwd=db.Column(db.String(255),nullable=False)
    create_time=db.Column(db.Integer)
    update_time=db.Column(db.Integer)
    avatar=db.Column(db.String(255))
    is_admin=db.Column(db.Boolean,default=0) #0:普通成员,1:普通管理员
    status=db.Column(db.Integer,default=1,nullable=False) # 1:ok,2:deleted


class Project(db.Model):
    __tablename__="project"
    __table_args__ = {"extend_existing": True}
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(32),nullable=False)
    baseurl=db.Column(db.String(255))
    desc=db.Column(db.TEXT)
    status=db.Column(db.Integer,default=1,nullable=False) # 1:ok,2:deleted
    create_time = db.Column(db.Integer)
    update_time = db.Column(db.Integer)

    members=db.relationship('Account',secondary="project_member",backref='projects')

class ProjectMember(db.Model):
    __tablename__="project_member"
    __table_args__ = {"extend_existing": True}
    member_id=db.Column(db.Integer,db.ForeignKey('account.id',ondelete='CASCADE'),primary_key=True)
    project_id=db.Column(db.Integer,db.ForeignKey('project.id',ondelete='CASCADE'),primary_key=True)

class ProjectInterface(db.Model):
    __tablename__="interface"
    __table_args__ = {"extend_existing": True}
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(64),nullable=False)
    desc=db.Column(db.String(128))
    method=db.Column(db.String(12),nullable=False)
    api=db.Column(db.TEXT)
    headers=db.Column(db.TEXT)
    Body=db.Column(db.TEXT)
    cookies=db.Column(db.TEXT)
    validator=db.Column(db.TEXT)
    create_time = db.Column(db.Integer)
    update_time = db.Column(db.Integer)
    status=db.Column(db.Integer,default=1,nullable=False) # 1:ok,2:deleted
    create_author_id=db.Column(db.Integer,db.ForeignKey('account.id'))
    update_author_id=db.Column(db.Integer,db.ForeignKey('account.id'))

class Environment(db.Model):
    __tablename__="enviroment"
    __table_args__ = {"extend_existing": True}
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    key=db.Column(db.String(255),nullable=False)
    value=db.Column(db.String(255),nullable=False)
    create_time = db.Column(db.Integer)
    update_time = db.Column(db.Integer)

if __name__=="__main__":
    db.create_all()
