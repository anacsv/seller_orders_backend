from app.dao.selller_order_dao import SellerOrderDao
from app.model.selller_order_model import SellerOrderModel
from flask import jsonify, request
from flask_restful import Resource

class SellerOrderController(Resource):

    def __init__(self):
        self.__dao = SellerOrderDao()

    def get(self, id = None):
        if id:
            model = self.__dao.read(id)
            if model:
                return jsonify(model.to_dict())
            return {}
        return jsonify([sellerorder.to_dict() for sellerorder in self.__dao.read()])

    def post(self):
        data = request.get_json()
        sellerorder = SellerOrderModel(**data)
        sellerorder.id = id
        model = self.__dao.create(sellerorder)
        return jsonify(model.to_dict())

    def put(self, id):
        data = request.get_json()
        sellerorder = SellerOrderModel(**data)
        sellerorder.id = id
        model = self.__dao.update(sellerorder)
        return jsonify(model.to_dict())

    def delete(self, id):
        msg = self.__dao.delete(id)
        return jsonify(msg)