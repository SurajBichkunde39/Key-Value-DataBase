import os
import json
import pickle
import time
from pprint import pprint

from database import Database

info_string = """
Welcome to the Simplest Key-Value based database
You can perform two major operations with the database.
1] Read Data from database
2] Write data in the database
Let's see the query syntax for both
**************************************
*** Reading Data From The DataBase ***
**************************************
query---> read
    Enter read following with the key you have
    for example if your key 'kapil' you will give command 'read kapil'
    you will get the result if you have that key persent database.
    {
        "Name":"Kapil",
        "age":"19",
        "address":"Rajneel park, dutal socity, keshavnagar, Pune"
        "odders placed":"19",
        "cancled orders":"22"
    }
    And if you do not have that key present in the database you will get the error msg saying.
    Error:Key is not present in database
**************************************
***   Writing Data Into DataBase   ***
**************************************
query --> write
    Data is stored in json format, so we have to enter the valied json format to correctly evealuate the query
    write kapil 
    {
        "Name":"Kapil",
        "age":"19",
        "address":"Rajneel park, dutal socity, keshavnagar, Pune"
        "odders placed":"19",
        "cancled orders":"22"
    }
    You can omit all the spaces and add everitning in one line also but you have to follow the json convensions
    If the key is already present in the database, you will get the error as,
    Error:Key is already present in the database, please use the different key

***************************************
***   Deleting data from database   ***
***************************************
query --> delete
    delete key from the database
    if the key is not present in the database you will get the error msg as
    Error:key not Found

"""


class Keyvaldb(object):
    def __init__(self):
        self.db = Database()
        self.check_and_do_setup()
        self.get_the_db_path()
        self.db.load(self.db_path)

    def get_the_db_path(self):
        self.db_path = None
        with open("config_file.txt", "rb") as config_file:
            config_ = pickle.load(config_file)
            self.db_path = config_["db_path"]

    def check_and_do_setup(self):
        cur_dir = os.listdir()
        if "config_file.txt" not in cur_dir:
            from setup import Config

            _ = Config()
            self.detailed_info()
        else:
            self.instructions_info()

    # def query_final(self):
    #     # lines = []
    #     first_line = input()
    #     if "read" in first_line:
    #         first_line = first_line.strip()
    #         query_temp = first_line.split()
    #         if len(query_temp) == 2:
    #             _, key = first_line
    #             self.db.load(self.db_path)
    #             return self.db.read(key)
    #         else:
    #             self.query_again(
    #                 msg="Possible Correction -> read query contains only two words, 'read' amd '[Key]' "
    #             )
    #     elif "write" in first_line:
    #         pass
    #     else:
    #         self.query_again()

    def query(self):
        print("choose action")
        action = input()
        action = action.strip()
        action = action.lower()
        if action == "read":
            self.read_query()
        elif action == "write":
            self.write_query()
        elif action == "delete":
            self.delete_query()
        else:
            self.query_again()

    def query_again(self, msg=""):
        print("Invalied Query")
        if len(msg) > 2:
            print(msg)
        print("please read the instructions carefully")
        self.instructions_info()
        self.query()

    def read_query(self):
        print("Enter the key")
        key = input()
        result = self.db.read(key=key)
        self.display_result(result)

    def write_query(self):
        print("Enter the key")
        key = input()
        print("Enter the value in json format")
        lines = []
        while True:
            line = input()
            lines.append(line)
            if line[-1] == "}":
                break
        value = "".join(lines)
        try:
            _ = json.loads(value)
            result = self.db.write(key, value)
            self.display_result(result)
        except:
            print("Something is wrong. Try Again")
            self.write_query()

    def delete_query(self):
        print("Enter the key to delete record")
        key = input()
        result = self.db.delete(key)
        self.display_result(result)

    def display_result(self, result):
        pprint(result)

    def db_info(self):
        pass

    def detailed_info(self):
        for line in info_string.split("\n"):
            print(line)
            time.sleep(0.1)
        self.instructions_info()

    def instructions_info(self):
        print("Instructions to query the database")
        print("for reading entry from the database   --> read")
        print("for writing the value to the database --> write")
        print("For deleting entry in the database    --> delete")
        print("for detailed information              --> help")


def main():
    db = Keyvaldb()
    db.query()
    db.db.commit()
    while True:
        repeat = input("Try another query (y/n)")
        repeat = repeat.lower()
        if repeat == "y":
            db.query()
            db.db.commit()
        else:
            break
    db.db.close()


if __name__ == "__main__":
    main()