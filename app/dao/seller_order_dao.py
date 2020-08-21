from app.dao.base_dao import BaseDao
from app.model.seller_order_model import SellerOrderModel


class SellerOrderDao(BaseDao):

    def __init__(self):
        self.__table_name = 'seller_orders_sellerorder'
        super().__init__(SellerOrderModel)

    def read(self, id:str = ''):
        return super().read(id)

    def create(self, model: SellerOrderModel) -> SellerOrderModel:
        return super().insert(model)

    def update(self, model: SellerOrderModel) -> SellerOrderModel:
        return super().update(model)

    def delete(self, id:str) -> dict:
        return super().delete(id)

