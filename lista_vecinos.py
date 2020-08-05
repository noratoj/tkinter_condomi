from conexion import *


class vecinos(Conexion):
    
    def listarVecinos(self, queries):
      cnx = self.conectar()
      registros = cnx.cursor()
      registros.execute(queries)
      reg1=registros.fetchall()
      #print(len(reg1))
      #print(registros.rowcount)
      self.cerrarConexion(cnx)
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
      query = "SELECT tb1.campo_des FROM tbreferencia tb1 where tb1.contador= %s" % ref_campo
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)


    def obtener_cuantos(self, queries):
      query = queries
      registros = vecinos()
      reg_1 = registros.listarVecinos(query)
      return(reg_1)

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
