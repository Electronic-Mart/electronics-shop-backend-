from flask import Blueprint, request
from app.services.user_service import *
from app.schemas.user_schema import UserSchema
from app.utils.jwt_handler import token_required
from app.utils.role_required import admin_required

user_bp = Blueprint('users', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.get('/')
@token_required
@admin_required
def get_users():
    users = get_all_users()
    return users_schema.dump(users)

@user_bp.get('/me')
@token_required
def get_my_profile(current_user):
    return user_schema.dump(current_user)

@user_bp.put('/me')
@token_required
def update_my_profile(current_user):
    data = request.get_json()
    updated = update_user(current_user, data)
    return user_schema.dump(updated)

@user_bp.put('/<int:user_id>/role')
@token_required
@admin_required
def assign_user_role(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return {"message": "User not found"}, 404
    data = request.get_json()
    return user_schema.dump(assign_role(user, data.get("role")))
