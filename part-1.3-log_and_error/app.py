from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from time import strftime
import json, logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
	
#################################### 
# Flask-RESTFul define custom error
####################################

## catch 404 default error with catch_all_404s=True
api = Api(app, catch_all_404s=True)

#################################### 
# Middlewares 
######################################

@app.after_request
def after_request(response):
	if request.method=='GET':
		app.logger.warning("REQUEST_LOG\t%s", json.dumps({ 'request': request.args.to_dict(), 'response': json.loads(response.data.decode('utf-8')) }))
	else:
		app.logger.warning("REQUEST_LOG\t%s", json.dumps({ 'request': request.get_json(), 'response': json.loads(response.data.decode('utf-8')) }))
	return response

#### PERSON CLASS

class Person():

	def __init__(self):
		self.reset()

	def reset(self):
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
		self.person.reset()
		return 'Deleted', 200
	
	def patch(self):
		return 'Not yet implement', 501

#################################### 
# Flask-restful routes 
######################################

api.add_resource(PersonResource, '/name')


if __name__ == '__main__':

	## define log format and create a rotating log with max size of 10MB and max backup up to 10 files
	formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
	log_handler = RotatingFileHandler("%s/%s" % (app.root_path, 'storage/log/app.log'), maxBytes=10000, backupCount=10)
	log_handler.setLevel(logging.INFO)
	log_handler.setFormatter(formatter)
	app.logger.addHandler(log_handler)

	## if you want to jsonify 500 error, you cannot. But you can set debug=False
	app.run(debug=False, host='0.0.0.0', port=5000)