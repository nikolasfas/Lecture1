import pathlib

import mysql


class DBConnect:

    _mypool =None

    def __init__(self):
        # Per implementare il pattern singletone ed impedirte al chiamante di implementare l'istanza di classe
        raise RuntimeError("Attenzione non devi creare un'istanza di questa classe. Usa i metodi di classe!")

    @classmethod
    def getConnection(cls):
        if cls._mypool is None:
            try:
                #cnx = mysql.connector.connect(
                #    user = "root",
                #    password = "politecnico.2026",
                #    host="127.0.0.1",
                #    database="sw_gestionale",
                #)
                cls.myPool = mysql.connector.pooling.MySQLConnectionPool(
                    #user ="root",
                    #password="politecnico.2026",
                    #host = "127.0.0.1",
                    #database="sw_gestionale",
                    pool_size = 3,
                    pool_name = "myPool",
                    option_file = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                return cls.myPool.get_connection()
            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            # Allora il pool già esiste e ritorno la connessione
            return cls._mypool.get_connection()

