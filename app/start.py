from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.controller.seller_orders_controller import SellerOrdersController

app = Flask(__name__)
api = Api(app)
cord = CORS(app)


@app.route('/')
def initial():
    return ''


api.add_resource(SellerOrdersController, '/api/seller-orders/', '/api/seller-orders/<id>', endpoint='seller-orders')

app.run()