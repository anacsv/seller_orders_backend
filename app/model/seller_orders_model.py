import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

from app.model.base_model import BaseModel

Base = declarative_base()


class SellerOrdersModel(BaseModel, Base):

    __tablename__ = 'seller_orders_sellerorder'
    __code = db.Column('code', db.String(length=16))
    __order_id = db.Column('order_id', db.String(length=16))
    __channel_slug = db.Column('channel_slug', db.String(length=16))
    __channel_store = db.Column('channel_store', db.String(length=100))
    __seller_id = db.Column('seller_id', db.String(length=16))
    __seller_name = db.Column('seller_name', db.String(length=100))
    __purchase_timestamp = db.Column('purchase_timestamp', db.TIMESTAMP())
    __status = db.Column('status', db.String(length=20))
    __approved_at = db.Column('approved_at', db.TIMESTAMP())
    __shipping_limit_date = db.Column('shipping_limit_date', db.TIMESTAMP())
    __availability_days = db.Column('availability_days', db.Integer)
    __invoice_url = db.Column('invoice_url', db.String(length=200))
    __invoice_issue_date = db.Column('invoice_issue_date', db.TIMESTAMP())
    __invoice_key = db.Column('invoice_key', db.String(length=100))
    __invoice_number = db.Column('invoice_number', db.Integer)
    __invoice_serial_number = db.Column('invoice_serial_number', db.Integer)
    __customer_id = db.Column('customer_id', db.String(length=16))
    __shipment_id = db.Column('shipment_id', db.String(length=16))
    __invoice_source = db.Column('invoice_source', db.String(length=32))
    __delivered_customer_date = db.Column('delivered_customer_date', db.TIMESTAMP())
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
    __invoice_errors = db.Column('invoice_errors', db.JSON)

    def __init__(self, code: str = '', order_id: str = ''
                 , channel_slug: str = '', channel_store: str = '', seller_id: str = '', seller_name: str = ''
                 , purchase_timestamp: str = '', status: str = '', approved_at: str = '', shipping_limit_date: str = ''
                 , availability_days: int = 0, invoice_url: str = '', invoice_issue_date: str = '', invoice_key: str = ''
                 , invoice_number: int = 0, invoice_serial_number: int = 0, customer_id: str = '', shipment_id: str = ''
                 , invoice_source: str = '', delivered_customer_date: str = '', seller_brand: str = '', seller_email: str = ''
                 , invoice_danfe_url: str = '', cancelation_reason: str = '', cancelation_status: str = '', suspension_reason: str = ''
                 , estimated_delivery_date: str = '', invoice_status: str = '', invoice_id: str = '', branded_store_slug: str = ''
                 , search_vector: str = '', shipping_quote_group_id: str = '', payer_id: str = '', display_status: str = ''
                 , estimated_delivery_shift: str = '', invoice_errors: str = ''):

        self.__code = code
        self.__order_id = order_id
        self.__channel_slug = channel_slug
        self.__channel_store = channel_store
        self.__seller_id = seller_id
        self.__seller_name = seller_name
        self.__purchase_timestamp = purchase_timestamp
        self.__status = status
        self.__approved_at = approved_at
        self.__shipping_limit_date = shipping_limit_date
        self.__availability_days = availability_days
        self.__invoice_url = invoice_url
        self.__invoice_issue_date = invoice_issue_date
        self.__invoice_key = invoice_key
        self.__invoice_number = invoice_number
        self.__invoice_serial_number = invoice_serial_number
        self.__customer_id = customer_id
        self.__shipment_id = shipment_id
        self.__invoice_source = invoice_source
        self.__delivered_customer_date = delivered_customer_date
        self.__seller_brand = seller_brand
        self.__seller_email = seller_email
        self.__invoice_danfe_url = invoice_danfe_url
        self.__cancelation_reason = cancelation_reason
        self.__cancelation_status = cancelation_status
        self.__suspension_reason = suspension_reason
        self.__estimated_delivery_date = estimated_delivery_date
        self.__invoice_status = invoice_status
        self.__invoice_id = invoice_id
        self.__branded_store_slug = branded_store_slug
        self.__search_vector = search_vector
        self.__shipping_quote_group_id = shipping_quote_group_id
        self.__payer_id = payer_id
        self.__display_status = display_status
        self.__estimated_delivery_shift = estimated_delivery_shift
        self.__invoice_errors = invoice_errors
        self

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'code': self.code,
            'order_id': self.order_id,
            'channel_slug': self.channel_slug,
            'channel_store': self.channel_store,
            'seller_id': self.seller_id,
            'seller_name': self.seller_name,
            'purchase_timestamp': self.purchase_timestamp,
            'status': self.status,
            'approved_at': self.approved_at,
            'shipping_limit_date': self.shipping_limit_date,
            'availability_days': self.availability_days,
            'invoice_url': self.invoice_url,
            'invoice_issue_date': self.invoice_issue_date,
            'invoice_key': self.invoice_key,
            'invoice_number': self.invoice_number,
            'invoice_serial_number': self.invoice_serial_number,
            'customer_id': self.customer_id,
            'shipment_id': self.shipment_id,
            'invoice_source': self.invoice_source,
            'delivered_customer_date': self.delivered_customer_date,
            'seller_brand': self.seller_brand,
            'seller_email': self.seller_email,
            'invoice_danfe_url': self.invoice_danfe_url,
            'cancelation_reason': self.cancelation_reason,
            'cancelation_status': self.cancelation_status,
            'suspension_reason': self.suspension_reason,
            'estimated_delivery_date': self.estimated_delivery_date,
            'invoice_status': self.invoice_status,
            'invoice_id': self.invoice_id,
            'branded_store_slug': self.branded_store_slug,
            'search_vector': self.search_vector,
            'shipping_quote_group_id': self.shipping_quote_group_id,
            'payer_id': self.payer_id,
            'display_status': self.display_status,
            'estimated_delivery_shift': self.estimated_delivery_shift,
            'invoice_errors': self.invoice_errors,
        }

    # --------------------------- code
    @property
    def code(self) -> str:
        return str(self.__code)

    @code.setter
    def code(self, code: str):
        self.__code = str(code)

    # --------------------------- order_id
    @property
    def order_id(self) -> str:
        return str(self.__order_id)

    @order_id.setter
    def order_id(self, order_id: str):
         self.__order_id = str(order_id)

    # --------------------------- channel_slug
    @property
    def channel_slug(self) -> str:
        return str(self.__channel_slug)

    @channel_slug.setter
    def channel_slug(self, channel_slug: str):
        self.__channel_slug = str(channel_slug)

     # --------------------------- channel_store
    @property
    def channel_store(self) -> str:
        return str(self.__channel_store)

    @channel_store.setter
    def channel_store(self, channel_store: str):
        self.__channel_store = str(channel_store)

    # ------------------------------ seller_id
    @property
    def seller_id(self) -> str:
        return str(self.__seller_id)

    @seller_id.setter
    def seller_id(self, seller_id: str):
        self.__seller_id = str(seller_id)

    # ------------------------------- seller_name
    @property
    def seller_name(self) -> str:
        return str(self.__seller_name)

    @seller_name.setter
    def seller_name(self, seller_name: str):
        self.__seller_name = str(seller_name)

    # -------------------------------- purchase_timestamp
    @property
    def purchase_timestamp(self) -> str:
        return str(self.__purchase_timestamp)

    @purchase_timestamp.setter
    def purchase_timestamp(self, purchase_timestamp: str):
        self.__purchase_timestamp = str(purchase_timestamp)

    # ---------------------------------- status
    @property
    def status(self) -> str:
        return str(self.__status)

    @status.setter
    def status(self, status: str):
        self.__status = str(status)

    # ---------------------------------- approved_at
    @property
    def approved_at(self) -> str:
        return str(self.__approved_at)

    @approved_at.setter
    def approved_at(self, approved_at: str):
        self.__approved_at = str(approved_at)

    # ---------------------------------- shipping_limit_date
    @property
    def shipping_limit_date(self) -> str:
        return str(self.__shipping_limit_date)

    @shipping_limit_date.setter
    def shipping_limit_date(self, shipping_limit_date: str):
        self.__shipping_limit_date = str(shipping_limit_date)

    # ---------------------------------- availability_days
    @property
    def availability_days(self) -> int:
        return int(self.__availability_days)

    @availability_days.setter
    def availability_days(self, availability_days: int):
        self.__availability_days = int(availability_days)

    # ---------------------------------- invoice_url
    @property
    def invoice_url(self) -> str:
        return str(self.__invoice_url)

    @invoice_url.setter
    def invoice_url(self, invoice_url: str):
        self.__invoice_url = str(invoice_url)

    # ---------------------------------- invoice_issue_date
    @property
    def invoice_issue_date(self) -> str:
        return str(self.__invoice_issue_date)

    @invoice_issue_date.setter
    def invoice_issue_date(self, invoice_issue_date: str):
        self.__invoice_issue_date = str(invoice_issue_date)

    # ---------------------------------- invoice_key
    @property
    def invoice_key(self) -> str:
        return str(self.__invoice_key)

    @invoice_key.setter
    def invoice_key(self, invoice_key: str):
        self.__invoice_key = str(invoice_key)

    # ---------------------------------- invoice_number
    @property
    def invoice_number(self) -> int:
        return int(self.__invoice_number)

    @invoice_number.setter
    def invoice_number(self, invoice_number: int):
        self.__invoice_number = int(invoice_number)

    # ---------------------------------- invoice_serial_number
    @property
    def invoice_serial_number(self) -> int:
        return int(self.__invoice_serial_number)

    @invoice_serial_number.setter
    def invoice_serial_number(self, invoice_serial_number: int):
        self.__invoice_serial_number = int(invoice_serial_number)

    # ------------------------------------ customer_id
    @property
    def customer_id(self) -> str:
        return str(self.__customer_id)

    @customer_id.setter
    def customer_id(self, customer_id: str):
        self.__customer_id = str(customer_id)

    # ------------------------------------ shipment_id
    @property
    def shipment_id(self) -> str:
        return str(self.__shipment_id)

    @shipment_id.setter
    def shipment_id(self, shipment_id: str):
        self.__shipment_id = str(shipment_id)

    # ------------------------------------ invoice_source
    @property
    def invoice_source(self) -> str:
        return str(self.__invoice_source)

    @invoice_source.setter
    def invoice_source(self, invoice_source: str):
        self.__invoice_source = str(invoice_source)

    # ------------------------------------ delivered_customer_date
    @property
    def delivered_customer_date(self) -> str:
        return str(self.__delivered_customer_date)

    @delivered_customer_date.setter
    def delivered_customer_date(self, delivered_customer_date: str):
        self.__delivered_customer_date = str(delivered_customer_date)

    # ------------------------------------ seller_brand
    @property
    def seller_brand(self) -> str:
        return str(self.__seller_brand)

    @seller_brand.setter
    def seller_brand(self, seller_brand: str):
        self.__seller_brand = str(seller_brand)

    # ------------------------------------ seller_email
    @property
    def seller_email(self) -> str:
        return str(self.__seller_email)

    @seller_email.setter
    def seller_email(self, seller_email: str):
        self.__seller_email = str(seller_email)

    # ------------------------------------ invoice_danfe_url
    @property
    def invoice_danfe_url(self) -> str:
        return str(self.__invoice_danfe_url)

    @invoice_danfe_url.setter
    def invoice_danfe_url(self, invoice_danfe_url: str):
        self.__invoice_danfe_url = str(invoice_danfe_url)

    # ------------------------------------ cancelation_reason
    @property
    def cancelation_reason(self) -> str:
        return str(self.__cancelation_reason)

    @cancelation_reason.setter
    def cancelation_reason(self, cancelation_reason: str):
        self.__cancelation_reason = str(cancelation_reason)

    # ------------------------------------ cancelation_status
    @property
    def cancelation_status(self) -> str:
        return str(self.__cancelation_status)

    @cancelation_status.setter
    def cancelation_status(self, cancelation_status: str):
        self.__cancelation_status = str(cancelation_status)

    # ------------------------------------ suspension_reason
    @property
    def suspension_reason(self) -> str:
        return str(self.__suspension_reason)

    @suspension_reason.setter
    def suspension_reason(self, suspension_reason: str):
        self.__suspension_reason = str(suspension_reason)

    # ------------------------------------ estimated_delivery_date
    @property
    def estimated_delivery_date(self) -> str:
        return str(self.__estimated_delivery_date)

    @estimated_delivery_date.setter
    def estimated_delivery_date(self, estimated_delivery_date: str):
        self.__estimated_delivery_date = str(estimated_delivery_date)

    # ------------------------------------ invoice_status
    @property
    def invoice_status(self) -> str:
        return str(self.__invoice_status)

    @invoice_status.setter
    def invoice_status(self, invoice_status: str):
        self.__invoice_status = str(invoice_status)

    # ------------------------------------ invoice_id
    @property
    def invoice_id(self) -> str:
        return str(self.__invoice_id)

    @invoice_id.setter
    def invoice_id(self, invoice_id: str):
        self.__invoice_id = str(invoice_id)

    # ------------------------------------ branded_store_slug
    @property
    def branded_store_slug(self) -> str:
        return str(self.__branded_store_slug)

    @branded_store_slug.setter
    def branded_store_slug(self, branded_store_slug: str):
        self.__branded_store_slug = str(branded_store_slug)

    # ------------------------------------ search_vector
    @property
    def search_vector(self) -> str:
        return str(self.__search_vector)

    @search_vector.setter
    def search_vector(self, search_vector: str):
        self.__search_vector = str(search_vector)

    # ------------------------------------ shipping_quote_group_id
    @property
    def shipping_quote_group_id(self) -> str:
        return str(self.__shipping_quote_group_id)

    @shipping_quote_group_id.setter
    def shipping_quote_group_id(self, shipping_quote_group_id: str):
        self.__shipping_quote_group_id = str(shipping_quote_group_id)

    # ------------------------------------ payer_id
    @property
    def payer_id(self) -> str:
        return str(self.__payer_id)

    @payer_id.setter
    def payer_id(self, payer_id: str):
        self.__payer_id = str(payer_id)

    # ------------------------------------ display_status
    @property
    def display_status(self) -> str:
        return str(self.__display_status)

    @display_status.setter
    def display_status(self, display_status: str):
        self.__display_status = str(display_status)

    # ------------------------------------ estimated_delivery_shift
    @property
    def estimated_delivery_shift(self) -> str:
        return str(self.__estimated_delivery_shift)

    @estimated_delivery_shift.setter
    def estimated_delivery_shift(self, estimated_delivery_shift: str):
        self.__estimated_delivery_shift = str(estimated_delivery_shift)

    # ------------------------------------ invoice_errors
    @property
    def invoice_errors(self) -> str:
        return str(self.__invoice_errors)

    @invoice_errors.setter
    def invoice_errors(self, invoice_errors: str):
        self.__invoice_errors = str(invoice_errors)