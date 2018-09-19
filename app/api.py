from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class Client(Resource):
   
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', type=int, help='Client id must be an integer',	location='args', required=True)
        parser.add_argument('client_key', location='args', required=True)
        parser.add_argument('client_secret', location='args', required=True)
        parser.add_argument('status', location='args')
        args = parser.parse_args()
        
        return {'client_id': args['client_id'], 'client_key': args['client_key'], 'client_secret': args['client_secret'], 'status': args['status']}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_id', type=int, help='Client id must be an integer',	location='json', required=True)
        parser.add_argument('client_key', location='json', required=True)
        parser.add_argument('client_secret', location='json', required=True)
        parser.add_argument('status', type=bool, location='json')
        args = parser.parse_args()

        return {'client_id': args['client_id'], 'client_key': args['client_key'], 'client_secret': args['client_secret'], 'status': args['status']}
    
    def put(self):
        return {'client_id': 1, 'client_key': 'CLIENT01', 'client_secret': 'SECRET01', 'status': True}
    
    def delete(self):
        return {'client_id': 1, 'client_key': 'CLIENT01', 'client_secret': 'SECRET01', 'status': True}

class HeaderPeek(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('User-Agent', location='headers')
        parser.add_argument('X-CustomHeader', location='headers')
        args = parser.parse_args()
        return {'headers': args}

api.add_resource(Client, '/client')
api.add_resource(HeaderPeek, '/headers')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)