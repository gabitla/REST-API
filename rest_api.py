from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
    """
    users = [{"id": 1, "name": "John Doe"}]
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    parameters:
      - name: name
        in: body
        type: string
        required: true
    responses:
      201:
        description: User created
    """
    user = request.json
    return jsonify({"message": "User created", "user": user}), 201

if __name__ == '__main__':
    app.run(debug=True)
