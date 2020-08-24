from app.dao.seller_orders_dao import SellerOrdersDao
from app.model.seller_orders_model import SellerOrdersModel
from flask import jsonify, request
from flask_restful import Resource


class SellerOrdersController(Resource):

    def __init__(self):
        self.__dao = SellerOrdersDao()

    def get(self, id=None):
        if id:
            model = self.__dao.read(id)
            if model:
                return jsonify(model.to_dict())
            return {}
        return jsonify([sellerorders.to_dict() for sellerorders in self.__dao.read()])

    # create
    def post(self):
        data = request.get_json()
        sellerorders = SellerOrdersModel(**data)
        model = self.__dao.create(sellerorders)
        return self.verify_sql_error(model)

    # update
    def put(self, id):
        data = request.get_json()
        sellerorders = SellerOrdersModel(**data)
        sellerorders.id = id
        model = self.__dao.update(sellerorders)
        return self.verify_sql_error(model)

    # delete
    def delete(self, id=None):
        message = self.__dao.delete(id)
        return jsonify(message)

    def verify_sql_error(self, m):
        if type(m) == SellerOrdersModel:
            return jsonify(m.to_dict())
        return jsonify(m)
