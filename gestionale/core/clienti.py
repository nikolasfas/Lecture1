from dataclasses import dataclass


@dataclass
class ClienteRecord:
    name: str
    email:str
    categoria: str

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email


    def __str__(self):
        return f"Cliente {self.name} ({self.categoria}) - {self.email}"