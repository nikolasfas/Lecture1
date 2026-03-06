from gestionale.core.cliente import Cliente, ClienteRecord
from gestionale.vendite.ordini import Ordine, OrdineConSconto, RigaOrdine
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard

print("==================================")
p1 = Prodotto(name= "Ebook Reader", price= 120, quantity= 1, supplier="AAA" )
p2 = crea_prodotto_standard(nome="Tablet", prezzo=750)

print(p1)
print(p2)

print("==================================")

c1 = Cliente(name="Mario Rossi", email="mariorossi@gmail.com", categoria="Gold")
print(c1.descrizione())

print("==================================")
print("--------------------------------------------------------------------")

#MODI PER IMPORTARE
#1)

#2)
from gestionale.core.prodotti import ProdottoScontato as ps
p3= ps(name="Auricolari", price=230, quantity=1, supplier="ABCC", scontoPercento=0.1)
print(p3)

#3)
from gestionale.core import prodotti
from gestionale.core import prodotti as p

p4 = prodotti.ProdottoScontato(name="Auricolari", price=230, quantity=1, supplier="ABCC", scontoPercento=0.1)

#4)
p5 = p.ProdottoScontato(name="Auricolari", price=230, quantity=1, supplier="ABCC", scontoPercento=0.1)



cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = prodotti.ProdottoRecord("Laptop", 1200.0)
p2 = prodotti.ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1, 2), RigaOrdine(p2, 10)], cliente1)

ordine_scontato = OrdineConSconto([RigaOrdine(p1, 2), RigaOrdine(p2, 10)], cliente1, 0.1)

print(ordine)
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Toale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto: ", ordine_scontato.totale_netto())
print("Toale lordo (IVA 22%): ", ordine_scontato.totale_lordo(0.22))


# Nel package gestionale, scriviamo un modulo fatture.py che contenga:
# - una classe Fattura che contiene un Ordine, un numero fattura e una data
# - un metodo genera_fattra() che restitusisce una stringa formattata con tutte le info della fattura
