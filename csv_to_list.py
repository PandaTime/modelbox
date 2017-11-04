import csv
from database.database import Database


class CSVFile:

    european_countries = {
        'Austria', 'Belgium', 'Cyprus',
        'Czech Republic', 'Denmark'
        'Estonia', 'Finland', 'France',
        'Germany', 'United Kingdom',
        'Greece', 'Hungary', 'Iceland',
        'Ireland', 'Italy', 'Latvia',
        'Lithuania', 'Luxembourg',
        'Netherlands', 'Norway',
        'Poland', 'Portugal', 'Romania',
        'Slovakia', 'Slovenia', 'Spain',
        'Sweden', 'Switzerland'
    }

    warehouses_coordinates = [
        [0.13228448, 48.85994964],
        [18.48496156, 52.20984462],
        [-7.18939865, 39.78374935],
        [19.62894233, 47.29642355],
        [15.36270296, 58.52179392],
        [13.20315229, 42.27914382],
        [25.9421426, 63.04870051],
        [-21.89500161, 64.13499892],
        [23.08940411, 38.86321707],
        [-0.49323907, 42.07350876],
        [9.10364119, 60.43317088],
        [-3.96711745, 53.98328821],
        [8.05582837, 46.8705798],
        [25.63603837, 45.662058],
        [-18.54521292, 31.75204049],
        [19.24317809, 66.85311598],
        [33.29261738, 34.99216804],
        [14.14465129, 50.40191986],
        [22.32304144, 51.99307471],
        [6.09146493, 51.39510866]
    ]

    def __init__(self, filename):
        self.database = Database()

    def read(self):
        with open('/home/kirill/Desktop/World_Cities.csv') as input_file:
            content = csv.reader(input_file, delimiter=',')
            for row in content:
                if row[8] in CSVFile.european_countries:
                    print("{}, {}".format(row[4], row[8]))
                    print("Longitude: {}".format(row[0]))
                    print("Latitude: {}".format(row[1]))
                    print("Population: {} peoples".format(row[10]))
                    print("Port id: {}\n".format(row[13]))
                    self.database.insert_city(row[4], row[10], row[0], row[1], row[8], row[13])
        self.database.conn.commit()

    @staticmethod
    def write(reader, filename):
        out_file = open(filename, "wb")
        writer = csv.writer(out_file, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(row)
        out_file.close()


if __name__ == "__main__":
    csv = CSVFile()
    csv.read()