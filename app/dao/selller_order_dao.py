from app.dao.base_dao import BaseDao
from app.model.selller_order_model import SellerOrderModel

class SellerOrderDao(BaseDao):

    def __init__(self):
        self.__table_name = 'sellerOrderModel'
        super().__init__(SellerOrderModel)

    def read(self, id: int = None):
        return super().__init__(id)

    def create(self, model: SellerOrderModel) -> SellerOrderModel:
        model.id = super().insert(model)
        return model

    def update(self, model: SellerOrderModel) -> SellerOrderModel:
        return super().update(model)

    def delete(self, id: int) -> dict:
        return super().delete(id)

