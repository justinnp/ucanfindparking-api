from flask import Flask
from flask_restful import Api, Resource, reqparse
from resources.Garages import Garage

app = Flask(__name__)
api = Api(app)


api.add_resource(Garage, "/all")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
