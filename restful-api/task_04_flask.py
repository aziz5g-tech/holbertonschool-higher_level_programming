from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

users = {}

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(list(users.keys())), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/status', methods=['GET'])
def get_status():
    return "OK"

if __name__ == '__main__':
    app.run()
