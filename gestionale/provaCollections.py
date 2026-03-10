import copy
#from builtins import function

from gestionale.core.prodotti import ProdottoRecord

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

tot, media, max, min = calcola_statistiche_carrello(carrello)
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

#Metodi utili
s = set()

s.add(ProdottoRecord("aaa", 20.0))
s.update([ProdottoRecord("aaa", 20.0),ProdottoRecord("bbb", 20.0)])

#togliere
s.remove(elem) #rimuove un elemento. Raise KeyError se non esiste
s.discard(elem) #rimuove un elemento, senza "arrabbiarsi" se questo non esiste
s.pop()
s.clear()