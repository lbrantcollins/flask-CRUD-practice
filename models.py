# Flask modules:
# import everything from peewee
from peewee import *

# pythod modules:
import datetime

# connects to database
DATABASE = SqliteDatabase('dogs.sqlite')

# set up the Dog model
# when we initialize it, this will be of class model
class Dog(Model):
	name = CharField()
	owner = CharField()
	age = SmallIntegerField()
	breed = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

# this gets run from app.py when the app starts up
def initialize():
	# open connection to databse
	DATABASE.connect() 
	# create two tables: User and Dog 
	# (with columns as defined above)
	# safe=True prevents overwriting existing tables
	DATABASE.create_tables([Dog], safe=True)
	print("DOG TABLE CREATED")
	# disconnect from db after writing (to save on resources)
	DATABASE.close()




