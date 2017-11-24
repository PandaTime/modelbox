import json

from flask import Flask
from flask import render_template
from roads.roads import Road
from contract.contract import Contract

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

        self.add_endpoint(endpoint='/get_contracts', endpoint_name='get_contracts', handler=self.get_contracts)

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler)

contracts = []

def toJSON(object):
    return json.dumps(object, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)



if __name__ == "__main__":
    app = Application()

    contract = Contract('12345', 'from', 'to')
    contracts.append(contract)

    contract = Contract('qwerty', 'from1', 'to1')
    contracts.append(contract)

    app.run()

