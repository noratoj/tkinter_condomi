import mysql.connector
from mysql.connector import errorcode

class Conexion:
    
    def conectar(self):        
        try:
            conexion = mysql.connector.connect(user='root', password='3875', database='condo', host='127.0.0.1')
            print("conecta")
            return(conexion)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de usuario o contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:    
                print("Error en la Base de Datos")
            else:
                print(err)
            return None

    def cerrarConexion(self, conexion):
        conexion.close()
        print("Conexion cerrada")
