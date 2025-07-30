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
@token_required     #  token_required must come first
@admin_required     # admin_required comes after
def create(current_user):
    try:
        data = request.get_json()

        # Optional: validate data using schema
        errors = product_schema.validate(data)
        if errors:
            return {"errors": errors}, 400

        product = create_product(data)
        return product_schema.dump(product), 201

    except Exception as e:
        print("❌ Product creation error:", str(e))
        return {"message": "Internal server error", "error": str(e)}, 500

@product_bp.put('/<int:product_id>')
@token_required
@admin_required
def update(current_user, product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404
    data = request.get_json()
    updated = update_product(product, data)
    return product_schema.dump(updated)

@product_bp.delete('/<int:product_id>')
@token_required
@admin_required
def delete(current_user, product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404
    delete_product(product)
    return {"message": "Product deleted"}
