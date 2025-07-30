import uuid
from datetime import datetime

def generate_invoice_number():
    now = datetime.utcnow()
    return f"INV-{now.strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
