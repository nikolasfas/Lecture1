# Scrivere un software gestonale che abbia le seguenti caratteritiche
# 1) Supportare l'arrivo e la gestioone di ordini
# 2) Quando arriva un nuovo ordine, lo aggiungo ad una coda,
#       assicurandomi che sia seguita da
from collections import deque, Counter, defaultdict

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdine:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def add_ordine(self, ordine: Ordine):

        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def processo_prossimo_ordine(self):
        if not self._ordini_da_processare:
            print(f"Non ci sono ordini in coda.")
            return False

        ordine = self._ordini_da_processare.popleft() #logica FIFO
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        self._ordini_per_categoria[ordine.cliente.categoria]

    def processa_tutti_gli_ordini(self):
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processo_prossimo_ordine()
        print("Tutti gli ordini sono stati processati")

    def get_statistiche_prodotti(self, top_n: int=5):
        valori = []
        for prodotto, quantità in self._statistiche_prodotti.most_common(top_n):
            valori.append(prodotto, quantità)
        return valori

    def get_distribuzione_categorie(self):
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum(o.totale_lordo(0.22) for o in ordini)
            valori.append(cat, totale_fatturato)
        return valori

    def stampa_riepilogo(self):
        print("\n"+"-"*60)
        print("Stato  attuale del business: ")
        print("Oridni ")

def test_modulo():
    sistema = GestoreOrdine()

    ordini = [
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)
        ], ClienteRecord("Laura Pausini", "pausinilaura@polito.it", "Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3),
            RigaOrdine(ProdottoRecord("Headphones", 45.0), 2)
        ], ClienteRecord("Francesco Renga", "rengafrancesco@polito.it", "Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3),
            RigaOrdine(ProdottoRecord("Headphones", 45.0), 2),
            RigaOrdine(ProdottoRecord("Keyboard", 25.0), 3)
        ], ClienteRecord("Giovanni  Verga", "vergagiovanni@polito.it", "Bronze")),
        Ordine([
            RigaOrdine(ProdottoRecord("Scarpe", 200.0), 1),
            RigaOrdine(ProdottoRecord("Maglietta", 10.0), 3),
            RigaOrdine(ProdottoRecord("IPhone", 1300.0), 1)
        ], ClienteRecord("Salvatore Fargione", "fargionesalvatore@polito.it", "Silver"))
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_gli_ordini()

    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()
