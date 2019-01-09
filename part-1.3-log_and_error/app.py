from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from time import strftime
import json

app = Flask(__name__)
api = Api(app)

#################################### 
# Middlewares 
######################################

@app.after_request
def after_request(response):
	app.logger.warning("REQUEST_LOG\t%s", json.dumps({ 'request': request.get_json(), 'response': json.loads(response.data.decode('utf-8')) }))
	return response

#### PERSON CLASS

class Person():

	def __init__(self):
		self.name = None
		self.age = 0
		self.sex = None

#################################### 
# Using flask-restful 
######################################

class PersonResource(Resource):

	person = Person()

	def get(self):
		return self.person.__dict__, 200, { 'Content-Type': 'application/json' }

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', location='json', required=True)
		parser.add_argument('age', location='json', type=int, required=True)
		parser.add_argument('sex', location='json')
		args = parser.parse_args()

		self.person.name = args['name']
		self.person.age = args['age']
		self.person.sex = args['sex']

		return self.person.__dict__, 200, { 'Content-Type': 'application/json' }
	
	def put(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', location='json', required=True)
		parser.add_argument('age', location='json', type=int, required=True)
		parser.add_argument('sex', location='json')
		args = parser.parse_args()

		self.person.name = args['name']
		self.person.age = args['age']
		self.person.sex = args['sex']

		return self.person.__dict__, 200, { 'Content-Type': 'application/json' }
	
	def delete(self):
		self.person = Person()
		return 'Deleted!', 200
	
	def patch(self):
		return 'Not yet implement!', 501

#################################### 
# Flask-restful routes 
######################################

api.add_resource(PersonResource, '/name')


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)