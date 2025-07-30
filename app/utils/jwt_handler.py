import jwt
import os
from functools import wraps
from flask import request, jsonify
from app.models.user import User

SECRET_KEY = os.getenv('SECRET_KEY')

def generate_token(user):
    payload = {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({"message": "Token missing"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.get(data["id"])
            if not current_user:
                return jsonify({"message": "User not found"}), 404
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401

        return f(current_user, *args, **kwargs)

    return decorated
