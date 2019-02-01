import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import jwt_required

from . import *

bp_person = Blueprint('person', __name__)
api = Api(bp_person)

#################################### 
# Using flask-restful 
######################################

class PersonResource(Resource):

	persons = Persons()

	def __init__(self):
		pass
	
	@jwt_required
	def get(self, id=None):
		if id is None:
			return self.persons.get_list(), 200, { 'Content-Type': 'application/json' }
		else:
			for person in self.persons.get_list():
				logging.error('VREKELE %s' % (person))	
				if person['id'] == int(id):
					return person, 200, { 'Content-Type': 'application/json' }
			
			return {'status': 'NOT_FOUND', 'message': 'Person not found'}, 404, { 'Content-Type': 'application/json' }

	@jwt_required
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', location='json', required=True)
		parser.add_argument('age', location='json', type=int, required=True)
		parser.add_argument('sex', location='json')
		args = parser.parse_args()

		person = Person()
		person.id = len(self.persons.get_list()) + 1
		person.name = args['name']
		person.age = args['age']
		person.sex = args['sex']

		self.persons.add(person.serialize())

		return person.__dict__, 200, { 'Content-Type': 'application/json' }
	
	@jwt_required
	def put(self, id):
		parser = reqparse.RequestParser()
		parser.add_argument('name', location='json', required=True)
		parser.add_argument('age', location='json', type=int, required=True)
		parser.add_argument('sex', location='json')
		args = parser.parse_args()

		result = self.persons.edit_one(id, args['name'], args['age'], args['sex'])

		if result is not None:
			return result.__dict__, 200, { 'Content-Type': 'application/json' }
		else:
			return {'status': 'NOT_FOUND', 'message': 'Person not found'}, 404, { 'Content-Type': 'application/json' }
	
	@jwt_required
	def delete(self, id):
		result = self.persons.delete_one(id)
		if result is not None:
			return 'deleted', 200, { 'Content-Type': 'application/json' }
		else:
			return {'status': 'NOT_FOUND', 'message': 'Person not found'}, 404, { 'Content-Type': 'application/json' }

### Routes

api.add_resource(PersonResource, '', '/<id>')
