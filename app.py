from flask import Flask
from flask_restful import Api, Resource, reqparse

import scraper

app = Flask(__name__)
api = Api(app)

class Garage(Resource):

    def get(self):
        return scraper.get_avail(), 200

api.add_resource(Garage, "/all")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
