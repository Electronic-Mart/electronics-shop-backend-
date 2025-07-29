from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.order import Order, OrderItem
from ..models.product import Product
from ..models.user import User
from ..extensions import db
from datetime import datetime

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_order():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    items = []
    total = 0.0
    
    for item in data['items']:
        product = Product.query.get(item['product_id'])
        if not product or product.stock < item['quantity']:
            return jsonify({"msg": f"Product {item['product_id']} not available"}), 400
        
        items.append({
            'product_id': product.id,
            'quantity': item['quantity'],
            'unit_price': product.price
        })
        total += product.price * item['quantity']
    
    order = Order(
        user_id=user_id,
        total_amount=total,
        shipping_address=data['shipping_address'],
        payment_method=data['payment_method']
    )
    db.session.add(order)
    db.session.commit()
    
    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            unit_price=item['unit_price']
        )
        db.session.add(order_item)
        
        product = Product.query.get(item['product_id'])
        product.stock -= item['quantity']
    
    db.session.commit()
    
    return jsonify({
        "msg": "Order created successfully",
        "order_id": order.id,
        "total": order.total_amount
    }), 201

@orders_bp.route('/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    user_id = get_jwt_identity()
    order = Order.query.filter_by(id=order_id, user_id=user_id).first_or_404()
    
    items = [{
        'product_id': item.product_id,
        'name': item.product.name,
        'quantity': item.quantity,
        'unit_price': item.unit_price,
        'subtotal': item.subtotal
    } for item in order.items]
    
    return jsonify({
        'id': order.id,
        'status': order.status,
        'total_amount': order.total_amount,
        'created_at': order.created_at.isoformat(),
        'items': items
    })

@orders_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).order_by(Order.created_at.desc()).all()
    
    return jsonify([{
        'id': order.id,
        'status': order.status,
        'total_amount': order.total_amount,
        'created_at': order.created_at.isoformat()
    } for order in orders])