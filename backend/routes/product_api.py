from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.product import Product, Category
from backend.extensions import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    category_id = request.args.get('category_id')
    search = request.args.get('search')
    
    query = Product.query
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    if search:
        query = query.filter(Product.name.ilike(f'%{search}%'))
    
    paginated_products = query.paginate(page=page, per_page=per_page)
    
    products = [{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'category_id': product.category_id,
        'stock': product.stock
    } for product in paginated_products.items]
    
    return jsonify({
        'products': products,
        'total': paginated_products.total,
        'pages': paginated_products.pages,
        'current_page': page
    })

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock,
        'category': product.category.name,
        'seller_id': product.seller_id
    })

@products_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': cat.id,
        'name': cat.name,
        'parent_id': cat.parent_id
    } for cat in categories])