from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.controller.seller_order_controller import SellerOrderController

app = Flask(__name__)
api = Api(app)
cord = CORS(app)


@app.route('/')
def initial():
    return ''


api.add_resource(SellerOrderController, '/api/sellers-order/', '/api/sellers-order/<id>', endpoint='sellers-order')

app.run(debug=True)