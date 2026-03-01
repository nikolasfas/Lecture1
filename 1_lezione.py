

class Prodotto:

    aliquota_iva = 0.22

    def __init__(self,name: str,price:  float,quantity: int,supplier = None):
        self.name = name
        self._price = None
        self.price = price
        # modo per definire varaibile con livello di sicurezza "_" prima della variabile,
        # oppure due "__" per essere sicuro che non si acceda alla variabile
        self.quantity  = quantity
        self.supplier = supplier

    def valore_netto(self):
         return self._price*self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto*(1+self.aliquota_iva)
        return lordo
    
    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str ):
       return cls(name, price, quantity= 1, supplier = supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)

    @property
    def price(self): # equivalente al GETTER
        return self._price
    @price.setter #solo se ho definito un GETTER
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione il prezzo non può essere negativo")
            pass
        self._price = valore



myproduct1 = Prodotto(name= "Laptop", price=1200, quantity = 12, supplier="ABC")
# definisco la variabile con tutti '=' se non ricordo l'ordine oppure con tutti ':'
print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1._price}")
print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}")

myproduct2 = Prodotto(name= "Mouse", price=10, quantity = 25, supplier="DEF")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2._price}")

print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
Prodotto.aliquota_iva = 0.24
print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")

p3 = Prodotto.costruttore_con_quantità_uno(name="Auricolari", price= 200.0, supplier="ABC")
# nomeClasse.metodo
print(f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1._price, percentuale=0.15)}")

# classe cliente con proprità "categoriaa" sia protetta e accetti solo ("Gold", "Silver", "Bronze")

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
        categorieValide = {"Gold", "Silver", "Bronze"}
        if categoria not in categorieValide:
            raise ValueError("Attenzione, categoria invalida. Scegliere fra Gold, Silver, Bronze")
        self._categoria = categoria

client1 = Cliente(name="Fulvio Bianchi", email= "fulviobianchi@google.com", categoria="Gold")
client2 = Cliente(name="Carlo Verdi", email= "carloverdi@google.com", categoria="Platinum")
print(client1.descrizione())
# nomeOggetto.metodo