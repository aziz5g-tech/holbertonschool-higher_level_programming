#!/usr/bin/python3
"""Flask API with Basic and JWT Authentication"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-in-production'
jwt = JWTManager(app)

# Users stored in memory with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# Basic Authentication verification
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


# Basic Auth error handler
@auth.error_handler
def auth_error(status):
    """Handle basic auth errors"""
    return jsonify({"error": "Unauthorized"}), 401


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle fresh token requirement"""
    return jsonify({"error": "Fresh token required"}), 401


# Custom decorator for role-based access
def admin_required(fn):
    """Decorator to require admin role"""
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get('role') != 'admin':
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper


# Routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protected by basic authentication"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login route to obtain JWT token"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with user identity and role in additional claims
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]['role']}
    )

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protected by JWT authentication"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@admin_required
def admin_only():
    """Route accessible only by admin users"""
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
