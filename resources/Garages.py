from flask_restful import Resource
from resources.scraper import get_avail

class Garages(Resource):
    def get(self):
        return get_avail()
