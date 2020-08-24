from app.dao.base_dao import BaseDao
from app.model.seller_orders_model import SellerOrdersModel


class SellerOrdersDao(BaseDao):

    def __init__(self):
        self.__table_name = 'seller_orders_sellerorder'
        super().__init__(SellerOrdersModel)

    def read(self, id:str = ''):
        return super().read(id)

    def create(self, model: SellerOrdersModel) -> SellerOrdersModel:
        return super().insert(model)

    def update(self, model: SellerOrdersModel) -> SellerOrdersModel:
        return super().update(model)

    def delete(self, id:str) -> dict:
        return super().delete(id)

