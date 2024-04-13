
class DbHandler:
    @staticmethod
    def write_to_file(data):
        with open("database.txt", mode="a") as my_db:
            my_db.write(f"{data}")
