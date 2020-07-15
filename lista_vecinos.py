from conexion import *


class vecinos(Conexion):
    
    def listarVecinos(self, queries):
        cnx = self.conectar()
        #registros = cnx.cursor()
        registros = cnx.cursor()
        #query = "SELECT * FROM vecinos_temporal"
        #query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador order by id_torre,id_piso,apto,id_miembro"
        #query="SELECT nro_cedula, nombre1, apellido_1, id_piso, apto, id_torre from vecinos_temporal"
        registros.execute(queries)
        reg1=registros.fetchall()
        print(len(reg1))
        print(registros.rowcount)
        cnx1 = self.cerrarConexion(cnx)
        return(reg1)

