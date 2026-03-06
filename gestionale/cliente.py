from dataclasses import dataclass

print("--------------------------------------------------------------------")
# classe cliente con proprità "categoriaa" sia protetta
# e accetti solo ("Gold", "Silver", "Bronze")

categorieValide = {"Gold", "Silver", "Bronze"}

class Cliente:
    def __init__(self, name: str, email: str, categoria: str):
        self.name = name
        self.email = email
        self._categoria = None
        self.categoria = categoria #presupposne per SETTER e GETTER

    def descrizione(self):
        return  f"Cliente {self.name} ({self.categoria}) - {self.email}"

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        if categoria not in categorieValide:
            raise ValueError("Attenzione, categoria invalida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria

def _test_modulo():
    client1 = Cliente(name="Fulvio Bianchi", email= "fulviobianchi@google.com", categoria="Gold")
    # client2 = Cliente(name="Carlo Verdi", email= "carloverdi@google.com", categoria="Platinum")
    print(client1.descrizione())
    # nomeOggetto.metodo

@dataclass
class ClienteRecord:
    name: str
    email:str
    categoria: str

if __name__ == "__main__":
    _test_modulo()