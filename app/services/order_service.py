from app import db
from app.models.order import Order, OrderItem
from app.models.invoice import Invoice
from app.utils.invoice_generator import generate_invoice_number

def create_order(user, data):
    items = data.get("items", [])
    total = sum(item["quantity"] * item.get("price", 0) for item in items)

    order = Order(
        user_id=user.id,
        address=data["address"],
        billing_info=data["billing_info"],
        total=total
    )
    db.session.add(order)
    db.session.flush()

    for item in items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item["product_id"],
            quantity=item["quantity"],
            price=item["price"]
        )
        db.session.add(order_item)

    invoice = Invoice(
        order_id=order.id,
        invoice_number=generate_invoice_number(),
        amount=total
    )
    db.session.add(invoice)
    db.session.commit()

    return order
