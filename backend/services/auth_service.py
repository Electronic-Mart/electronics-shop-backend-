from models import User, db
from flask_jwt_extended import create_access_token

def register_user(data):
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered"}

def login_user(data):
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        token = create_access_token(identity={"id": user.id, "role": user.role})
        return {"token": token}
    return {"error": "Invalid credentials"}, 401
