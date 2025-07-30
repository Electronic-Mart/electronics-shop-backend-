from app.models.user import User
from app import db, bcrypt
from app.utils.jwt_handler import generate_token

def register_user(data):
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Automatically assign 'admin' role if the email matches
    role = "admin" if data['email'] == "alexnjugi11@gmail.com" else "user"

    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_pw,
        phone=data.get('phone'),
        role=role  # ✅ This line was missing
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        token = generate_token(user)
        return {"user": user, "token": token}
    return None
