import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord



class DAO:

    def getAllProdotti(self):
        #cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "politecnico.2026",
        #    host = "127.0.0.1",
        #     database = "sw_gestionale"
        #)
        cnx = DBConnect.getConnection()


        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from prodotti")
        row = cursor.fetchall()

        res = []
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = mysql.connector.connect(
             user = "root",
             password = "politecnico.2026",
            host = "127.0.0.1",
             database = "sw_gestionale"
         )


        cursor = cnx.cursor(dictionary=True)
        cursor.execute("Select * from clienti")
        row = cursor.fetchall()

        res = []
        for c in row:
            res.append(ClienteRecord(c["nome"], c["email"], c["categoria"]))

        cursor.close()
        cnx.close()
        return res

    def addProdotto(self, prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="politecnico.2026",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor()
        query = """
                        insert into prodotti
                            (nome, prezzo) values (%s, %s)
        """
        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))
        row = cursor.fetchall()

        cnx.commit() # va a modificare il database

        cursor.close()
        cnx.close()
        return

    def addCliente(self, cliente):
        cnx = mysql.connector.connect(
            user="root",
            password="politecnico.2026",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor()
        query = """
                        insert into clienti
                            (nome, email, categoria) values (%s, %s, %s)
        """
        cursor.execute(query, (cliente.name, cliente.email, cliente.categoria))
        row = cursor.fetchall()

        cnx.commit() # va a modificare il database

        cursor.close()
        cnx.close()
        return

    def hasCliente(self, cliente):
        cnx = mysql.connector.connect(
             user = "root",
             password = "politecnico.2026",
            host = "127.0.0.1",
             database = "sw_gestionale"
         )


        cursor = cnx.cursor(dictionary=True)
        query = "Select * from clienti where email = %s"
        cursor.execute(query,  (cliente.email,))
        row = cursor.fetchall()


        cursor.close()
        cnx.close()
        return len(row) > 0

    def hasProdotto(self, prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="politecnico.2026",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prodotto.name,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0






if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()
    mydao.getAllClienti()
