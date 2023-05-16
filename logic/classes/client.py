import json
from logic.classes.person import Person


class Client (Person):
    """
    A class that represents a Client
    """

    def __init__(self,
                 id: int = 0,
                 name: str = 'name',
                 last_name: str = 'last_name',
                 phone: str = 'phone',
                 mail: str = 'mail') -> object:
        """
        Constructor of the class
        :param id: the id of the Client
        :type id: int
        :param name: the name of the Client
        :type name: str
        :param last_name: the last name of the Client
        :type last_name: str
        :param phone: the phone of the Client
        :type phone: str
        :param mail: the mail of the Client
        :type mail: str
        """
        super().__init__(id, name, last_name, phone, mail)

    def __str__(self) -> dict:
        """
        String representation of the Client
        :return: a string containing the Client
        :rtype: str
        """
        return {"id": self.id,
                "name": self.name,
                "last_name": self.last_name,
                "phone": self.phone,
                "mail": self.mail}

    def __eq__(self, other: object) -> bool:
        """
        Checks if two Clients are equal
        :param other: the other Client
        :type other: object
        :return: True if the Clients are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Client):
            return self.id == other.id
        return False


if __name__ == '__main__':
    client = Client(1, 'name', 'last_name', 'phone', 'mail')
    client2 = Client(1, 'name', 'last_name', 'phone', 'mail')
    print(json.dumps(client.__str__()))

    print('client1 == client2') if client == client2 else print(
        'client1 != client2')
