from dataclasses import dataclass

class Person:
    def __init__(self, person_first_name, person_last_name, person_age) -> None:
        self.first_name = person_first_name
        self.last_name = person_last_name
        self.age = person_age

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass

    def __eq__(self, __value: object) -> bool:
        pass


@dataclass ## tem parametros do dataclass()
class PersonDataclass:
    first_name: str
    last_name: str
    age: int = 22
    full_name: str = None

    def __post_init__(self):
        self.full_name = self.first_name + self.last_name


person = PersonDataclass("Nome", "Sobrenome", 22)
print(person)
print(repr(person))

### faz tudo isso da classe acima
