from flask import Blueprint, request
from app.services.order_service import create_order
from app.schemas.order_schema import OrderSchema
from app.utils.jwt_handler import token_required

order_bp = Blueprint('orders', __name__)
order_schema = OrderSchema()

@order_bp.post('/')
@token_required
def place_order(current_user):
    data = request.get_json()
    order = create_order(current_user, data)
    return order_schema.dump(order), 201
