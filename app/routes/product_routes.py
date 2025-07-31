from flask import Blueprint, request
from app.services.product_service import *
from app.schemas.product_schema import ProductSchema

product_bp = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Public: GET all products
@product_bp.get('/')
def get_products():
    products = get_all_products()
    return products_schema.dump(products), 200

# Public: GET product by ID
@product_bp.get('/<int:product_id>')
def get_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404
    return product_schema.dump(product), 200

# No Auth: CREATE product (trust frontend to allow only admin)
@product_bp.post('/')
def create_product_route():
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return {"errors": errors}, 400

    product = create_product(data)
    return product_schema.dump(product), 201

# No Auth: UPDATE product
@product_bp.put('/<int:product_id>')
def update_product_route(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404

    data = request.get_json()
    updated = update_product(product, data)
    return product_schema.dump(updated), 200

# No Auth: DELETE product
@product_bp.delete('/<int:product_id>')
def delete_product_route(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404

    delete_product(product)
    return {"message": "Product deleted"}, 200
