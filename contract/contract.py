import json

class Contract:
    def __init__(self, id, city_from, city_to):
        self.id = id
        self.city_from = city_from
        self.city_to = city_to

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)