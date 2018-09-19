from flask_restful import Resource,reqparse

class Env(Resource):
    def post(self):
        parse=reqparse.RequestParser()
        parse.add_argument('key',type=str,required=True,location=['json'])
        parse.add_argument('value',type=str,required=True,location=['json'])
        args=parse.parse_args()



