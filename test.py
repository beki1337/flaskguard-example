from FlaskGuard import RequestParameter, FlaskGuard

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)


users = []
messages = []

class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def serialize(self):
        return {'id': self.id, 'name': self.name}

class Message:
    def __init__(self, id, text, user_id):
        self.id = id
        self.text = text
        self.user_id = user_id

    def serialize(self):
        return {'id': self.id, 'text': self.text, 'user_id': self.user_id}
    

name_key     = RequestParameter("name", str, 0, 20)
age_key      = RequestParameter("age", int, 0, 99)
message_key  = RequestParameter("message", str, 0, 200)

flask_guard = FlaskGuard(__name__)

user_required_keys = [name_key, age_key]

# The request must have at least a 'name' key with a minimum length of 0 and
#  maximum length of 20. It also needs to have an 'age' key with a value type
#  of integer which has a minimum value of 0 and maximum value of 99 to pass 
# and be considered valid."
validated_user_creation_request = flask_guard.create_validate_function(user_required_keys)

# The request must have the 'message' key with a value of type string and a
#  minimum length of 0 and a maximum length of 200 to be considered valid.
validated_message_creation_request = flask_guard.create_validate_function([message_key])


@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    # The validated function will return a tuple where the first element is 
    # True or False depending on if the request is valid, and the second element
    # will be the error messages.
    is_vaild,messages = validated_user_creation_request(data)
    if not is_vaild:
        return jsonify(messages),400
    user = User(str(uuid.uuid4()), data['name'])
    users.append(user)
    return jsonify(user.serialize()), 201

@app.route('/messages', methods=['POST'])
def add_message():
    data = request.json
    user_id = data['user_id']
    if not any(user.id == user_id for user in users):
        return 'Invalid user id', 400
    is_vaild,message = validated_message_creation_request(data)
    if not is_vaild:
        return jsonify(messages),400
    message = Message(str(uuid.uuid4()), data['text'], user_id)
    messages.append(message)
    return jsonify(message.serialize()), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.serialize() for user in users])

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify([message.serialize() for message in messages])

if __name__ == '__main__':
    app.run(debug=True)