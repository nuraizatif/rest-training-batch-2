from app import db
from flask_restful import fields

class Person(db.Model):
	__tablename__ = "person"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=True, nullable=False)
	age = db.Column(db.Integer, nullable=True)
	sex = db.Column(db.String(10), nullable=False)

	response_fields = {
		'id': fields.Integer,
		'name': fields.String,
		'age': fields.String,
		'sex': fields.Boolean
	}

	def __repr__(self):
		return '<Person %r>' % self.id
