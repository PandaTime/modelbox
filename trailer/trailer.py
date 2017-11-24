import json

class Trailer:
    def __init__(self, id, city_from, city_to, status, rfid):
        self.id = id
        self.city_from = city_from
        self.city_to = city_to
        self.status = status
        self.rfid = rfid

    # accelerometer
    def set_x_acceleration(self, x_acceleration):
        self.x_acceleration = x_acceleration

    def set_y_acceleration(self, y_acceleration):
       self.y_acceleration = y_acceleration

    def set_z_acceleration(self, z_acceleration):
        self.z_acceleration = z_acceleration

    # hyroscope
    def set_x_orientation(self, x_orientation):
       self.x_orientation = x_orientation

    def set_y_orientation(self, y_orientation):
        self.y_orientation = y_orientation

    def set_z_orientation(self, z_orientation):
        self.z_orientation = z_orientation

    def set_doors_open(self, doors_open):
        self.doors_open = doors_open

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)