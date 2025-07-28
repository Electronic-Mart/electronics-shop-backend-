from flask import Blueprint, request, jsonify
from backend.models.product import Product
from backend.models.db import db


product_api = Blueprint('product_api', __name__)

@product_api.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        image_url=data.get('image_url'),  
        stock_qty=data.get('stock_qty', 0)  
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created", "product": new_product.id}), 201
