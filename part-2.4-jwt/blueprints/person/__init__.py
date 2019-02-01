import random, logging

#### PERSON CLASS

class Person():

	def __init__(self):
		self.reset()

	def reset(self):
		self.id = 0
		self.name = None
		self.age = 0
		self.sex = None
		
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'age': self.age,
			'sex': self.sex,
		}

class Persons():

	persons = []

	def __init__(self):
		for i in range(15):
			person = Person()
			person.id = i
			person.name = "Person ke %d" % (i)
			person.age = random.randrange(1,80)
			person.sex = random.choice([ "male", "female" ])
			self.persons.append(person.serialize())
	
	def get_list(self):
		return self.persons
	
	def add(self, str_serialized):
		self.persons.append(str_serialized)
	
	def get_one(self, id):
		for v in enumerate(self.persons):
			if v['id'] == id:
				return v
		return None
	
	def edit_one(self, id, name, age, sex):
		for k,v in enumerate(self.persons):
			if int(v['id']) == int(id):
				person = Person()
				person.id = id
				person.name = name
				person.age = age
				person.sex = sex
				self.persons[k] = person.serialize()
				return person
		return None
	
	def delete_one(self, id):
		for k,v in enumerate(self.persons):
			if int(v['id']) == int(id):
				self.persons.pop(k)
				return True
		return None