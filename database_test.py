from database.database import Database


if __name__ == "__main__":
    db = Database()
    clause = db.meta.tables['regional_warehouses'].insert().values(warehouse_id=1, longitude=1, latitude=1, capacity=1, cost_of_service=1)
    db.con.execute(clause)