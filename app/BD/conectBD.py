import sqlite3

laConexion = sqlite3.connect("BDReto")
try:
    laConexion.execute("""
                            create table JUGADOR (
                                id integer primary key autoincrement,
                                nombre_usu varchar(50),
                                correo varchar(100),
                                contrasena varchar(50)
                            )
                        """)
    print("Se creo la tabla de JUGADOR")
except sqlite3.OperationalError:
    print("Ya existe la tabla JUGADOR")

laConexion.close()
