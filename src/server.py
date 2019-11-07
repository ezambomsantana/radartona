# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from flask import render_template
import json
from server_functions import load_acidentes

app = Flask(__name__, static_url_path='', 
            static_folder='static')
api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")
 
class Acidentes(Resource):
    def get(self):
        args = request.args
        tipo = args['tipo']
        return load_acidentes(tipo).to_json(orient='records')

api.add_resource(Acidentes, '/acidentes')

if __name__ == '__main__':
     app.run(port='5002')