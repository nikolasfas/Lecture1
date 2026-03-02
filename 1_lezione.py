

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
        return self.price*(1+self.aliquota_iva)


class ProdottoScontato(Prodotto): # ereditarietà
    def __init__(self, name: str, price: float, quantity: int, supplier: str, scontoPercento: float):
        #Prodotto.__init__()
        super().__init__(name, price, quantity, supplier)
        self.scontoPercento = scontoPercento

    def prezzo_finale(self) -> float:
        return self.valore_lordo() * (1-self.scontoPercento/100)

class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria: float, num_ore: int):
        super().__init__(name=name, price=tariffa_oraria, quantity=1, supplier = None)
        self.num_ore = num_ore

    def prezzo_finale(self)-> float:
        return self.price * self.num_ore



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

myProductScontato = ProdottoScontato(name= "Auricolari", price=320, quantity = 1, supplier="ABC", scontoPercento = 10)
myService = Servizio(name="Consulenza", tariffa_oraria=100, num_ore = 3)

myList.append(myProductScontato)
myList.append(myService)

myList.sort(reverse=True)

for elem in myList:
    print(elem.name, "-->  ", elem.prezzo_finale() )

print("------------------------------------------------------------------")

# Definire una classe Abbonamento che abbia come attributi: "nome, prezzo_mensile, mesi". Abbonamento dovrà avere
# un metodo per calcolare il prezzo finale, ottenuto come prezzo_mensile*mesi

class Abbonamento:
    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile*self.mesi

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

print("--------------------------------------------------------------------")
print("Sperimentiamo con dataclass")

from dataclasses import dataclass

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

@dataclass
class ClienteRecord:
    name: str
    email:str
    categoria: str

@dataclass
class RigaOrdine:
    prodotto: ProdottoRecord
    quantita: int

    def totale_riga (self):
        return self.prodotto.prezzo_unitario * self.quantita

@dataclass
class Ordine:
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)

    def totale_lordo(self, aliquota_iva):
        return self.totale_netto()*(1+aliquota_iva)

    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineConSconto(Ordine):
    sconto_percentuale: float

    def totale_scontato(self):
        return self.totale_lordo()*(1-self.sconto_percentuale)

    def totale_netto(self):
        netto_base = super().totale_netto()
        return netto_base*(1-self.sconto_percentuale)

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1, 2), RigaOrdine(p2, 10)], cliente1)

ordine_scontato = OrdineConSconto([RigaOrdine(p1, 2), RigaOrdine(p2, 10)], cliente1, 0.1)

print(ordine)
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Toale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto: ", ordine_scontato.totale_netto())
print("Toale lordo (IVA 22%): ", ordine_scontato.totale_lordo(0.22))





print("--------------------------------------------------------------------")
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
# client2 = Cliente(name="Carlo Verdi", email= "carloverdi@google.com", categoria="Platinum")
print(client1.descrizione())
# nomeOggetto.metodo