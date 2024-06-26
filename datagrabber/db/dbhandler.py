from  datagrabber.helper.validator import Validator

class DBHandler:

    def __init__(self) -> None:
        self.validator = Validator()
        self.conn = None
        self.cursor = None

    def connect(self, dbPath):
        pass