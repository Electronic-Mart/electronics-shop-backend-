from flask import Blueprint, jsonify

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Electronics Shop API"})
