# model
from models import Dog
# modules
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# bluepring
dog = Blueprint('dogs', 'dog', url_prefix='/api/v1')

# CREATE route (create one)
@dog.route('/', methods=['POST'])
#########################################
def createDog():
	name = request.json['name']
	owner = request.json['owner']
	age = request.json['age']
	breed = request.json['breed']

	payload = {
		"name": name,
		"owner": owner,
		"age": age,
		"breed": breed
	}

	dog = Dog.create(**payload)

	print(model_to_dict(dog))
	
	return jsonify(model_to_dict(dog))


# READ route (read all)
@dog.route('/', methods=['GET'])
#########################################
def getDogs():
	selected_dogs = []
	for dog in Dog.select().where(Dog.breed == "cat"):
		selected_dogs.append(model_to_dict(dog))
		print(model_to_dict(dog))

	return jsonify(selected_dogs)


# READ route (read one)
@dog.route('/3', methods=['GET'])
#########################################
def getDog():
	found_dog = Dog.get_by_id(3)
	# found_dog = Dog.get(Dog.id == 3)

	print(model_to_dict(found_dog))

	return jsonify(model_to_dict(found_dog))


# # READ route (read one and just return the name)
# @dog.route('/1', methods=['GET'])
#########################################
# def getDog():
# 	found_dog = Dog.get(Dog.id == 1)
# 	dog_name = found_dog.name

# 	print(dog_name)

# 	return jsonify(dog_name)

# DELETE route
@dog.route('/', methods=['DELETE'])
#########################################
def deleteDogs():
	selected_dogs = []
	for dog in Dog.select().where(Dog.breed == "cat"):
		selected_dogs.append(model_to_dict(dog))
		print(model_to_dict(dog))
	
	query = Dog.delete().where(Dog.breed == "cat")
	print(query.execute(), "rows deleted")

	return jsonify(selected_dogs)

# UPDATE route
@dog.route('/2', methods=['PUT'])
#########################################
def updateDog():
	found_dog = Dog.get_by_id(2)

	name = found_dog.name
	owner = found_dog.owner
	age = request.json['age']
	breed = found_dog.breed

	payload = {
		"name": name,
		"owner": owner,
		"age": age,
		"breed": breed
	}
	print("payload: ", payload)

	num_updated = Dog.update(**payload).where(Dog.id == 2).execute()
	print("number of dogs updated", num_updated)

	found_dog = Dog.get_by_id(2)
	
	return jsonify(model_to_dict(found_dog))







