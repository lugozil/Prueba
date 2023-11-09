# import mysql.connector

# conexion = mysql.connector.connect(user='root', password='root',
#                                     host='localhost',
#                                     database='pruebapos',
#                                     port='3307')
# print(conexion)

import pymysql 

class DataBase: 

    #conexion a BD
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password='',
            db='ejercicio2'
        )
        self.cursor = self.connection.cursor()
        print("Conexion establecida")

    # Select de los datos a insertar en el pdf
    def select_user(self,id): 
        # sql = 'SELECT id, username, email FROM users WHERE id = {id}'.format(id)

        # try:
        #     self.cursor.execute(sql)
        #     user = self.cursor.fetchall() 

        #     print("Id:", user[0])
        #     print("Username:", user[1])
        #     print("Email:", user[2])

#         SELECT
#   e.nombre_est,
#   e.direccion_est,
#   e.cp_est,
#   e.localidad_est,
#   r.estatus,
#   r.valor,
#   em.nombre_emp,
#   em.cif_emp,
#   em.direccion_emp
# FROM
#   instalaciones i
#   JOIN establecimientos e ON i.id_establecimiento = e.id_establecimiento
#   JOIN empresas em ON i.id_empresa = em.id_empresa
#   JOIN retornos r ON e.id_retorno = r.id_retorno;

        sql = 'SELECT * FROM instalaciones WHERE id = {id}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall() 

            print("Id:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])

        
        except Exception as e:
            raise

database = DataBase()
database.select_user(1)
        