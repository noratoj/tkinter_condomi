from conexion import *


class vecinos(Conexion):
    
    def listarVecinos(self, queries):
        cnx = self.conectar()
        registros = cnx.cursor()
        registros.execute(queries)
        reg1=registros.fetchall()
        print(len(reg1))
        print(registros.rowcount)
        cnx1 = self.cerrarConexion(cnx)
        return(reg1)

    def combo_add(self, ref_campo):
      q2 = ref_campo
      query = "SELECT tb1.campo_des, tb1.contador FROM tbreferencia tb1 where tabla LIKE '%"+q2+"%' order by campo_des"    
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      data=[]
      for row in reg_1:
          string2=row[0]
          string_length=len(string2)+60
          string3 = string2.ljust(string_length)
          #print(string3+str(row[1]))
          data.append(string3+str(row[1]))  
      return(data)

    def referencia(self, ref_campo):
      q2 = ref_campo
      query = "SELECT tb1.campo_des, tb1.contador FROM tbreferencia tb1 where tabla LIKE '%"+q2+"%' order by campo_des"    
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)

    def obtener_desc(self, ref_campo):
      q2 = ref_campo
      query = "SELECT tb1.campo_des FROM tbreferencia tb1 where tb1.contador= %s" % ref_campo
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)

    def obtener_cuantos(self, queries):
      query = queries
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)

