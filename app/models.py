

class Users:
    def __init__(self, name, id_message, post) -> None:
        self.name = name
        self.__id_message = id_message
        self.post = post

    def get_id_user(self):
        return f'{self.__id_message}'
    
    def add_user(self, name_user, id_message, post) -> object:
        pass
