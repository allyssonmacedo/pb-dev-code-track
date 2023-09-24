## Client and address

class Address:
    def __init__(self, streat, house_number) -> None:
        self.streat = streat
        self.house_number = house_number

    def get_address(self):
        return f'{self.streat}, {self.house_number}'
    
    def change_address(self, new_streat, new_house_number):
        self.streat = new_streat
        self.house_number = new_house_number

    

class Client:
    def __init__(self, client_name: str, client_address: Address) -> None:
        self.name = client_name
        self.address = client_address

    def change_address(self, new_name):
        self.name = new_name

marcos_add = Address('Rua Luiz Correia', 999)
marcos_cli = Client('Marcos', marcos_add)

print(marcos_cli.address.get_address())