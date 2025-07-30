from flask import Blueprint, request, jsonify
from app.services.product_service import *
from app.schemas.product_schema import ProductSchema
from app.models.product import Product
from app.utils.role_required import admin_required
from app.utils.jwt_handler import token_required

product_bp = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.get('/')
def get_products():
    products = get_all_products()
    return products_schema.dump(products)

@product_bp.get('/<int:product_id>')
def get_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404
    return product_schema.dump(product)

@product_bp.post('/')
@token_required
@admin_required
def create():
    data = request.get_json()
    product = create_product(data)
    return product_schema.dump(product), 201

@product_bp.put('/<int:product_id>')
@token_required
@admin_required
def update(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404
    data = request.get_json()
    updated = update_product(product, data)
    return product_schema.dump(updated)

@product_bp.delete('/<int:product_id>')
@token_required
@admin_required
def delete(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404
    delete_product(product)
    return {"message": "Product deleted"}
