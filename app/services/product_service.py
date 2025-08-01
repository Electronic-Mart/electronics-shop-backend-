from app.models.product import Product
from app import db
from app.utils.cloudinary_uploader import upload_image_to_cloudinary

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(data):
    # Handle image upload
    if "image_base64" in data:
        image_url = upload_image_to_cloudinary(data["image_base64"])
        if image_url:
            data["image_url"] = image_url
    data.pop("image_base64", None)  # Remove base64 key before DB insert

    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product, data):
    # Handle optional image update
    if "image_base64" in data:
        image_url = upload_image_to_cloudinary(data["image_base64"])
        if image_url:
            data["image_url"] = image_url
    data.pop("image_base64", None)

    for key, value in data.items():
        setattr(product, key, value)

    db.session.commit()
    return product

def delete_product(product):
    db.session.delete(product)
    db.session.commit()
