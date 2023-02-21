from flask_restful import fields
from datetime import datetime
import random
from dataclasses import dataclass

resource_fields = {
	'country':   fields.String,
	'incident':   fields.String,
	'location':   fields.String,
	'casualties':   fields.Integer,
	'injured':   fields.Integer,
}


@dataclass(kw_only=False)
class Data:
	country: str
	incident: str
	location: str
	casualties: int
	injured: int
	created: str = datetime.utcnow()
	id: int = random.randint(1000000, 10000000)


def data_json(dt: Data):
	return {
		'id': dt.id,
		'country': dt.country,
		'incident': dt.incident,
		'location': dt.location,
		'casualties': dt.casualties,
		'injured': dt.injured,
		'created': dt.created
	}


class User:
	def __init__(self, email, password):
		self.id = random.randint(1000000, 10000000)
		self.email = email
		self.password = password
		self.created = datetime.utcnow()

	def user_json(self):
		return {
			'id': self.id,
			'username': self.email[:self.email.index("@")],
			'email': self.email,
			'password': self.password,
			'created': self.created
		}