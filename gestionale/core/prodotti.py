from dataclasses import dataclass


class Prodotto:

    aliquota_iva = 0.22

    def __init__(self ,name: str ,price:  float ,quantity: int ,supplier = None):
        self.name = name
        self._price = None
        self.price = price
        # modo per definire varaibile con livello di sicurezza "_" prima della variabile,
        # oppure due "__" per essere sicuro che non si acceda alla variabile
        self.quantity  = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price *self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto *( 1 +self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str ):
        return cls(name, price, quantity= 1, supplier = supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo *( 1 -percentuale)

    @property
    def price(self): # equivalente al GETTER
        return self._price
    @price.setter # solo se ho definito un GETTER
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione il prezzo non può essere negativo")
            pass
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibilità {self.quantity} pezzi a {self.price}€"

    def __repr__(self):
        return f"Prodotto(nome = {self.name}, price ={self.price}, quantity = {self.quantity}, supplier = {self.supplier})"

    def __eq__(self, other):

        if not isinstance(other, Prodotto):
            return NotImplemented

        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)


    def __lt__(self, other: "Prodotto") -> bool:
        return self.price < other.price

    def prezzo_finale(self):
        return self.price *( 1 +self.aliquota_iva)


class ProdottoScontato(Prodotto): # ereditarietà
    def __init__(self, name: str, price: float, quantity: int, supplier: str, scontoPercento: float):
        # Prodotto.__init__()
        super().__init__(name, price, quantity, supplier)
        self.scontoPercento = scontoPercento

    def prezzo_finale(self) -> float:
        return self.valore_lordo() * ( 1 -self.scontoPercento /100)

class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria: float, num_ore: int):
        super().__init__(name=name, price=tariffa_oraria, quantity=1, supplier = None)
        self.num_ore = num_ore

    def prezzo_finale(self )-> float:
        return self.price * self.num_ore

# Definire una classe Abbonamento che abbia come attributi: "nome, prezzo_mensile, mesi". Abbonamento dovrà avere
# un metodo per calcolare il prezzo finale, ottenuto come prezzo_mensile*mesi

class Abbonamento:
    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile *self.mesi

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

# Per reendere oggetti univoci, come per esempio keys di un dizionario
    def __hash__(self):
        return hash((self.name, self.prezzo_unitario))

    def __str__(self):
        return f"{self.name} -- {self.prezzo_unitario}"

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome:str, prezzo:float):
    return Prodotto(nome, prezzo, quantity=1, supplier= None)


def _test_modulo():

    print("Sto testando il mio modulo!")

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

    print(p3)

    p_a = Prodotto(name= "Laptop", price = 1200, quantity = 12, supplier = "ABC")
    p_b = Prodotto(name= "Mouse", price= 10, quantity= 15, supplier= "CDE")

    print("myproduct1 == p_a?", myproduct1 == p_a) # va  a chiamare metodo __eq__. Mi aspetto TRUE
    print("p_a == p_b?", p_a == p_b) # FALSE

    myList = [p_a, p_b, myproduct1]
    myList.sort()

    for p in myList:
        print(f"- {p}")


# faccio funzione per fare run del mio test delle classi solo se questo file viene utilizzato ALONE
if __name__ == "__main__":
    _test_modulo()






"""
myProductScontato = ProdottoScontato(name= "Auricolari", price=320, quantity = 1, supplier="ABC", scontoPercento = 10)
myService = Servizio(name="Consulenza", tariffa_oraria=100, num_ore = 3)

myList.append(myProductScontato)
myList.append(myService)

myList.sort(reverse=True)

for elem in myList:
    print(elem.name, "-->  ", elem.prezzo_finale() )

print("------------------------------------------------------------------")

abb = Abbonamento(name="Software gestionale", prezzo_mensile = 30.0, mesi=24)

myList.append(abb)
for elem in myList:
    print(elem.name, "-->  ", elem.prezzo_finale())

def calcola_totale(elementi):
    tot = 0
    for e in elementi:
        tot += e.prezzo_finale()
    return tot

print (f"Il  totale è: {calcola_totale(myList)}")

from typing import Protocol

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self) -> float:
        ...

def calcola_totale(elementi: list[HaPrezzoFinale]) -> float:
    return sum(e.prezzo_finale() for e in elementi)
"""