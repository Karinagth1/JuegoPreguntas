import sqlite3

laConexion = sqlite3.connect("BDReto")

class Registro_datos():

    def busca_users(self, usuarios):
        cur = self.laConexion.cursor()
        sqlite3 = "SELECT * FROM JUGADOR WHERE correo = {}".format(usuarios)
        cur.execute(sqlite3)
        correox = cur.fetchall()
        cur.close()     
        return correox 

    def busca_password(self, contrasena):
        cur = self.laConexion.cursor()
        sqlite3 = "SELECT * FROM JUGADOR WHERE contrasena = {}".format(contrasena)
        cur.execute(sqlite3)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx 