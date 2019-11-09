# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask import render_template
import json
from server_functions import load_acidentes, load_faixas, load_corredores, load_radares, load_ciclovias

app = Flask(__name__, static_url_path='', 
            static_folder='static')
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")
 
class Acidentes(Resource):
    def get(self):
        args = request.args
        tipo = args['tipo']
        return load_acidentes(tipo).to_json(orient='records')

class Radares(Resource):
    def get(self):
        return load_radares().to_json(orient='records')

class Faixas(Resource):
    def get(self):
        return load_faixas().to_json()

class Corredores(Resource):
    def get(self):
        return load_corredores().to_json()

class Ciclovias(Resource):
    def get(self):
        return load_ciclovias().to_json()

api.add_resource(Acidentes, '/acidentes', )
api.add_resource(Faixas, '/faixas')
api.add_resource(Corredores, '/corredores')
api.add_resource(Radares, '/radares')
api.add_resource(Ciclovias, '/ciclovias')

if __name__ == '__main__':
     app.run(port='5005')