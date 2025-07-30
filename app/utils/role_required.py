from functools import wraps
from flask import jsonify
import os

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not current_user or not current_user.is_admin():
            return jsonify({"message": "Admin access required"}), 403
        return f(current_user, *args, **kwargs)
    return decorated
