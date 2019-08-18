from flask import Flask, g  

# import Dog model
import models 

# dog.py Flask CRUD routes
from api.dog import dog

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__, static_url_path="", static_folder="static")

# sets up the blueprint (controller) in the server file
app.register_blueprint(dog)

# connect to database before each query/request
@app.before_request # given to us by flask @
def before_request():
	"""Connect to the database before each request"""
	g.db = models.DATABASE
	g.db.connect()

# close connection to database after each query/request
@app.after_request # given to us by flask @
def after_request(response):
	"""Close connection to the database after each request"""
	g.db = models.DATABASE
	g.db.close()
	return response

# The default URL ends in / ("my-website.com/").
# this is a get route (default is GET)
@app.route('/')  
def index():  # can name this method whatever you like
    return 'hello world' # like "res.send" in express

# Run the app when the program starts!
if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT) # like app.listen in express



