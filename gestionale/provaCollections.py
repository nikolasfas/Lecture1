import copy
from collections import Counter

from gestionale.core.cliente import ClienteRecord
#from builtins import function

from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Headphones", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello: ")
for i, p in enumerate(carrello):
    print(f"{i+1}. {p.name} - {p.prezzo_unitario}" )

# Aggiungere ad una lista
print(f"="*60)
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key=lambda x: x.prezzo_unitario, reverse=True)
print("Prodotti nel carrello (ordinati): ")
for i, p in enumerate(carrello):
    print(f"{i+1}. {p.name} - {p.prezzo_unitario}" )

print(f"="*60)
tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale nel carrello: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Keyboard", 100.0))
carrello.extend([ProdottoRecord("Phone", 1000.0), ProdottoRecord("Phone case", 20.0)])
carrello.insert(2, ProdottoRecord("Charger", 50.0))

# Rimuovere
carrello.pop() #rimuove ultimo elemento
carrello.pop(2) #rimuovere elemento in posizione 2
carrello.remove(p1) #elimina la prima occorrenza di p1
# carrello.clear() #svuoto la lista

#Sorting
#carrello.sort() # ordina secondo ordine naturale
#carrello.sort(reverse=True) # ordina al contrario
#carrello.sort(key=function)

#carrello_ordinato = sorted(carrello)
carrello.reverse() #restituisce lista al contrario
carrello_copia = carrello.copy() #copia con stessi oggetti lista di partenza - shallow copy
carrello_copia2 = copy.deepcopy(carrello)

#TUPLE
sede_principale = (45, 8) #lat e long della sede di torino
sede_milano = (45, 9) #lat e long della sede di milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")
print(f"Sede Milano lat: {sede_milano[0]}, long: {sede_milano[1]}")

AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)

)
for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

def calcola_statistiche_carrello(carrello):
    # Restituisce prezzo totale, medio, massimo e minimo
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi) )

tot, media, mass, minim = calcola_statistiche_carrello(carrello)
tot, *altricampi = calcola_statistiche_carrello(carrello)

print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
categorie2 = {"Platinum", "Elite", "Gold"}
categorie_all = categorie|categorie2
print(categorie_all)

categorie_comuni = categorie & categorie2
print(categorie_comuni)

categorie_esclusive = categorie - categorie2
print(categorie_esclusive)

categorie_esclusive_symm = categorie ^ categorie2
print(categorie_esclusive_symm)

prodotti_ordine_A = {
    ProdottoRecord("Laptop", 1200.0),
    ProdottoRecord("Mouse", 20.0),
    ProdottoRecord("Headphones", 250.0)
}

prodotti_ordine_B = {
    ProdottoRecord("Laptop2", 1200.0),
    ProdottoRecord("Mouse2", 20.0),
    ProdottoRecord("Headphones2", 250.0)
}

#Metodi utili per i set
s = set()
s1 = set()

#aggiungere
s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiungo più elementi

#togliere
# s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste.
# s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste.
s.pop() #rimuove e restituisce un elemento.
s.clear()

#operazioni insiemistiche
s.union(s1) # s | s1, ovvero genera un set che unisce i due set di partenza
s.intersection(s1) # s & s1, ovvero solo elementi comuni
s.difference(s1) # s-s1, ovvero elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^s1, ovvero elementi di s non contenuti in s1 ed elementi di s1 non contenuti in s

s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) # se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) # se gli elementi di s e quelli di s1 sono diversi


# Dictionary
# Ad ogni oggetto, assegno una chiave con la quale posso richiamarlo
catalogo = {
    "LAP001": ProdottoRecord("Laptop", 1200.0),
    "LAP002": ProdottoRecord("LaptopPro",1500.0),
    "MOU001": ProdottoRecord("Mouse", 20.0),
    "HEA001": ProdottoRecord("Headphones", 250.0)
}

cod = "LAP002"
prod = catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")
# print(f"Cerco un altro oggetto: {catalogo["NonEsiste"]}")

prod1 = catalogo.get("NonEsiste")
if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0))
print(prod2)

# Come iterare su un dizionaro se non so ne le keys, ne i value
keys = catalogo.keys()
values = catalogo.values()

for k in keys:
    print(k)

for v in values:
    print(v)

# Ciclo su coppia chiave - valore
for key, val in catalogo.items():
    print(f"COD: {key} - REF: {val}")

# RImuovere dal dizionario
removed = catalogo.pop("LAP002")
print(removed)

# dict comprehension
prezzi = { codice: prod.prezzo_unitario for codice, prod in catalogo.items() }

# DA RICORDARE PER DICT


""""Esercizio live
    Per ciascuno dei seguenti casi, decidere quale struttura usare: """
# 1) Memorizzare una elenco di ordini che dovranno poi essere processati in ordine di arrivo
ordini = []
ord_1 = Ordine([], ClienteRecord("Mario Rossi", "rossimario@polito.it", "Gold"))
ord_2 = Ordine([], ClienteRecord("Luca Blu", "bluluca@polito.it", "Silver"))
ord_3 = Ordine([], ClienteRecord("Valentino Verdi", "verdivalentino@polito.it", "Bronze"))
ord_4 = Ordine([], ClienteRecord("Marco Marroni", "marronimarco@polito.it", "Gold"))

ordini.append((ord_1, 0))
ordini.append((ord_2, 10))
ordini.append((ord_3, 18))
ordini.append((ord_4, 42))

# 2) Memorizzare i codici fiscali dei clienti (univoco)
codiciFiscali = {"FSSNLS03A05L219M", "SLVFRG05P08245M", "MRCGST88T23G376M"}
print(codiciFiscali)
# 3) Creare un database di prodotti che posso cercare con un codice univoco
listinoProdotti = {"LAP001": ProdottoRecord("Laptop", 1200.0),
                   "KEY001": ProdottoRecord("KeyBoard", 1500.0)}

# 4) Memorizzare le coordinate gps della nuova sede di Roma
magazzino_Roma = (45, 7)

# 5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale
categoriePeriodo = set()
categoriePeriodo.add("Gold")
categoriePeriodo.add("Silver")
categoriePeriodo.add("Bronze")

print("="*60)
#COUNTER
lista_clienti = [
    ClienteRecord("Mario Rossi", "rossimario@polito.it", "Gold"),
    ClienteRecord("Luca Blu", "bluluca@polito.it", "Silver"),
    ClienteRecord("Valentino Verdi", "verdivalentino@polito.it", "Bronze"),
    ClienteRecord("Marco Marroni", "marronimarco@polito.it", "Gold"),
    ClienteRecord("Giovanni Arancio", "aranciogiovanni@polito.it", "Silver"),
    ClienteRecord("Renato Viola", "violarenato@polito.it", "Gold")]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

#stampa
print(f"Distribuzione categorie: {categorie_counter}")
#most common
print(f"Le due categori più frequenti: {categorie_counter.most_common(2)}")
#totals
print(f"Totale: {categorie_counter.total()}")

vendite_Gennaio = Counter({
    "Laptop": 13,  "Tablet": 15
})
vendite_Febbraio = Counter ({
    "Laptop": 3, "Printer": 8
})

vendite_bimestre = vendite_Gennaio + vendite_Febbraio
#Aggregare informazione
print(f"Vendite Gennaio: {vendite_Gennaio}")
print(f"Vendite Febbraio: {vendite_Febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

#Fare la differenza
print(f"Differenza di vendite: {vendite_Gennaio-vendite_Febbraio}")

# Modificare i valori in the fly
vendite_Gennaio["Laptop"] += 4
print(f"Nuove vendite Gennaio: {vendite_Gennaio}")



