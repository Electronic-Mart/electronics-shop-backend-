from flask import Blueprint, request
from app.services.user_service import *
from app.schemas.user_schema import UserSchema

user_bp = Blueprint('users', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.get('/')
def get_users():
    users = get_all_users()
    return users_schema.dump(users), 200

@user_bp.get('/me')
def get_my_profile():
    
    dummy_user = get_user_by_id(1)
    if not dummy_user:
        return {"message": "Dummy user not found"}, 404
    return user_schema.dump(dummy_user), 200

@user_bp.put('/me')
def update_my_profile():
    dummy_user = get_user_by_id(1)
    if not dummy_user:
        return {"message": "Dummy user not found"}, 404

    data = request.get_json()
    updated = update_user(dummy_user, data)
    return user_schema.dump(updated), 200

# Public: Assign role (e.g., promote/demote user)
@user_bp.put('/<int:user_id>/role')
def assign_user_role(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return {"message": "User not found"}, 404
    data = request.get_json()
    return user_schema.dump(assign_role(user, data.get("role"))), 200
