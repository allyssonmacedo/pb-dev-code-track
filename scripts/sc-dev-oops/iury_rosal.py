## Associação
## um atributo que vai ser um método de outra classe

class PubCompany:
    def __init__(self, name_company, cnpj) -> None:
        self.name_company = name_company
        self.cnpj = cnpj

    def get_cnpj(self):
        return self.cnpj
    
class Book:
    def __init__(self, title: str, pub_company: PubCompany) -> None:
        self.title = title
        self.pub_company = pub_company

pubcompanySaraiva = PubCompany('saraiva', '1234')
book = Book('Livro1', pubcompanySaraiva)
print(book.pub_company.get_cnpj())

## se apagar o book, nao vai apagar a pubcompany 


#####
##Agregação

class Cart:
    def __init__(self) -> None:
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(f'{product.name} {product.value}\n')


class Product:
    def __init__(self, product_name, product_value) -> None:
        self.name = product_name
        self.value = product_value

p1 = Product('caneta', 2)
p2 = Product('caderno', 50)

cart = Cart()
cart.insert_product(p1)
cart.insert_product(p2)
cart.list_products()