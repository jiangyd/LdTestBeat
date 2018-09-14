from flask import Flask
from ld.ext import api,db
from ld.routes.account import account_bp
from yaml import load,dump
import os


app=Flask(__name__)

config={}

def init_config():
    global config
    base_path=os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    with open(base_path+'/../config/config.yaml') as f:
        config=load(f)
        # print(config)

init_config()

app.config["SQLALCHEMY_DATABASE_URI"]=config.datebase.db_connect
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SQLALCHEMY_ECHO"]=False

db.app=app
db.init_app(app)

app.register_blueprint(account_bp,url_prefix="/api")
api.init_app(app)


