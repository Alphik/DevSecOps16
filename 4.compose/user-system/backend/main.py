from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

users = [
    {'id': 1, 'name': 'Alice Smith'},
    {'id': 2, 'name': 'Bob Johnson'},
    {'id': 3, 'name': 'Charlie Brown'},
    {'id': 4, 'name': 'Diana Prince'}
]
@app.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    """Add a new user."""
    user_data = request.get_json()
    
    if not user_data or 'name' not in user_data:
        return jsonify({"error": "Invalid user data"}), 400
    
    user = {
        'id': len(users) + 1,  # Simple ID generation
        'name': user_data['name']
    }
    
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True,port=5050,host='0.0.0.0')
