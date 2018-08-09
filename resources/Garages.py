from flask_restful import Resource
from resources.scraper import get_avail

class Garage(Resource):

    def get(self):
        return get_avail(), 200
