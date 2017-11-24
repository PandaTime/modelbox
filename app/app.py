import json
import random

from threading import Thread
from time import sleep
from flask import Flask
from flask import render_template
from roads.roads import Road
from trailer.trailer import Trailer

class Application:

    def __init__(self):
        self.app = Flask(__name__)
        self.add_routing()

    def index(self):
        return render_template("index.html")

    def configure(self):
        return render_template("configure.html")

    def get_contracts(self):
        return toJSON(trailers)

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
        trailer = Trailer(str(number), cities[random.randint(0,47)], cities[random.randint(0,47)], 'OK')
        trailers.append(trailer)

def add_trailer(id, city_from, city_to, status, rfid, longitude, latitude):
    trailer = Trailer(id, city_from, city_to, status, rfid, longitude, latitude)
    trailer.acquire_telemetry()
    trailer.set_doors_open('closed')
    thread = Thread(target=monitor, args=(1,))
    thread.start()


def monitor(number_of_trailer):
    while True:
        print('check trailer {}'.format(number_of_trailer))
        sleep(1)



    trailers.append(trailer)

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
trailers = []

if __name__ == "__main__":
    app = Application()

    print(len(cities))

    add_trailer('123', 'Essen', 'Dortmund', 'ADDED', 1234, 45.2, 23.4)

    app.run()

