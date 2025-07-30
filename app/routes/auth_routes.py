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
    try:
        data = request.get_json()
        if not data or "email" not in data or "password" not in data:
            return jsonify({"message": "Email and password required"}), 400

        auth = authenticate_user(data["email"], data["password"])
        if auth:
            return jsonify({
                "user": user_schema.dump(auth["user"]),
                "token": auth["token"]
            }), 200

        return jsonify({"message": "Invalid credentials"}), 401

    except Exception as e:
        # You can also log this using logging module instead of print
        print(f"Login error: {str(e)}")
        return jsonify({"message": "Internal server error"}), 500
