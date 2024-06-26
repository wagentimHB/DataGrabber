#from dbhandler import DBHandler
import sqlite3
from datagrabber.validator import Validator

class SqliteHandler():

    def __init__(self) -> None:
        self.validator = Validator()

    def connect(self, dbPath):
        if self.validator.isEmptyString(dbPath):
            raise ValueError("Not defined DB Path")
        
        self.conn = sqlite3.connect(dbPath)
        self.cursor = self.conn.cursor()