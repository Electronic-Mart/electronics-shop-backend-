from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.models.db import db

user_api = Blueprint('user_api', __name__)

@user_api.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'], 
                    password_hash=data['password_hash'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user": new_user.id}), 201


