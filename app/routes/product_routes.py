from flask import Blueprint, request
from app.services.product_service import *
from app.schemas.product_schema import ProductSchema
from app.utils.cloudinary_uploader import upload_image_to_cloudinary

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

# Create a new product with optional image upload
@product_bp.post('/')
def create_product_route():
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return {"errors": errors}, 400

    try:
        # Handle Cloudinary upload if base64 image is provided
        image_url = data.get('image_url')
        image_base64 = data.get('image_base64')

        if image_base64:
            uploaded_url = upload_image_to_cloudinary(image_base64)
            if not uploaded_url:
                return {"message": "Image upload to Cloudinary failed"}, 500
            data['image_url'] = uploaded_url

        elif not image_url:
            return {"message": "Image required"}, 400

        product = create_product(data)
        return product_schema.dump(product), 201

    except Exception as e:
        return {"message": "Error creating product", "error": str(e)}, 500

# Update product
@product_bp.put('/<int:product_id>')
def update_product_route(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404

    data = request.get_json()

    # Handle optional image upload update
    image_base64 = data.get('image_base64')
    if image_base64:
        uploaded_url = upload_image_to_cloudinary(image_base64)
        if uploaded_url:
            data['image_url'] = uploaded_url

    updated = update_product(product, data)
    return product_schema.dump(updated), 200

# Delete product
@product_bp.delete('/<int:product_id>')
def delete_product_route(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return {"message": "Product not found"}, 404

    delete_product(product)
    return {"message": "Product deleted"}, 200
