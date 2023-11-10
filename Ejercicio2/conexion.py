import pymysql 
import PyPDF3
from datetime import datetime

class DataBase: 

    # Conexion a BD
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password='',
            db='ejercicio2'
        )
        self.cursor = self.connection.cursor()
        print("Conexion establecida")

    # Consulta con la BD
    def consulta_bd(self, id): 

        #datos establecimientos
        sql_establecimiento = 'SELECT id_establecimiento, nombre, direccion, cp, localidad, provincia, persona_contacto, telefono_contacto, correo, sector_actividad, check_cajero, check_datafono, comision, retorno_grupo, retorno_porcentaje, fondo_inicial, aportacion, reposicion FROM establecimientos WHERE id_establecimiento = {}'.format(id)

        #datos de empresa
        sql = 'SELECT id_empresa, nombre, cif, direccion_fiscal, cp, localidad, provincia, nombre_admin, dni_admin FROM empresas WHERE id_empresa = {}'.format(id)

        try:
            self.cursor.execute(sql_establecimiento)
            establecimiento = self.cursor.fetchall() 
        
            self.cursor.execute(sql)
            empresa = self.cursor.fetchall() 
        
        except Exception as e:
            raise

        return establecimiento, empresa

    # Escritura del pdf

def relleno_pdf(establecimiento,empresa): 
        
        est = establecimiento[0]
        emp = empresa[0]

        # Rutas 
        ruta_pdf_vacio = 'pdf/Formulario_vacio.pdf'
        ruta_pdf_lleno = 'pdf/Formulario_lleno.pdf'

        # Abre el PDF original en modo lectura
        with open(ruta_pdf_vacio, 'rb') as pdf_file:
            pdf_reader = PyPDF3.PdfFileReader(pdf_file)
            pdf_writer = PyPDF3.PdfFileWriter()

            # Paginas del pdf
            for page_num in range(len(pdf_reader.pages)): 
                page = pdf_reader.pages[page_num]
                pdf_writer.addPage(page)

            # Rellena de campos
            pdf_writer.updatePageFormFieldValues(page, {
                'Fecha': datetime.now(),
                'Nombre establecimiento': est[1],
                'Dirección': est[2],
                'CP': est[3],
                'Localidad': est[4],
                'Provincia': est[5],
                'Persona contacto': est[6],
                'Teléfono contacto': est[7],
                'email': est[8],
                'Sector actividad': est[9],
                'Check cajero': est[10],
                'Check datáfono': est[11],
                'comisión': est[12],
                'Retorno grupo': est[13],
                'porcentaje retorno': est[14],
                'Fondo inicial': est[15],
                'Aportacion fondo grupo': est[16],
                'Método reposición grupo': est[17],
                'Nombre empresa': emp[1],
                'CIF': emp[2],
                'Dirección Fiscal': emp[3],
                'CP 2': emp[4],
                'Localidad 2': emp[5],
                'Provincia 2': emp[6],
                'Nombre administrador': emp[7],
                'DNI administrador': emp[8],
            })

            # Guarda el PDF llenado 
            with open(ruta_pdf_lleno, 'wb') as pdf_filled_file:
                pdf_writer.write(pdf_filled_file)

            print("PDF llenado guardado en:", ruta_pdf_lleno)


database = DataBase()
resultado = database.consulta_bd(1)
establecimiento, empresa = resultado 
relleno_pdf(establecimiento,empresa)


        