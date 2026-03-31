# Scrivere un software gestonale che abbia le seguenti caratteritiche
# 1) Supportare l'arrivo e la gestioone di ordini
# 2) Quando arriva un nuovo ordine, lo aggiungo ad una coda,
#       assicurandomi che sia seguita da
import random
from collections import deque, Counter, defaultdict

from dao.dao import DAO
from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdine:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)
        self._dao = DAO()
        self._allP = []
        self._allC = []
        self._fill_data()

    def _fill_data(self):
        # Leggo prodotti e clienti dal  DB, e poi creao degli ordini randomici per testare la mia app
        self._allP = self._dao.getAllProdotti()
        self._allC = self._dao.getAllClienti()

        for i in range(10):
            indexP = random.randint(0, len(self._allP) -1)
            indexC = random.randint(0, len(self._allC) -1)
            ordine = Ordine([RigaOrdine(self._allP[indexP], random.randint(1, 5))],
                            self._allC[indexC])
            self.add_ordine(ordine)

    def add_ordine(self, ordine: Ordine):

        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def crea_ordine(self, nomeP, prezzoP, quantitaP,
                    nomeC, emailC, categoriaC):

        prod = ProdottoRecord(nomeP, prezzoP)
        client = ClienteRecord(nomeC, emailC, categoriaC)

        self._update_DB(prod, client)

        return Ordine([RigaOrdine(prod, quantitaP)],client)

    def _update_DB(self, prod, client):
        if not self._dao.hasProdotto(prod):
            self._dao.addProdotto(prod)

        if not self._dao.hasCliente(client):
            self._dao.addCliente(client)

    def processo_prossimo_ordine(self):
        """Questo metodo legge il prossimo ordine in coda e lo gestisce"""
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)

        # Assicuriamoci che un ordine da processare esista.
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda.")
            return False, Ordine([], ClienteRecord("", "", ""))

        # Se esiste, gestiamo il primo in coda.
        ordine = self._ordini_da_processare.popleft()  # Loigica FIFO

        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        # Aggiornare statistiche sui prodotti venduti --
        # Laptop - 10 +1
        # Mouse - 5 +2
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        # Raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        # Archiviamo l'ordine
        self._ordini_processati.append(ordine)

        print("Ordine correttamente processato.")

        return True, ordine


    def processa_tutti_gli_ordini(self):
        """Processa tutti gli ordini attualmente presenti in coda."""
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")

        ordini = []

        while self._ordini_da_processare:
            _, ordine = self.processo_prossimo_ordine()
            ordini.append(ordine)
        print("Tutti gli ordini sono stati processati.")
        return ordini

    def get_statistiche_prodotti(self, top_n: int=5):
        valori = []
        for prodotto, quantità in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantità))
        return valori

    def get_distribuzione_categorie(self):
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum(o.totale_lordo(0.22) for o in ordini)
            valori.append(cat, totale_fatturato)
        return valori

    def stampa_riepilogo(self):
        """Stampa info di massima"""
        print("\n" + "=" * 60)
        print("Stato attuale del business:")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")

        print("Prodotti più venduti:")
        for prod, quantità in self.get_statistiche_prodotti():
            print(f"{prod}: {quantità}")

        print(f"Fatturato per categoria:")
        for cat, fatturato in self.get_distribuzione_categorie():
            print(f"{cat} : {fatturato}")

    def get_riepilogo(self):
        """restituisce una stringa con le info di massima"""
        sommario = ""
        sommario += "\n" + "=" * 60
        sommario += f"\n Ordini correttamente gestiti: {len(self._ordini_processati)}"
        sommario += f"\n Ordini in coda: {len(self._ordini_da_processare)}"

        sommario += "\n Prodotti più venduti:"
        for prod, quantità in self.get_statistiche_prodotti():
            sommario += f"\n {prod}: {quantità}"

        sommario += f"\n Fatturato per categoria:"
        for cat, fatturato in self.get_distribuzione_categorie():
            sommario += f"\n {cat} : {fatturato}"
        sommario += "\n" + "=" * 60
        return sommario

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
