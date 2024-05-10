




class Token:
    def __init__(self, token) -> None:
       self.__token = token

    def get_token(self) -> str:
        return self.__token

    def __repr__(self) -> str:
        return f'{self.__token}'
       
    
    
test_token = Token('6105146346:AAFcm1CVVly8GllMD_KXDBw0iF20x6RiW8g')

