from flask import Blueprint, request, jsonify
from backend.models.db import db
from backend.models.order import Order
from backend.models.user import User

order_api = Blueprint('order_api', __name__)

@order_api.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    user = db.session.get(User, data['user_id'])
    if not user:
        return jsonify({"error": "User not found"}), 404

    new_order = Order(
        user_id=data['user_id'],
        total=data['total'],
        status=data['status']
    )
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order created", "order_id": new_order.id}), 201


@order_api.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = []
    for order in orders:
        result.append({
            "id": order.id,
            "user_id": order.user_id,
            "total": float(order.total),  
            "status": order.status
        })
    return jsonify({"orders": result})


@order_api.route('/orders/<int:order_id>', methods=['PUT']) 
def update_order(order_id):
    order = db.session.get(Order, order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    data = request.json
    if 'status' in data:
        order.status = data['status']
    if 'total' in data:
        order.total = data['total']

    db.session.commit()
    return jsonify({"message": "Order updated"})


@order_api.route('/orders/<int:order_id>', methods=['DELETE']) 
def delete_order(order_id):
    order = db.session.get(Order, order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"})
