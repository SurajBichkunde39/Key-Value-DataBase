import os
import pickle

from database import Database

class Config(object):
    def __init__(self):
        self.create_empty_database()
        self.initlilize_db()

    def create_empty_database(self):
        self.config_file = {}
        self.db = Database()
    
    def initlilize_db(self):
        print("where do you want to create your database (press '.' to use default location) ")
        print("Note - please type full path to desired directory")
        db_path = input()
        if db_path == '.':
            self.db.create()
            self.update_config_file(db_path = os.getcwd())
        else:
            if os.path.isdir(db_path):
                self.db.create(path = db_path)
                self.update_config_file(db_path = db_path)
            else:
                print("Please Enter the valid path")


    def update_config_file(self, db_path = '.'):
        self.config_file['db_path'] = os.path.join(db_path,'my_db.json')
        with open('config_file.txt','wb') as config_file:
            pickle.dump(self.config_file, config_file)        
