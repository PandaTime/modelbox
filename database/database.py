import sqlalchemy


class Database:

    def __init__(self, dbname='postgres', user='postgres', host='localhost', password='pass', port=5432):
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, dbname)
        self.con = sqlalchemy.create_engine(url, client_encoding='utf8')
        self.meta = sqlalchemy.MetaData(bind=self.con, reflect=True)

    def create_warehouse(self, longitude, latitude, capacity=88, cost_of_service=5000):
        clause = self.meta.tables['regional_warehouses'].insert().values(
            longitude=longitude, latitude=latitude, capacity=capacity, cost_of_service=cost_of_service)
        self.con.execute(clause)

    def create_city(self, name, longitude, latitude, population, country, port_id, warehouse_id):
        clause = self.meta.tables['cities'].insert().values(
            name=name, longitude=longitude, latitude=latitude, population=population,
            country=country, port_id=port_id, warehouse_id=warehouse_id)
        self.con.execute(clause)

    def create_port(self, port_id, cost_of_shipping_to_us=400, cost_of_shipping_to_china=500):
        clause = self.meta.tables['ports'].insert().\
            values(port_id=port_id, cost_of_shipping_to_us=cost_of_shipping_to_us,
                   cost_of_shipping_to_china=cost_of_shipping_to_china)
        self.con.execute(clause)

    def create_dealer(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
