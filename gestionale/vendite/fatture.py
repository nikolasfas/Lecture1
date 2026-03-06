from dataclasses import dataclass
from datetime import date

from gestionale.core.cliente import Cliente
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            f"="*60,
            #intestazione della fattura, ovvero data e numero fattura
            f"Fattura no. {self.numero_fattura} del {self.data}",
            f"="*60,
            #dettagli del cliente
            f"Cliente: {self.ordine.cliente.name}",
            f"Categoria: {self.ordine.cliente.categoria}",
            f"Mail: {self.ordine.cliente.email}",
            f"-"*60,
            f"DETTAGLIO ORDINE"
        ]
        for i, riga in enumerate(self.ordine.righe):
            linee.append(
                f"{i}. "
                f"{riga.prodotto.name} "
                f"Q.tà {riga.quantita} x {riga.prodotto.prezzo_unitario} = "
                f"Totale {riga.totale_riga()}"
            )

        linee.extend([
            f"-"*60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA(22%): {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            f"=" * 60
        ])

        return "\n".join(linee)



def test_modulo():
    p1 = ProdottoRecord("Samsung laptop", 1200.0)
    p2 = ProdottoRecord("Mouse wireless", 25.0)
    p3 = ProdottoRecord("Tablet Samsung", 600.0)
    cliente = Cliente("Francesco Lazzaro", "francescolazzaro@polito.it", "Gold")
    ordine = Ordine(righe=[
        RigaOrdine(p1, 1),
        RigaOrdine(p2, 5),
        RigaOrdine(p3, 3)
    ], cliente=cliente)
    fattura = Fattura(ordine, "2026/01", date.today())
    print(fattura.genera_fattura())

if __name__ == "__main__":
    test_modulo()