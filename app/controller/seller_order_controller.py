from app.dao.seller_order_dao import SellerOrderDao
from app.model.seller_order_model import SellerOrderModel
from flask import jsonify, request
from flask_restful import Resource


class SellerOrderController(Resource):

    def __init__(self):
        self.__dao = SellerOrderDao()

    def get(self, id=None):
        if id:
            model = self.__dao.read(id)
            if model:
                return jsonify(model.to_dict())
            return {}
        return jsonify([sellerorder.to_dict() for sellerorder in self.__dao.read()])

    # create
    def post(self):
        data = request.get_json()
        sellerorder = SellerOrderModel(**data)
        model = self.__dao.create(sellerorder)
        return self.verify_sql_error(model)

    # update
    def put(self, id):
        data = request.get_json()
        sellerorder = SellerOrderModel(**data)
        sellerorder.id = id
        model = self.__dao.update(sellerorder)
        return self.verify_sql_error(model)

    # delete
    def delete(self, id=None):
        message = self.__dao.delete(id)
        return jsonify(message)

    def verify_sql_error(self, m):
        if type(m) == SellerOrderModel:
            return jsonify(m.to_dict())
        return jsonify(m)
