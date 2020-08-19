import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

class sellerOrderModel():
    __tablename__ = 'seller_orders_sellerorder'
    __created_at = db.Column('created_at', db.TIMESTAMP)
    __update_at = db.Column('update_at', db.TIMESTAMP)
    __code = db.Column('code', db.String(length=16))
    __order_id = db.Column('order_id', db.String(length=16))
    __channel_slug = db.Column('channel_slug', db.String(length=16))
    __channel_store = db.Column('channel_store', db.String(length=100))
    __seller_id = db.Column('seller_id', db.String(length=16))
    __seller_name = db.Column('seller_name', db.String(length=100))
    __purchase_timestamp = db.Column('purchase_timestamp', db.TIMESTAMP)
    __status = db.Column('status', db.String(length=20))
    __approved_at = db.Column('approved_at', db.TIMESTAMP)
    __shipping_limit_date = db.Column('shipping_limit_date', db.TIMESTAMP)
    __availability_days = db.Column('availability_days', db.Integer)
    __invoice_url = db.Column('invoice_url', db.String(length=200))
    __invoice_issue_date = db.Column('invoice_issue_date', db.TIMESTAMP)
    __invoice_key = db.Column('invoice_key', db.String(length=100))
    __invoice_number = db.Column('invoice_number', db.Integer)
    __invoice_serial_number = db.Column('invoice_serial_number', db.Integer)
    __customer_id = db.Column('customer_id', db.String(length=16))
    __shipment_id = db.Column('shipment_id', db.String(length=16))
    __invoice_source = db.Column('invoice_source', db.String(length=32))
    __delivered_customer_date = db.Column('delivered_customer_date', db.TIMESTAMP)
    __seller_brand = db.Column('seller_brand', db.String(length=256))
    __seller_email = db.Column('seller_email', db.String(length=254))
    __invoice_danfe_url = db.Column('invoice_danfe_url', db.String(length=200))
    __cancelation_reason = db.Column('cancelation_reason', db.String(length=64))
    __cancelation_status = db.Column('cancelation_status', db.String(length=64))
    __suspension_reason = db.Column('suspension_reason', db.String(length=64))
    __estimated_delivery_date = db.Column('estimated_delivery_date', db.DATE)
    __invoice_status = db.Column('invoice_status', db.String(length=16))
    __invoice_id = db.Column('invoice_id', db.String(length=16))
    __branded_store_slug = db.Column('branded_store_slug', db.String(length=32))
    __search_vector = db.Column('search_vector', db.String(length=16))
    __shipping_quote_group_id = db.Column('shipping_quote_group_id', db.String(length=16))
    __payer_id = db.Column('payer_id', db.String(length=16))
    __display_status = db.Column('display_status', db.String(length=20))
    __estimated_delivery_shift = db.Column('estimated_delivery_shift', db.String(length=16))
    __invoice_error = db.Column('invoice_error', db.JSON)

    def __init__(self, created_at: str = '', updated_at: str = '', code: str = '', order_id: str = ''
                 , channel_slug: str = '', channel_store: str = '', seller_id: str = '', seller_name: str = ''
                 , purchase_timestamp: str = '', status: str = '', approved_at: str = '', shipping_limit_date: str = ''
                 , availability_days: int = 0, invoice_url: str = '', invoice_issue_data: str = '', invoice_key: str = ''
                 , invoice_number: int = 0, invoice_serial_number: int = 0, customer_id: str = '', shipment_id: str = ''
                 , invoice_source: str = '', delivered_customer_date: str = '', seller_brand: str = '', seller_email: str = ''
                 , invoice_danfe_url: str = '', cancelation_reason: str = '', cancelation_status: str = '', suspension_reason: str = ''
                 , estimated_delivery_date: str = '', invoice_status: str = '', invoice_id: str = '', branded_store_slug: str = ''
                 , search_vector: str = '', shipping_quote_group_id: str = '', payer_id: str = '', display_status: str = ''
                 , estimated_delivery_shift: str = '', invoice_error: str = ''):