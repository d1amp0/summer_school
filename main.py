from flask import Flask, request, send_file
import json
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./upload"

products = [
    {"id": 0,
     "name": "apple",
     "description": "red"},
    {"id": 1,
     "name": "banana",
     "description": "yellow"}]


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
    for elem in products:
        if elem['id'] == id:
            return json.dumps(elem), 200
    return "Bad Gate", 404


@app.route("/PUT/product/<product_id>", methods=['PUT'])
def put(product_id):
    id = int(product_id)
    for elem in products:
        if elem['id'] == id:
            data = request.get_json()
            if 'name' in data:
                elem['name'] = data['name']
            if 'description' in data:
                elem['description'] = data['description']
            return json.dumps(elem), 200
    return "Bad Gate", 404


@app.route("/DELETE/product/<product_id>", methods=['DELETE'])
def delete(product_id):
    id = int(product_id)
    for elem in products:
        if elem['id'] == id:
            products.remove(elem)
            return json.dumps(elem), 200
    return "Bad Gate", 404


@app.route("/GET/products", methods=['GET'])
def get_all():
    return products, 200


@app.route("/POST/product/<product_id>/image", methods=['POST'])
def post_image(product_id):
    id = int(product_id)
    for elem in products:
        if elem['id'] == id:
            file = request.files['icon']
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            elem['image'] = path
            return "OK", 200
    return "Bad Gate", 404


@app.route("/GET/product/<product_id>/image", methods=['GET'])
def get_image(product_id):
    id = int(product_id)
    for elem in products:
        if elem['id'] == id:
            return send_file(elem['image']), 200
    return "Bad Gate", 404


if __name__ == "__main__":
    app.run()
