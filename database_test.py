from database.database import Database


if __name__ == "__main__":
    db = Database()
    print(db.get_truck(1, 2))
