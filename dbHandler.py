import csv
import os


class DbHandler:

    @staticmethod
    def write_to_file(data):
        with open("database.txt", mode="a") as my_db:
            my_db.write(f"{data}")

    '''@staticmethod
    def write_to_csv(data):
        field_names = ["name", "email", "message"]
        file_exists = os.path.isfile("database.csv")
        with open("database.csv", mode="w") as my_db:
            writer = csv.DictWriter(my_db, fieldnames=field_names)
            not file_exists and writer.writeheader()
            writer.writerow(data)'''

    @staticmethod
    def write_to_csv(data):
        field_names = ["name", "email", "message"]
        file_exists = os.path.isfile("database.csv")
        with open("database.csv", mode="a+", newline="") as my_db:
            writer = csv.DictWriter(my_db, fieldnames=field_names)

            my_db.seek(0)

            if not file_exists or len(my_db.readlines()) == 0:
                writer.writeheader()

            my_db.seek(0, os.SEEK_END)

            writer.writerow(data)
