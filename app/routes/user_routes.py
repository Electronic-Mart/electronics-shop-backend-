from flask import Blueprint, request, jsonify
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
    return users_schema.dump(users), 200

@user_bp.get('/me')
@token_required
def get_my_profile(current_user):
    return user_schema.dump(current_user), 200

@user_bp.put('/me')
@token_required
def update_my_profile(current_user):
    data = request.get_json()

    if not data:
        return jsonify({'message': 'No data provided'}), 400

    try:
        current_user.username = data.get('name') or data.get('username') or current_user.username
        current_user.email = data.get('email', current_user.email)
        current_user.password = data.get('password', current_user.password)
        current_user.phone = data.get('phone', current_user.phone)

        from app import db
        db.session.commit()
        return user_schema.dump(current_user), 200

    except Exception as e:
        from app import db
        db.session.rollback()
        return jsonify({'message': 'Update failed', 'error': str(e)}), 500

@user_bp.put('/<int:user_id>/role')
@token_required
@admin_required
def assign_user_role(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return {"message": "User not found"}, 404
    data = request.get_json()
    return user_schema.dump(assign_role(user, data.get("role"))), 200
