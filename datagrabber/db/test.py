#from dbhandler import DBHandler
import sqlite3
from dbhandler import DBHandler

class Test(DBHandler):

    def __init__(self) -> None:
        super().__init__()

    def connect(self, dbPath):
        if self.validator.isEmptyString(dbPath):
            raise ValueError("Not defined DB Path")
        
        self.conn = sqlite3.connect(dbPath)
        self.cursor = self.conn.cursor()

test = Test()
test.connect("")