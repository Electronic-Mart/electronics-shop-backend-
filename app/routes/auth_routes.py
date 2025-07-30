from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, authenticate_user
from app.schemas.user_schema import UserSchema

auth_bp = Blueprint('auth', __name__)
user_schema = UserSchema()

@auth_bp.post('/register')
def register():
    data = request.get_json()
    user = register_user(data)
    return user_schema.dump(user), 201

@auth_bp.post('/login')
def login():
    data = request.get_json()
    auth = authenticate_user(data["email"], data["password"])
    if auth:
        return {
            "user": user_schema.dump(auth["user"]),
            "token": auth["token"]
        }
    return {"message": "Invalid credentials"}, 401
