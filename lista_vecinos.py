from conexion import *

"""
Permite tener todas las actividades referentes a lo relacionado con la conexión a BD->:Base de datos y
el CRUD de las tablas pertenecientes a la BD. Igual los SELECT que se requieran.
"""

class vecinos(Conexion):

    #Realizar un select. Puede ser llamao desde cualquier sitio. Enviando el SELECT q se necesita    
    def listarVecinos(self, queries):
      cnx = self.conectar()
      registros = cnx.cursor()
      registros.execute(queries)
      reg1=registros.fetchall()
      self.cerrarConexion(cnx)
      return(reg1)

    #Poder armar un combo. Enviando el CAMPO que están solicitando. TBREFERENCIA CAMPO=TABLA
    #si es con_string = 1, armará la cadena necesaria en el combo
    #si es con_string = 0, enviará el resultado del reg1, para ramar un listado resultante
    def combo_add(self, ref_campo, con_string):

      q2 = ref_campo
      query = "SELECT tb1.campo_des, tb1.contador FROM tbreferencia tb1 where tabla LIKE '%"+q2+"%' order by campo_des"    
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      if (con_string == 1):
        data=[]
        for row in reg_1:
            string2=row[0]
            string_length=len(string2)+60
            string3 = string2.ljust(string_length)
            #print(string3+str(row[1]))
            data.append(string3+str(row[1]))  
      else:
        data=reg_1
      return(data)

    #Descripcion del contador a consultar de la tabla TBREFERENCIA
    def obtener_desc(self, ref_campo):
      query = "SELECT tb1.campo_des FROM tbreferencia tb1 where tb1.contador= %s" % ref_campo
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)

    #número de registros tabla
    def obtener_cuantos(self, queries):
      query = queries
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)

    #INSERT EN LA TABLA vecinos_temporal
    def insertvec(self, datos):
      cnx = self.conectar()
      sql = "Insert into vecinos_temporal(nro_cedula,nombre1,nombre_2,apellido_1,apellido_2,telefono_1,"
      sql = sql + "telefono_2,fecha_nac,correo_elec, profesion,sexo,id_torre,id_piso,apto,id_miembro,grupo_fam,medicamentos,"
      sql = sql + "observacion,antecedentes) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      registros = cnx.cursor()
      #print(sql)
      #print(datos)
      registros.execute(sql,datos)
      cnx.commit()
      self.cerrarConexion(cnx)
      #return(reg1)

    #UPDATE EN LA TABLA vecinos_temporal
    def updatevec(self, datos):
      cnx = self.conectar()
      sql = "update vecinos_temporal set nro_cedula=%s, nombre1=%s,nombre_2=%s,apellido_1=%s,apellido_2=%s,telefono_1=%s,"
      sql = sql + "telefono_2=%s,fecha_nac=%s,correo_elec=%s, profesion=%s,sexo=%s,id_torre=%s,id_piso=%s,apto=%s,"
      sql = sql + "id_miembro=%s,grupo_fam=%s,medicamentos=%s,observacion=%s,antecedentes=%s where id_vecino=%s"
      registros = cnx.cursor()
      #print(sql)
      #print(datos)
      registros.execute(sql,datos)
      cnx.commit()
      self.cerrarConexion(cnx)

    #DELETE EN LA TABLA vecinos_temporal
    def eliminarreg(self, datos):
      cnx = self.conectar()
      sql = "delete from vecinos_temporal where id_vecino=%s"
      registros = cnx.cursor()
      registros.execute(sql,datos)
      cnx.commit()
      self.cerrarConexion(cnx)
      return registros.rowcount #retorna cantidad de filas eliminadas...debe ser 1

    #INSERT EN LA TABLA TBREFERENCIA
    def insertref(self, datos):
      cnx = self.conectar()
      sql = "Insert into tbreferencia(contador,tabla,campo_des,orden, relacionado_con)"
      sql = sql + "values (%s,%s,%s,%s,%s)"
      registros = cnx.cursor()
      registros.execute(sql,datos)
      cnx.commit()
      self.cerrarConexion(cnx)

    #UPDATE EN LA TABLA TBREFERENCIA
    def updateref(self, datos):
      cnx = self.conectar()
      sql = "update tbreferencia set tabla=%s, campo_des=%s,orden=%s where id_contador=%s"
      registros = cnx.cursor()
      registros.execute(sql,datos)
      cnx.commit()
      self.cerrarConexion(cnx)

    #DELETE EN LA TABLA TBREFERENCIA
    def eliminarref(self, datos):
      cnx = self.conectar()
      sql = "delete from tbreferencia where id_contador=%s"
      registros = cnx.cursor()
      registros.execute(sql,datos)
      cnx.commit()
      self.cerrarConexion(cnx)
      return registros.rowcount #retorna cantidad de filas eliminadas...debe ser 1
