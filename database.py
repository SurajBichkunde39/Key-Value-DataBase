import json
import os


class Database(object):
    """
    All the database related actions can be taken from here
    """

    def __init__(self):
        pass

    def create(self, path=os.getcwd()):
        """
        Check the given path is valid or not
        """
        empty_database = {}
        filename = os.path.join(path, "my_db.json")
        with open(filename, "w") as new_db:
            json.dump(empty_database, new_db)

    def load(self, path):
        self.db_file = open(path, "r+")
        self.db = json.load(self.db_file)

    def close(self):
        self.db_file.close()

    def commit(self):
        self.db = json.dumps(self.db)
        json.dump(self.db, self.db_file)

    def read(self, key):
        try:
            return dict(self.db[key])
        except:
            return "Error:key Not found"

    def write(self, key, value):
        self.db[key] = value
        return "Done"

    def delete(self, key):
        try:
            del self.db[key]
        except:
            return "Error:key Not found"
