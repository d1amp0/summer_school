from flask import Flask, request
import json

app = Flask(__name__)

products = [
    {"id": 0,
     "name": "apple",
     "description": "red"}]


@app.route("/")
def index():
    pass


@app.route("/POST/product", methods=['POST'])
def post():
    data = request.get_json()
    if len(products) != 0:
        new = {"id": products[-1]["id"] + 1,
               "name": data['name'],
               "description:": data['description']
               }
    else:
        new = {"id": 0,
               "name": data['name'],
               "description:": data['description']
               }
    products.append(new)
    return json.dumps(new), 200


@app.route("/GET/product/<product_id>", methods=['GET'])
def get(product_id):
    id = int(product_id)
    if id >= len(products):
        return "Bad Gate", 404
    else:
        return json.dumps(products[id]), 200


@app.route("/PUT/product/<product_id>", methods=['PUT'])
def put(product_id):
    id = int(product_id)
    if id >= len(product_id):
        return "Bad Gate", 404
    else:
        data = request.get_json()
        if 'name' in data:
            products[id]['name'] = data['name']
        if 'description' in data:
            products[id]['description'] = data['description']
        return json.dumps(products[id]), 200


@app.route("/DELETE/product/<product_id>", methods=['DELETE'])
def delete(product_id):
    id = int(product_id)
    if id >= len(product_id):
        return "Bad Gate", 404
    else:
        return json.dumps(products.pop(id)), 200


@app.route("/GET/products", methods=['GET'])
def get_all():
    return products, 200


if __name__ == "__main__":
    app.run()
