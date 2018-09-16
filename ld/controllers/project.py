from ld.models.entities import Project
from sqlalchemy import and_, or_
from ld.ext import db
from ld.utils import exceptions
import time


def add_project(name, baseurl, desc):
    projectinfo = Project.query.filter(Project.name == name, Project.status != Project.StatusDeleted).first()
    if projectinfo is None:
        projectinfo = Project(name=name, baseurl=baseurl, desc=desc, create_time=int(time.time()))
        db.session.add(projectinfo)
        db.session.commit()
    else:
        raise exceptions.ProjectIsExist()


def edit_project(project_id, name, baseurl, desc):
    p = Project.query.filter(Project.id == project_id, Project.status != Project.StatusDeleted).first()
    if p is None:
        raise exceptions.ProjectNotFound()
    # .filter(Project.id!=project_id)排除本身
    projectinfo = Project.query.filter(Project.id != project_id).filter(
        and_(Project.name == name, Project.status != Project.StatusDeleted)).first()

    if projectinfo is None:
        p.name = name
        p.baseurl = baseurl
        p.desc = desc
        p.update_time = int(time.time())
        db.session.add(p)
        db.session.commit()
    else:
        raise exceptions.ProjectIsExist()


def del_project(project_id):
    p = Project.query.filter(and_(Project.id == project_id, Project.status != Project.StatusDeleted)).first()
    if p is None:
        raise exceptions.ProjectNotFound()
    else:
        p.status = Project.StatusDeleted
        db.session.add(p)
        db.session.commit()


def get_project(project_id):
    p = Project.query.filter(and_(Project.id == project_id, Project.status != Project.StatusDeleted)).first()
    if p is None:
        raise exceptions.ProjectNotFound()
    else:
        return p.to_dict()


def get_list_project(page,pagesize):
    p=Project.query.filter(Project.status!=Project.StatusDeleted).paginate(page=page,per_page=pagesize)
    print(p.total)
    print(p.items)
    print(p.pages)
    print(dir(p))
    print(p)
    data=[]
    for i in p.items:
        data.append(i.to_dict())
    return {"pages":p.pages,"data":data,"total":p.total}
