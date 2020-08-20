from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from app.controller.selller_order_controller

app = Flask(__name__)
api = Api(app)
cord = CORS(app)

@app.route('/')
def initial():
    return ''
from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from app.controller.selller_order_controller import SellerOrderController

app = Flask(__name__)
api = Api(app)
cord = CORS(app)

@app.route('/')
def initial():
    return ''

api.add_resource(
    SellerOrderController, '/api/sellers_order/', '/api/sellers_order/<id>', endpoint = 'sellers_order'
)

app.run(debug=True)
from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from app.controller.selller_order_controller

app = Flask(__name__)
api = Api(app)
cord = CORS(app)

@app.route('/')
def initial():
    return ''

api.add_resource(
    '/api/sellers_order/', '/api/sellers_order/<int:id>', endpoint = 'sellers_order'
)

app.run(debug=True)