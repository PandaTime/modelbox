import psycopg2


class Database:

    def __init__(self, dbname='postgres', user='postgres', host='localhost', password='pass'):

        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password

        self.connect()
        self.cur = self.conn.cursor()

    def connect(self):
        try:
            self.conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'"
                                         .format(self.dbname, self.user, self.host, self.password))
        except ConnectionError:
            print("Unable to connect to the database")
            exit(1)

    def insert_city(self, name, population, longitude, latitude, country, port_id):
        try:
            self.cur.execute("INSERT INTO cities (NAME, POPULATION, LONGITUDE, LATTITUDE, COUNTRY, PORT_ID)"
                    "VALUES (%s, %s, %s, %s, %s, %s)", (name, population, longitude, latitude, country, port_id))
        except Exception:
            print("Cannot insert")
