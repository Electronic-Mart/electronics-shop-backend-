from flask import Blueprint, jsonify
from sqlalchemy import func
from backend.models.order import Order
from backend.models.db import db

analytics_api = Blueprint('analytics_api', __name__)

@analytics_api.route('/analytics/order-summary', methods=['GET'])
def order_summary():
    result = db.session.query(
        func.count(Order.id).label("total_orders"),
        func.sum(Order.total).label("total_revenue")
    ).one()

    return jsonify({
        "total_orders": result.total_orders or 0,
        "total_revenue": float(result.total_revenue or 0.0)
    })

@analytics_api.route('/analytics/order-trends', methods=['GET'])
def order_trends():
    result = (
        db.session.query(func.date(Order.created_at), func.count(Order.id))
        .group_by(func.date(Order.created_at))
        .all()
    )
    trends = [{"date": str(date), "orders": count} for date, count in result]
    return jsonify({"order_trends": trends})
