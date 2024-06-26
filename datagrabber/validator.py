class Validator:

    def __init__(self) -> None:
        pass

    def isEmptyString(self, input):
        if input is None:
            return True
        
        temp = str(input).strip()

        if not temp:
            return True
        
        return False