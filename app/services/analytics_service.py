from app.models.order import Order, OrderItem
from app.models.product import Product
from sqlalchemy import func
from app import db

def get_order_stats():
    total_orders = Order.query.count()
    total_revenue = db.session.query(func.sum(Order.total)).scalar() or 0
    return {"total_orders": total_orders, "total_revenue": total_revenue}

def get_top_products(limit=5):
    top_products = db.session.query(
        Product.name,
        func.sum(OrderItem.quantity).label('total_sold')
    ).join(OrderItem.product).group_by(Product.id).order_by(func.sum(OrderItem.quantity).desc()).limit(limit).all()

    return [{"product": p[0], "sold": p[1]} for p in top_products]
