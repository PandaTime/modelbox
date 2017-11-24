import json
import random

from flask import Flask
from flask import render_template
from roads.roads import Road
from trailer.trailer import Contract

class Application:

    def __init__(self):
        self.app = Flask(__name__)
        self.add_routing()

    def index(self):
        return render_template("index.html")

    def configure(self):
        return render_template("configure.html")

    def get_contracts(self):
        return toJSON(contracts)

    def add_routing(self):
        self.add_endpoint(endpoint='/get_route/<longitude_from>/<latitude_from>/<longitude_to>/<latitude_to>',
                          endpoint_name='main', handler=Road.get_duration_and_distance)

        self.add_endpoint(endpoint='/index',
                      endpoint_name='index', handler=self.index)

        self.add_endpoint(endpoint='/configure',
                          endpoint_name='configure', handler=self.configure)

        self.add_endpoint(endpoint='/get_trailers', endpoint_name='get_trailers', handler=self.get_contracts)

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler)


def toJSON(object):
    return json.dumps(object, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)

def add_contracts():
    for number in range(0,50):
        contract = Contract(str(number), cities[random.randint(0,47)], cities[random.randint(0,47)], 'OK')
        contracts.append(contract)


cities = [
    'London', 'Berlin' 'Madrid',
    'Rome', 'Paris', 'Bucharest',
    'Hamburg', 'Warsaw', 'Budapest',
    'Barcelona', 'Vienna', 'Munich',
    'Stockholm', 'Prague', 'Copenhagen',
    'Dublin', 'Brussels', 'Naples',
    'Birmingham', 'Cologne', 'Turin',
    'Valencia', 'Marseille', 'Lodz',
    'Krakow', 'Riga', 'Amsterdam',
    'Athens', 'Seville', 'Palermo',
    'Frankfurt', 'Zaragoza', 'Wroclaw',
    'Glasgow', 'Genoa', 'Rotterdam',
    'Essen', 'Dortmund', 'Oslo',
    'Dusseldorf', 'Poznan', 'Helsinki',
    'Bremen', 'Vilnius', 'Lisbon',
    'Goteborg', 'Hannover', 'Leipzig',
    'Duisburg'
]
contracts = []

if __name__ == "__main__":
    app = Application()

    print(len(cities))

    add_contracts()

    app.run()

