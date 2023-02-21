from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, TextAreaField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, InputRequired
from forms.formData import incidents, countries, locations
from datetime import datetime


class DataForm(FlaskForm):
	country = SelectField('Country', validators=[DataRequired(message='Please choose a country')], choices=countries)
	incident = SelectField('Incident', validators=[DataRequired(message='Please choose an incident')], choices=incidents)
	incident_date = DateTimeField('Incident Date', validators=[InputRequired(message='Please enter a date')],
	                          default=datetime.today())
	location = SelectField('Location', validators=[DataRequired(message='Please choose a location')], choices=locations)
	# Using Inputrequired otherwise it won't accept 0 (zero) as a valid amount
	casualties = IntegerField('Casualties', validators=[InputRequired(message='Please enter amount')])
	injured = IntegerField('injured', validators=[InputRequired(message='Please enter amount')])











