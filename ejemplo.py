import mysql.connector

config = {
    'user': 'root',
    'password': '3875',
    'host': '127.0.0.1',
    'database': 'condo'
    }

connection = mysql.connector.connect(user='root', password='3875', database='condo', host='127.0.0.1')
#connection = mysql.connector.connect(config)

cursor = connection.cursor()

query = "SELECT * FROM vecinos_temporal"

cursor.execute(query)

count = cursor.rowcount 
count = cursor.fetchall()
print(count) # This prints -1 as the rows have not yet been fetched

i = 0
"""for row in cursor:
    i += 1
    # Save row to file
    print(i)
    print("Progress {:2.1%}".format(i / count), end="\r") # This prints a negative number since count is -1
"""
"""import mysql.connector
from mysql.connector import errorcode

class Conexion:
    
    def conectar(self):        
        try:
            conexion = mysql.connector.connect(user='root', password='3875', database='condo', host='127.0.0.1')
            print("conecta")            
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de usuario o contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:    
                print("Error en la Base de Datos")
            else:
                print(err)
        else:
            conexion.close()
            print("Conexion cerrada")
        input()

obj = Conexion()
obj.conectar()
"""