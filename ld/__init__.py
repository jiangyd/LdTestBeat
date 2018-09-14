from flask import Flask
from ld.ext import api,db
from ld.routes.account import account_bp

from ld.ext import config


app=Flask(__name__)







app.config["SQLALCHEMY_DATABASE_URI"]=config["database"]["db_connect"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SQLALCHEMY_ECHO"]=False

db.app=app
db.init_app(app)

app.register_blueprint(account_bp,url_prefix="/api")
api.init_app(app)


