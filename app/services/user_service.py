from app.models.user import User
from app import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user(user, data):
    for key in ['username', 'email', 'phone']:
        if key in data:
            setattr(user, key, data[key])
    if 'password' in data:
        from app import bcrypt
        user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    db.session.commit()
    return user

def assign_role(user, role):
    user.role = role
    db.session.commit()
    return user
