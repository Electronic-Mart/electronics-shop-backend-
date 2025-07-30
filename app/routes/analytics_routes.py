from flask import Blueprint
from app.services.analytics_service import *
from app.utils.jwt_handler import token_required
from app.utils.role_required import admin_required

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.get('/orders')
@token_required
@admin_required
def order_stats():
    return get_order_stats()

@analytics_bp.get('/top-products')
@token_required
@admin_required
def top_products():
    return get_top_products()
