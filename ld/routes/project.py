from flask_restful import Resource,reqparse
from ld.controllers import project as project_ctrl
from ld.ext import api
from flask import Blueprint
from ld.utils.params import auth


project_bp=Blueprint("project",__name__)






class Project(Resource):
    """
    项目
    """
    # decorators = [auth.login_required]
    def post(self):
        parse=reqparse.RequestParser()
        parse.add_argument('name',type=str,required=True,location=['json'])
        parse.add_argument('baseurl',type=str,required=True,location=['json'])
        parse.add_argument('desc',type=str,required=True,location=['json'])
        args=parse.parse_args()
        return  project_ctrl.add_project(name=args.name,baseurl=args.baseurl,desc=args.desc)

    def put(self):
        parse=reqparse.RequestParser()
        parse.add_argument('project_id', type=int, required=True, location=['json'])
        parse.add_argument('name', type=str, required=True, location=['json'])
        parse.add_argument('baseurl', type=str, required=True, location=['json'])
        parse.add_argument('desc', type=str, required=True, location=['json'])
        args=parse.parse_args()
        return project_ctrl.edit_project(project_id=args.project_id,name=args.name,baseurl=args.baseurl,desc=args.desc)
    def delete(self):
        parse=reqparse.RequestParser()
        parse.add_argument('project_id',type=int,required=True,location=['args'])
        args=parse.parse_args()
        return project_ctrl.del_project(project_id=args.project_id)

    def get(self):
        parse=reqparse.RequestParser()
        parse.add_argument('project_id',type=int,required=True,location=['args'])
        args=parse.parse_args()
        return project_ctrl.get_project(project_id=args.project_id)

class ProjectList(Resource):
    def get(self):
        parse=reqparse.RequestParser()
        parse.add_argument('page',type=int,required=True,location=['args'])
        parse.add_argument('pagesize',type=int,location=['args'])
        args=parse.parse_args()
        return

api.add_resource(Project,'/api/project')
